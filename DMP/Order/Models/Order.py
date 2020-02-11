from django.db import models
from rest_framework import serializers


class OrderInfo(models.Model):
    """
    订单详情
    """
    ## 是否需要发货
    DELIVERY_NEED_STATUS_YES = 1
    DELIVERY_NEED_STATUS_NO = 0
    DELIVERY_NEED_CHOICE = (
        (DELIVERY_NEED_STATUS_YES, '需要配送'),
        (DELIVERY_NEED_STATUS_NO, '无需配送')
    )
    ## 付款状态
    PAY_STATUS_UNPAID = 0
    PAY_STATUS_PAID = 1
    PAY_STATUS_REFUND = 2
    PAY_STATUS_CHOICE = (
        (PAY_STATUS_UNPAID, '待付款'),
        (PAY_STATUS_PAID, '已付款'),
        (PAY_STATUS_REFUND, '已退回')
    )
    ## 订单状态
    ORDER_STATUS_UNCONFIRMED = 1
    ORDER_STATUS_WAIT_DELIVERY = 2
    ORDER_STATUS_DELIVERY = 3
    ORDER_STATUS_FINISHED = 4
    ORDER_STATUS_REFUNDING = 5
    ORDER_STATUS_REFUND = 6
    ORDER_STATUS_REFUND_FAILED = 7
    ORDER_STATUS_CANCELED = 8

    ORDER_STATUS_CHOICE = (
        (ORDER_STATUS_UNCONFIRMED, '待确认'),
        (ORDER_STATUS_WAIT_DELIVERY, '待发货'),
        (ORDER_STATUS_DELIVERY, '已发货'),
        (ORDER_STATUS_FINISHED, '已完成'),
        (ORDER_STATUS_REFUNDING, '退款中'),
        (ORDER_STATUS_REFUND, '退款完成'),
        (ORDER_STATUS_REFUND_FAILED, '退款失败'),
        (ORDER_STATUS_CANCELED, '已取消'),
    )

    business_id = models.PositiveIntegerField("商户id")
    customer_id = models.PositiveIntegerField("客户id", default=0)
    operator_id = models.PositiveIntegerField("录入人id", default=0)
    unique_code = models.CharField("订单唯一标示", max_length=20)
    name = models.CharField("订单名称", max_length=255, default="")
    price = models.DecimalField("价格", default=0, max_digits=12, decimal_places=2)
    discount_price = models.DecimalField("优惠价格", default=0, max_digits=12, decimal_places=2)
    original_price = models.DecimalField("优惠价格", default=0, max_digits=12, decimal_places=2)
    custom_name = models.CharField("客户名称", max_length=20, default="")
    mobile = models.CharField("客户联系方式", max_length=20, default="")
    country_id = models.PositiveIntegerField("国家id", default=0)
    state_id = models.PositiveIntegerField("省份id", default=0)
    city_id = models.PositiveIntegerField("城市id", default=0)
    area_id = models.PositiveIntegerField("区域id", default=0)
    address = models.PositiveIntegerField("详细地址", max_length=255, default="")
    express_company_id = models.PositiveIntegerField("快递公司id")
    express_code = models.CharField("快递单号", max_length=20, default="")
    need_delivery = models.PositiveSmallIntegerField("是否需要配送", choices=DELIVERY_NEED_CHOICE,
                                                     default=DELIVERY_NEED_STATUS_YES)
    pay_status = models.PositiveSmallIntegerField("支付状态", choices=PAY_STATUS_CHOICE, default=PAY_STATUS_UNPAID)
    status = models.PositiveSmallIntegerField("订单状态", choices=ORDER_STATUS_CHOICE, default=ORDER_STATUS_UNCONFIRMED)
    delete_flag = models.PositiveSmallIntegerField("删除标记", default=0)
    created_at = models.DateTimeField("产生时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = 'order_info'


class OrderProduct(models.Model):
    """
    订单商品详情
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, db_column='order_info_id',
                              db_constraint=False)
    product_id = models.PositiveIntegerField("商品id")
    product_name = models.CharField("商品名称", max_length=250)
    image_id = models.PositiveIntegerField("图片文件id")
    snapshoot = models.TextField("商品快照信息")
    specification_info = models.CharField("规格信息")
    price = models.DecimalField("价格", default=0, max_digits=12, decimal_places=2)
    discount_price = models.DecimalField("优惠价格", default=0, max_digits=12, decimal_places=2)
    original_price = models.DecimalField("优惠价格", default=0, max_digits=12, decimal_places=2)
    num = models.PositiveIntegerField("购买数量")

    class Meta:
        db_table = 'order_product'


class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__",
        exclude = ["created_at", "updated_at"]
