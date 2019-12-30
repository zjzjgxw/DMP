from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Product.Models.Category import Category, CategorySerializer
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
        except IntegrityError:
            raise

    @classmethod
    def _create_specification(cls, category_id, specification_list):
        pass

    @classmethod
    def _create_attribute(cls, category_id, attribute_list):
        pass
