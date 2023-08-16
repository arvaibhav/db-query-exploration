from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    DateTimeField,
    FloatField,
    IntField,
    BooleanField,
    ListField,
    ReferenceField,
    CASCADE,
    EmbeddedDocumentField,
)
from datetime import datetime


class BaseDocument(Document):
    created_on = DateTimeField(default=datetime.utcnow)
    meta = {"abstract": True}


class BaseEmbeddedDocument(EmbeddedDocument):
    created_on = DateTimeField(default=datetime.utcnow)
    meta = {"abstract": True}


class Category(EmbeddedDocument):
    name = StringField(required=True)
    category_code = StringField(primary_key=True, unique=True, required=True)
    children = ListField(EmbeddedDocumentField("self"))


class CategoryDocument(BaseDocument):
    category = EmbeddedDocumentField(Category)


class Coupon(BaseDocument):
    coupon_code = StringField(required=True)
    campaign_type = IntField(required=True)
    discount_type = IntField(required=True)
    discount_value = IntField(required=True)
    min_order_value = IntField(required=True)
    max_discount = IntField(required=True)


class Store(BaseDocument):
    name = StringField(required=True)
    phone_number = IntField(required=True)
    lat = FloatField(required=True)
    lng = FloatField(required=True)


class StoreCoupon(BaseDocument):
    coupon = ReferenceField("Coupon", required=True, reverse_delete_rule=CASCADE)
    store = ReferenceField("Store", required=True, reverse_delete_rule=CASCADE)


class Customer(BaseDocument):
    name = StringField(required=True)
    phone_number = IntField(required=True)
    addresses = ListField(EmbeddedDocumentField("CustomerAddress"))


class CustomerCoupon(BaseDocument):
    coupon = ReferenceField("Coupon", required=True, reverse_delete_rule=CASCADE)
    customer = ReferenceField("Customer", required=True, reverse_delete_rule=CASCADE)


class CustomerAddress(BaseEmbeddedDocument):
    lat = FloatField(required=True)
    lng = FloatField(required=True)
    text = StringField(required=True)


class CustomerAddressHistory(BaseDocument):
    lat = FloatField(required=True)
    lng = FloatField(required=True)
    customer_address = ReferenceField(
        "CustomerAddress", required=True, reverse_delete_rule=CASCADE
    )


class ProductDetail(BaseDocument):
    name = StringField(required=True)
    image_urls = StringField(required=True)


class LibraryProduct(BaseDocument):
    sp = IntField(required=True)
    mrp = IntField(required=True)
    detail = ReferenceField("ProductDetail")
    price_change_logs = ListField(EmbeddedDocumentField("LibraryProductPriceChangeLog"))
    parent_product = ReferenceField("self", reverse_delete_rule=CASCADE)


class LibraryProductPriceChangeLog(BaseEmbeddedDocument):
    sp = IntField(required=True)
    mrp = IntField(required=True)


class StoreProductPriceChangeLog(BaseEmbeddedDocument):
    sp = IntField(required=True)
    mrp = IntField(required=True)


class StoreProduct(BaseDocument):
    mrp = IntField(required=True)
    sp = IntField(required=True)
    in_stock = IntField(required=True)
    detail = ReferenceField("ProductDetail")
    price_change_logs = ListField(EmbeddedDocumentField("StoreProductPriceChangeLog"))
    store = ReferenceField("Store", default=None, reverse_delete_rule=CASCADE)


class OrderSession(BaseDocument):
    applied_coupon = ReferenceField("Coupon", default=None, reverse_delete_rule=CASCADE)


class Order(BaseDocument):
    customer = ReferenceField("Customer", required=True, reverse_delete_rule=CASCADE)
    customer_location = EmbeddedDocumentField("CustomerAddress")
    applied_coupon = ReferenceField("Coupon", default=None, reverse_delete_rule=CASCADE)
    store = ReferenceField("Store", required=True, reverse_delete_rule=CASCADE)
    state = IntField(required=True, default=1)
    coupon_discount_amount = IntField(default=None)
    product_total = IntField(default=None)
    version = IntField(required=True, default=1)
    products = ListField(EmbeddedDocumentField("OrderProduct"))


class OrderProduct(BaseEmbeddedDocument):
    is_active = BooleanField(required=True, default=True)
    store_product_price_log = EmbeddedDocumentField("StoreProductPriceChangeLog")
    quantity = IntField(required=True, default=1)
    version = IntField(required=True, default=1)
