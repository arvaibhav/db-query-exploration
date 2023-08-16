import pytz as pytz
from django.db import models
from django.utils.timezone import datetime


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.created_on = datetime.utcnow().replace(tzinfo=pytz.UTC)
        super().save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )

    class Meta:
        app_label = "__main__"
        abstract = True
        managed = True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._meta.db_table = cls.__name__.lower()


# Category Model
class Category(BaseModel):
    name = models.CharField(max_length=256)
    category_code = models.CharField(max_length=256, primary_key=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)


# Coupon Model
class Coupon(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    coupon_code = models.CharField(max_length=32)
    campaign_type = models.SmallIntegerField()
    discount_type = models.SmallIntegerField()
    discount_value = models.SmallIntegerField()
    min_order_value = models.SmallIntegerField()
    max_discount = models.SmallIntegerField()


# Store Model
class Store(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    phone_number = models.BigIntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    coupons = models.ManyToManyField(Coupon, through="StoreCoupon")


# Store Coupon Relationship
class StoreCoupon(BaseModel):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


# Customer Model
class Customer(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    phone_number = models.BigIntegerField()
    coupons = models.ManyToManyField(Coupon, through="CustomerCoupon")


# Customer Coupon Relationship
class CustomerCoupon(BaseModel):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


# Customer Address Model
class CustomerAddress(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lng = models.FloatField()
    text = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


# Customer Address History Model
class CustomerAddressHistory(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()
    lng = models.FloatField()
    customer_address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)


# Product Detail Model
class ProductDetail(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=256)
    image_urls = models.TextField()
    categories = models.ManyToManyField(Category, default=None)


# Library Product Model
class LibraryProduct(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    sp = models.SmallIntegerField()
    mrp = models.SmallIntegerField()
    detail = models.OneToOneField(ProductDetail, on_delete=models.CASCADE)
    parent_product = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )


# Library Product Price Change Log Model
class LibraryProductPriceChangeLog(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    sp = models.SmallIntegerField()
    mrp = models.SmallIntegerField()
    library_product = models.ForeignKey(LibraryProduct, on_delete=models.CASCADE)


# Library Product Price Change Log Model
class StoreProductPriceChangeLog(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    sp = models.SmallIntegerField()
    mrp = models.SmallIntegerField()
    store_product = models.ForeignKey("StoreProduct", on_delete=models.CASCADE)


# Store Product Model
class StoreProduct(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    mrp = models.SmallIntegerField()
    sp = models.SmallIntegerField()
    in_stock = models.SmallIntegerField()
    detail = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None, null=True)


# Order Session Model
class OrderSession(BaseModel):
    applied_coupon = models.ForeignKey(
        "Coupon", on_delete=models.CASCADE, null=True, default=None
    )
    created_on = models.DateTimeField(auto_now_add=True)


# Order Model
class Order(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_location = models.ForeignKey(
        CustomerAddressHistory, on_delete=models.CASCADE, default=None, null=True
    )
    order_session = models.ForeignKey(
        OrderSession, on_delete=models.CASCADE, null=True, default=None
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    state = models.SmallIntegerField(default=1)
    coupon_discount_amount = models.SmallIntegerField(default=None, null=True)
    product_total = models.SmallIntegerField(default=None, null=True)

    version = models.SmallIntegerField(default=1)


# Order Product Model
class OrderProduct(BaseModel):
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    store_product_price_log = models.ForeignKey(
        StoreProductPriceChangeLog, on_delete=models.CASCADE
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    version = models.SmallIntegerField(default=1)
