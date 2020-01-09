from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from DMP.Product.Models.Detail import Detail, DetailSerializer


class DetailService(BasicService):
    """
    商品详情服务
    """

    @classmethod
    def create(cls, business_id, **kwargs):
        data = kwargs
        data['business_id'] = business_id
        serializer = DetailSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
        else:
            raise ValidationException(detail=serializer.errors)
        return obj.id

    @classmethod
    def detail(cls, business_id, pk):
        try:
            obj = Detail.objects.detail(pk, business_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException
        serializer = DetailSerializer(obj)
        return serializer.data
