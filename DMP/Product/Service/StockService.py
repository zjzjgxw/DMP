from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from django.db import transaction, IntegrityError
from DMP.Product.Models.Stock import StockInfoSerializer, StockSpecificationDetail, StockInfo
import json


class StockService(BasicService):
    """
    库存服务
    """

    @classmethod
    def create(cls, **kwargs):
        """
        新建库存
        :param kwargs:
        :return:
        """
        cls._validate_kwargs(kwargs)
        try:
            with transaction.atomic('ProductMysql'):
                specifications = kwargs['specifications']
                stock_list = kwargs['stock_list']
                data = {}
                data["product_id"] = kwargs["product_id"]
                data["currency_code"] = kwargs["currency_code"]
                if isinstance(specifications, dict) and isinstance(stock_list, list) and len(stock_list) > 0:
                    data["default_specifications"] = json.dumps(specifications, ensure_ascii=False)
                    serializer = StockInfoSerializer(data=data)
                    if serializer.is_valid():
                        obj = serializer.save()
                        stock_specifications_detail_list = []
                        for item in stock_list:
                            stock_specifications_detail_list.append(StockSpecificationDetail(stock_id=obj.id, **item))
                        StockSpecificationDetail.objects.bulk_create(stock_specifications_detail_list)
                    else:
                        raise ValidationException(detail=serializer.errors)
                    return obj.id
                else:  # 没有具体规格
                    data['last_num'] = kwargs['last_num']
                    data['price'] = kwargs['price']
                    serializer = StockInfoSerializer(data=data)
                    if serializer.is_valid():
                        obj = serializer.save()
                    else:
                        raise ValidationException(detail=serializer.errors)
                    return obj.id

        except IntegrityError:
            raise
        except:
            raise

    @classmethod
    def _validate_kwargs(cls, kwargs):
        if "product_id" not in kwargs:
            raise ValidationException(30003)
        if "currency_code" in kwargs:
            if len(kwargs["currency_code"]) != 3:
                raise ValidationException(30002)
        else:
            raise ValidationException(30001)

    @classmethod
    def detail(cls, product_id):
        """
        获取库存详情
        :param product_id: 商品id
        :return:
        """
        try:
            stock_obj = StockInfo.objects.get(product_id=product_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        return stock_obj.format_data()

    @classmethod
    def update(cls, product_id, **kwargs):
        """
        修改库存信息
        :param product_id:
        :param kwargs:
        :return:
        """
        try:
            stock_obj = StockInfo.objects.get(product_id=product_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExistException()
        if "product_id" in kwargs:
            del kwargs['product_id']
        serializer = StockInfoSerializer(instance=stock_obj, data=kwargs, partial=True)
        specifications = kwargs['specifications']
        stock_list = kwargs['stock_list']
        try:
            with transaction.atomic('ProductMysql'):
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise ValidationException(detail=serializer.errors)
                if isinstance(specifications, dict) and isinstance(stock_list, list) and len(stock_list) > 0:
                    stock_obj.stockspecificationdetail_set.all().delete()  # 删除库存信息
                    stock_specifications_detail_list = []
                    for item in stock_list:
                        stock_specifications_detail_list.append(StockSpecificationDetail(stock_id=stock_obj.id, **item))
                    StockSpecificationDetail.objects.bulk_create(stock_specifications_detail_list)
                return True
        except IntegrityError:
            raise
        except:
            raise

    @classmethod
    def get_prices(cls, product_ids):
        """
        根据商品Id 获取价格信息
        :param product_ids: 商品id列表
        :return:
        """
        obj_list = StockInfo.objects.filter(product_id__in=product_ids)
        res = dict()
        for item in obj_list:
            res[item.product_id] = item.price
        return res

    @classmethod
    def check_stock(cls, product_list):
        """
        根据商品信息，检验库存是否足够
        :param product_list:
        :return:
        """
        if not isinstance(product_list, list):
            raise ValidationException(10007)
        if len(product_list) == 0:
            raise ValidationException(30005)
        res_dict = {"res": True, "failed": []}
        for info in product_list:
            for item in ["first_specification_name", "second_specification_name"]:
                if item not in info:
                    info[item] = None
            try:
                stock_obj = StockInfo.objects.get(product_id=info['product_id'])
            except ObjectDoesNotExist:
                raise ObjectDoesNotExistException()
            res = stock_obj.check_stock(info["num"], info["first_specification_name"],
                                        info["first_specification_value"], info["second_specification_name"],
                                        info["second_specification_value"])
            if not res:  # 库存不满足
                res_dict["res"] = False
                res_dict["failed"].append(info)
        return res_dict
