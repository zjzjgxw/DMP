from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Product.Models.Category import Category, CategorySerializer, CategoryAttribute, CategorySpecification
from django.db import transaction, IntegrityError


class CategoryService(BasicService):
    """
    商品类目服务
    """

    @classmethod
    def create(cls, business_id, **kwargs):
        data = kwargs
        data['business_id'] = business_id
        try:
            with transaction.atomic('ProductMysql'):
                serializer = CategorySerializer(data=data)
                if serializer.is_valid():
                    obj = serializer.save()
                else:
                    raise ValidationException(serializer.errors)
                if "specification_list" in data:  # 规格参数必传
                    if isinstance(data['specification_list'], list) and len(data['specification_list']) > 0:
                        cls._create_specification(obj.id, data["specification_list"])
                    else:
                        ValidationException(20010)
                else:
                    raise ValidationException(20010)
                if "attribute_list" in data:
                    if isinstance(data['attribute_list'], list) and len(data['attribute_list']) > 0:
                        cls._create_attribute(obj.id, data["attribute_list"])
                    else:
                        ValidationException(20011)
                return obj.id
        except IntegrityError:
            raise

    @classmethod
    def _create_specification(cls, category_id, specification_list):
        if len(specification_list) == 0:
            return False
        object_list = []
        for item in specification_list:
            cls._verify_item(item)
            object_list.append(CategorySpecification(category_id=category_id, name=item["name"], option=item["option"]))
        CategorySpecification.objects.bulk_create(object_list)
        return True

    @classmethod
    def _verify_item(cls, item):
        """
        检验规格和属性
        :param item:
        :return:
        """
        if "name" not in item:
            raise ValidationException(20012)
        if "option" not in item:
            raise ValidationException(20013)
        if len(item["name"]) > 10:
            raise ValidationException(20014)
        if len(item["option"]) > 10:
            raise ValidationException(20015)

    @classmethod
    def _create_attribute(cls, category_id, attribute_list):
        if len(attribute_list) == 0:
            return False
        object_list = []
        for item in attribute_list:
            cls._verify_item(item)
            object_list.append(CategoryAttribute(category_id=category_id, name=item["name"], option=item["option"]))
        CategoryAttribute.objects.bulk_create(object_list)
        return True
