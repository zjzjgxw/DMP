from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Product.Models.Detail import Detail, DetailSerializer, DetailAttribute, MainImages, DescribeImages
from django.db import transaction, IntegrityError


class DetailService(BasicService):
    """
    商品详情服务
    """

    @classmethod
    def create(cls, business_id, **kwargs):
        cls._validate_kwargs(kwargs)
        data = kwargs
        data['business_id'] = business_id
        try:
            with transaction.atomic('ProductMysql'):
                serializer = DetailSerializer(data=data)
                if serializer.is_valid():
                    obj = serializer.save()
                else:
                    raise ValidationException(detail=serializer.errors)
                attribute_list = []
                for item in kwargs['attribute_list']:
                    attribute_list.append(DetailAttribute(detail_id=obj.id, **item))
                DetailAttribute.objects.bulk_create(attribute_list)
                main_image_list = []
                for item in kwargs['main_images']:
                    main_image_list.append(MainImages(detail_id=obj.id, **item))
                MainImages.objects.bulk_create(main_image_list)
                describe_image_list = []
                for item in kwargs["describe_images"]:
                    describe_image_list.append(DescribeImages(detail_id=obj.id, **item))
                DescribeImages.objects.bulk_create(describe_image_list)
                return obj.id
        except IntegrityError:
            raise
        except:
            raise

    @classmethod
    def _validate_kwargs(cls, kwargs):
        if 'attribute_list' in kwargs:
            cls._validate_attribute_list(kwargs['attribute_list'])
        else:
            raise ValidationException(20016)
        if 'main_images' in kwargs:
            cls._validate_main_images(kwargs['main_images'])
        else:
            raise ValidationException(20017)
        if 'describe_images' in kwargs:
            cls._validate_describe_images(kwargs['describe_images'])
        else:
            raise ValidationException(20018)

    @classmethod
    def _validate_attribute_list(cls, attrs):
        for item in attrs:
            if not isinstance(item, dict):
                raise ValidationException(20016)
            if "name" not in item or "option" not in item:
                raise ValidationException(20016)
            if not isinstance(item["name"], str):
                raise ValidationException(20016)
            if not isinstance(item["option"], str):
                raise ValidationException(20016)
        return attrs

    @classmethod
    def _validate_main_images(cls, attrs):
        for item in attrs:
            if not isinstance(item, dict):
                raise ValidationException(20017)
            if "img_id" not in item or "index_no" not in item:
                raise ValidationException(20017)
            if not isinstance(item["img_id"], int):
                raise ValidationException(20017)
            if not isinstance(item["index_no"], int):
                raise ValidationException(20017)
        return attrs

    @classmethod
    def _validate_describe_images(cls, attrs):
        for item in attrs:
            if not isinstance(item, dict):
                raise ValidationException(20018)
            if "img_id" not in item or "index_no" not in item:
                raise ValidationException(20018)
            if not isinstance(item["img_id"], int):
                raise ValidationException(20018)
            if not isinstance(item["index_no"], int):
                raise ValidationException(20018)
        return attrs

    @classmethod
    def detail(cls, business_id, pk):
        try:
            obj = Detail.objects.detail(pk, business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException
        serializer = DetailSerializer(obj)
        return serializer.data
