from DMP.Core.Service import BasicService
from django.core.exceptions import ObjectDoesNotExist
from DMP.Core.Exceptions import ValidationException, ObjectDoesNotExistException
from django.db import transaction, IntegrityError
from DMP.Order.Models.Order import OrderInfo, OrderInfoSerializer


class OrderService(BasicService):
    """
    订单服务
    """

    @classmethod
    def create(cls, **kwargs):
        """
        新建订单
        :param kwargs:
        :return:
        """
        try:
            with transaction.atomic('OrderMysql'):
                pass

        except IntegrityError:
            raise
        except:
            raise
