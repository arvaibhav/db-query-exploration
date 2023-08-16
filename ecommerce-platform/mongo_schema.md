### BaseDocument

Abstract base class for other document models.

- **created_on**: DateTimeField
    - Contains the creation date and time.
    - Default: Current UTC time.

### BaseEmbeddedDocument

Abstract base class for other embedded document models.

- **created_on**: DateTimeField
    - Contains the creation date and time.
    - Default: Current UTC time.

### Category

An embedded document representing a category.

- **name**: StringField
    - The name of the category.
    - Constraints: Required.
- **category_code**: StringField
    - The code of the category.
    - Constraints: Required, Primary Key, Unique.
- **children**: ListField of EmbeddedDocumentField
    - Child categories, recursively defined.

### CategoryDocument

A document representing a category.

- **category**: EmbeddedDocumentField
    - The embedded category.

### Coupon

A document representing a coupon.

- **coupon_code**: StringField
    - The code of the coupon.
    - Constraints: Required.
- **campaign_type**: IntField
    - Type of campaign.
    - Constraints: Required.
- **discount_type**: IntField
    - Type of discount.
    - Constraints: Required.
- **discount_value**: IntField
    - Value of discount.
    - Constraints: Required.
- **min_order_value**: IntField
    - Minimum order value for applying the coupon.
    - Constraints: Required.
- **max_discount**: IntField
    - Maximum discount value.
    - Constraints: Required.

### Store

A document representing a store.

- **name**: StringField
    - The name of the store.
    - Constraints: Required.
- **phone_number**: IntField
    - The phone number of the store.
    - Constraints: Required.
- **lat**: FloatField
    - Latitude coordinate.
    - Constraints: Required.
- **lng**: FloatField
    - Longitude coordinate.
    - Constraints: Required.

### StoreCoupon

A document representing the association between a store and a coupon.

- **coupon**: ReferenceField
    - Reference to a coupon document.
    - Constraints: Required, CASCADE delete.
- **store**: ReferenceField
    - Reference to a store document.
    - Constraints: Required, CASCADE delete.

### Customer

A document representing a customer.

- **name**: StringField
    - The name of the customer.
    - Constraints: Required.
- **phone_number**: IntField
    - The phone number of the customer.
    - Constraints: Required.
- **addresses**: ListField of EmbeddedDocumentField
    - Addresses associated with the customer.

### CustomerCoupon

A document representing the association between a customer and a coupon.

- **coupon**: ReferenceField
    - Reference to a coupon document.
    - Constraints: Required, CASCADE delete.
- **customer**: ReferenceField
    - Reference to a customer document.
    - Constraints: Required, CASCADE delete.

### CustomerAddress

An embedded document representing a customer address.

- **lat**: FloatField
    - Latitude coordinate.
    - Constraints: Required.
- **lng**: FloatField
    - Longitude coordinate.
    - Constraints: Required.
- **text**: StringField
    - Textual description of the address.
    - Constraints: Required.

### CustomerAddressHistory

A document representing a customer's address history.

- **lat**: FloatField
    - Latitude coordinate.
    - Constraints: Required.
- **lng**: FloatField
    - Longitude coordinate.
    - Constraints: Required.
- **customer_address**: ReferenceField
    - Reference to a customer address.
    - Constraints: Required, CASCADE delete.

### ProductDetail

A document representing product details.

- **name**: StringField
    - The name of the product.
    - Constraints: Required.
- **image_urls**: StringField
    - URLs to images for the product.
    - Constraints: Required.

### LibraryProduct

A document representing a library product.

- **sp**: IntField
    - Selling price.
    - Constraints: Required.
- **mrp**: IntField
    - Maximum Retail Price.
    - Constraints: Required.
- **detail**: ReferenceField
    - Reference to product details.
- **price_change_logs**: ListField of EmbeddedDocumentField
    - Logs of price changes.
- **parent_product**: ReferenceField
    - Reference to a parent product.
    - Constraints: CASCADE delete.

### LibraryProductPriceChangeLog

An embedded document representing a library product price change log.

- **sp**: IntField
    - Selling price.
    - Constraints: Required.
- **mrp**: IntField
    - Maximum Retail Price.
    - Constraints: Required.

### StoreProductPriceChangeLog

An embedded document representing a store product price change log.

- **sp**: IntField
    - Selling price.
    - Constraints: Required.
- **mrp**: IntField
    - Maximum Retail Price.
    - Constraints: Required.

### StoreProduct

A document representing a store product.

- **mrp**: IntField
    - Maximum Retail Price.
    - Constraints: Required.
- **sp**: IntField
    - Selling price.
    - Constraints: Required.
- **in_stock**: IntField
    - Quantity in stock.
    - Constraints: Required.
- **detail**: ReferenceField
    - Reference to product details.
- **price_change_logs**: ListField of EmbeddedDocumentField
    - Logs of price changes.
- **store**: ReferenceField
    - Reference to a store.
    - Constraints: CASCADE delete, Default: None.

### OrderSession

A document representing an order session.

- **applied_coupon**: ReferenceField
    - Reference to an applied coupon.
    - Constraints: CASCADE delete, Default: None.

### Order

A document representing an order.

- **customer**: ReferenceField
    - Reference to a customer.
    - Constraints
    - Required, CASCADE delete.
- **customer_location**: EmbeddedDocumentField
    - Embedded customer address.
- **applied_coupon**: ReferenceField
    - Reference to an applied coupon.
    - Constraints: CASCADE delete, Default: None.
- **store**: ReferenceField
    - Reference to a store.
    - Constraints: Required, CASCADE delete.
- **state**: IntField
    - State of the order.
    - Constraints: Required, Default: 1.
- **coupon_discount_amount**: IntField
    - Amount of discount from the applied coupon.
    - Default: None.
- **product_total**: IntField
    - Total amount for products.
    - Default: None.
- **version**: IntField
    - Version of the order.
    - Constraints: Required, Default: 1.
- **products**: ListField of EmbeddedDocumentField
    - Products in the order.

### OrderProduct

An embedded document representing a product in an order.

- **is_active**: BooleanField
    - Indicates if the product is active.
    - Constraints: Required, Default: True.
- **store_product_price_log**: EmbeddedDocumentField
    - Embedded log of store product price change.
- **quantity**: IntField
    - Quantity of the product.
    - Constraints: Required, Default: 1.
- **version**: IntField
    - Version of the product.
    - Constraints: Required, Default: 1.
