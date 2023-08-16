from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    SmallInteger,
    BigInteger,
    Float,
    Boolean,
    Text,
    DateTime,
    Integer,
)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Table

Base = declarative_base()
# Associative tables for many-to-many relationships
store_coupon_association = Table(
    "store_coupon",
    Base.metadata,
    Column("store_id", Integer, ForeignKey("store.id")),
    Column("coupon_id", Integer, ForeignKey("coupon.id")),
)

customer_coupon_association = Table(
    "customer_coupon",
    Base.metadata,
    Column("customer_id", Integer, ForeignKey("customer.id")),
    Column("coupon_id", Integer, ForeignKey("coupon.id")),
)


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    __tablename__ = lambda cls: f"__name__{cls.__name__.lower()}"


class Category(BaseModel):
    name = Column(String(256))
    category_code = Column(String(256), unique=True)
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)


class Coupon(BaseModel):
    coupon_code = Column(String(32))
    campaign_type = Column(SmallInteger)
    discount_type = Column(SmallInteger)
    discount_value = Column(SmallInteger)
    min_order_value = Column(SmallInteger)
    max_discount = Column(SmallInteger)
    stores = relationship(
        "Store", secondary=store_coupon_association, back_populates="coupons"
    )
    customers = relationship(
        "Customer", secondary=customer_coupon_association, back_populates="coupons"
    )


class Store(BaseModel):
    name = Column(String(128))
    phone_number = Column(BigInteger)
    lat = Column(Float)
    lng = Column(Float)
    coupons = relationship(
        "Coupon", secondary=store_coupon_association, back_populates="stores"
    )
    store_products = relationship("StoreProduct", backref="store")


class StoreCoupon(BaseModel):
    coupon_id = Column(Integer, ForeignKey("coupon.id"), primary_key=True)
    store_id = Column(Integer, ForeignKey("store.id"), primary_key=True)
    coupons = relationship(
        "Coupon", secondary=customer_coupon_association, back_populates="customers"
    )


class Customer(BaseModel):
    name = Column(String(128))
    phone_number = Column(BigInteger)


class CustomerCoupon(BaseModel):
    coupon_id = Column(Integer, ForeignKey("coupon.id"), primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), primary_key=True)


class CustomerAddress(BaseModel):
    lat = Column(Float)
    lng = Column(Float)
    text = Column(Text)
    customer_id = Column(Integer, ForeignKey("customer.id"))


class CustomerAddressHistory(BaseModel):
    lat = Column(Float)
    lng = Column(Float)
    customer_address_id = Column(Integer, ForeignKey("customeraddress.id"))


class ProductDetail(BaseModel):
    name = Column(String(256))
    image_urls = Column(Text)
    library_product = relationship(
        "LibraryProduct", back_populates="detail", uselist=False
    )


class LibraryProduct(BaseModel):
    sp = Column(SmallInteger)
    mrp = Column(SmallInteger)
    detail_id = Column(Integer, ForeignKey("productdetail.id"), unique=True)
    detail = relationship("ProductDetail", back_populates="library_product")
    parent_product_id = Column(Integer, ForeignKey("libraryproduct.id"), nullable=True)


class LibraryProductPriceChangeLog(BaseModel):
    sp = Column(SmallInteger)
    mrp = Column(SmallInteger)
    library_product_id = Column(Integer, ForeignKey("libraryproduct.id"))


class StoreProductPriceChangeLog(BaseModel):
    sp = Column(SmallInteger)
    mrp = Column(SmallInteger)
    store_product_id = Column(Integer, ForeignKey("storeproduct.id"))


class StoreProduct(BaseModel):
    mrp = Column(SmallInteger)
    sp = Column(SmallInteger)
    in_stock = Column(SmallInteger)
    detail_id = Column(Integer, ForeignKey("productdetail.id"))
    store_id = Column(Integer, ForeignKey("store.id"), nullable=True)


class OrderSession(BaseModel):
    applied_coupon_id = Column(Integer, ForeignKey("coupon.id"), nullable=True)
    orders = relationship("Order", backref="order_session")


class Order(BaseModel):
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer_location_id = Column(
        Integer, ForeignKey("customeraddresshistory.id"), nullable=True
    )
    order_session_id = Column(Integer, ForeignKey("ordersession.id"), nullable=True)
    store_id = Column(Integer, ForeignKey("store.id"))
    state = Column(SmallInteger, default=1)
    coupon_discount_amount = Column(SmallInteger, nullable=True)
    product_total = Column(SmallInteger, nullable=True)
    version = Column(SmallInteger, default=1)


class OrderProduct(BaseModel):
    is_active = Column(Boolean, default=True)
    store_product_price_log_id = Column(
        Integer, ForeignKey("storeproductpricechangelog.id")
    )
    order_id = Column(Integer, ForeignKey("order.id"))
    quantity = Column(SmallInteger, default=1)
    version = Column(SmallInteger, default=1)


UniqueConstraint("libraryproduct.detail_id")
