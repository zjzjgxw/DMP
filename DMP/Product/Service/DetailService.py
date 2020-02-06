from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Product.Models.Detail import Detail, DetailSerializer, DetailAttribute, MainImages, DescribeImages, \
    DetailAttributeSerializer, MainImagesSerializer, DescribeImagesSerializer
from django.db import transaction, IntegrityError
from DMP.File.Service.FileService import FileService


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
        ret_data = serializer.data

        ret_data['attribute_list'] = DetailAttributeSerializer(obj.detailattribute_set, many=True).data
        ret_data['main_images'] = MainImagesSerializer(obj.mainimages_set, many=True).data
        file_ids = []
        for item in ret_data['main_images']:
            file_ids.append(item['img_id'])
        ret_data['describe_images'] = DescribeImagesSerializer(obj.describeimages_set, many=True).data
        for item in ret_data['describe_images']:
            file_ids.append(item['img_id'])
        ret_data['file_map'] = cls._file_info(file_ids)
        return ret_data

    @classmethod
    def _file_info(cls, file_ids):
        service = FileService()
        return service.list(file_ids)

    @classmethod
    def update(cls, business_id, pk, **kwargs):
        cls._validate_kwargs(kwargs)
        try:
            obj = Detail.objects.detail(pk, business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException
        try:
            with transaction.atomic('ProductMysql'):
                serializer = DetailSerializer(obj, kwargs, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise ValidationException(serializer.errors)
                attribute_list = []
                for item in kwargs['attribute_list']:
                    attribute_list.append(DetailAttribute(detail_id=obj.id, **item))
                DetailAttribute.objects.filter(detail_id=obj.id).delete()
                DetailAttribute.objects.bulk_create(attribute_list)
                main_image_list = []
                for item in kwargs['main_images']:
                    main_image_list.append(MainImages(detail_id=obj.id, **item))
                MainImages.objects.filter(detail_id=obj.id).delete()
                MainImages.objects.bulk_create(main_image_list)
                describe_image_list = []
                for item in kwargs["describe_images"]:
                    describe_image_list.append(DescribeImages(detail_id=obj.id, **item))
                DescribeImages.objects.filter(detail_id=obj.id).delete()
                DescribeImages.objects.bulk_create(describe_image_list)
                return True
        except IntegrityError:
            raise

    @classmethod
    def delete(cls, business_id, pk):
        try:
            obj = Detail.objects.detail(pk, business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException
        obj.delete_flag = 1
        obj.save()
        return True

    @classmethod
    def list(cls, business_id, name=None, category_id=None, status_type=None, page=1, page_size=10):
        kwargs = {"business_id": business_id}
        if name is not None:
            kwargs["name"] = name
        if category_id is not None:
            kwargs["category_id"] = category_id
        if status_type is not None:
            kwargs["status_type"] = status_type
        count = Detail.objects.count(**kwargs)
        object_list = Detail.objects.list(page, page_size, **kwargs)
        serializer = DetailSerializer(object_list, many=True)
        return {"list": serializer.data, "count": count}
