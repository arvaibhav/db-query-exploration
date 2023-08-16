## ContentType (Table Name: django_content_type)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | AutoField | Primary Key, Unique, Not Null |  | No |
| app_label | CharField | Not Null |  | No |
| model | CharField | Not Null |  | No |


## Category (Table Name: __main___category)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| created_on | DateTimeField | Not Null |  | No |
| name | CharField | Not Null |  | No |
| category_code | CharField | Primary Key, Unique, Not Null |  | No |
| parent | ForeignKey |  | SET NULL | Yes |


## Coupon (Table Name: __main___coupon)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| coupon_code | CharField | Not Null |  | No |
| campaign_type | SmallIntegerField | Not Null |  | No |
| discount_type | SmallIntegerField | Not Null |  | No |
| discount_value | SmallIntegerField | Not Null |  | No |
| min_order_value | SmallIntegerField | Not Null |  | No |
| max_discount | SmallIntegerField | Not Null |  | No |


## Store (Table Name: __main___store)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| name | CharField | Not Null |  | No |
| phone_number | BigIntegerField | Not Null |  | No |
| lat | FloatField | Not Null |  | No |
| lng | FloatField | Not Null |  | No |


## StoreCoupon (Table Name: __main___storecoupon)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| coupon | ForeignKey | Not Null | CASCADE | Yes |
| store | ForeignKey | Not Null | CASCADE | Yes |


## Customer (Table Name: __main___customer)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| name | CharField | Not Null |  | No |
| phone_number | BigIntegerField | Not Null |  | No |


## CustomerCoupon (Table Name: __main___customercoupon)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| coupon | ForeignKey | Not Null | CASCADE | Yes |
| customer | ForeignKey | Not Null | CASCADE | Yes |


## CustomerAddress (Table Name: __main___customeraddress)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| lat | FloatField | Not Null |  | No |
| lng | FloatField | Not Null |  | No |
| text | TextField | Not Null |  | No |
| customer | ForeignKey | Not Null | CASCADE | Yes |


## CustomerAddressHistory (Table Name: __main___customeraddresshistory)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| lat | FloatField | Not Null |  | No |
| lng | FloatField | Not Null |  | No |
| customer_address | ForeignKey | Not Null | CASCADE | Yes |


## ProductDetail (Table Name: __main___productdetail)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| name | CharField | Not Null |  | No |
| image_urls | TextField | Not Null |  | No |


## LibraryProduct (Table Name: __main___libraryproduct)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| sp | SmallIntegerField | Not Null |  | No |
| mrp | SmallIntegerField | Not Null |  | No |
| detail | OneToOneField | Unique, Not Null | CASCADE | Yes |
| parent_product | ForeignKey |  | SET NULL | Yes |


## LibraryProductPriceChangeLog (Table Name: __main___libraryproductpricechangelog)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| sp | SmallIntegerField | Not Null |  | No |
| mrp | SmallIntegerField | Not Null |  | No |
| library_product | ForeignKey | Not Null | CASCADE | Yes |


## StoreProductPriceChangeLog (Table Name: __main___storeproductpricechangelog)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| sp | SmallIntegerField | Not Null |  | No |
| mrp | SmallIntegerField | Not Null |  | No |
| store_product | ForeignKey | Not Null | CASCADE | Yes |


## StoreProduct (Table Name: __main___storeproduct)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| mrp | SmallIntegerField | Not Null |  | No |
| sp | SmallIntegerField | Not Null |  | No |
| in_stock | SmallIntegerField | Not Null |  | No |
| detail | ForeignKey | Not Null | CASCADE | Yes |
| store | ForeignKey | Default: None | CASCADE | Yes |


## OrderSession (Table Name: __main___ordersession)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| applied_coupon | ForeignKey | Default: None | CASCADE | Yes |
| created_on | DateTimeField | Not Null |  | No |


## Order (Table Name: __main___order)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| customer | ForeignKey | Not Null | CASCADE | Yes |
| customer_location | ForeignKey | Default: None | CASCADE | Yes |
| order_session | ForeignKey | Default: None | CASCADE | Yes |
| store | ForeignKey | Not Null | CASCADE | Yes |
| state | SmallIntegerField | Not Null, Default: 1 |  | No |
| coupon_discount_amount | SmallIntegerField | Default: None |  | No |
| product_total | SmallIntegerField | Default: None |  | No |
| version | SmallIntegerField | Not Null, Default: 1 |  | No |


## OrderProduct (Table Name: __main___orderproduct)
| Field Name | Type | Constraints | On Delete | Index |
|------------|------|-------------|-----------|-------|
| id | BigAutoField | Primary Key, Unique, Not Null |  | No |
| created_on | DateTimeField | Not Null |  | No |
| is_active | BooleanField | Not Null, Default: True |  | No |
| store_product_price_log | ForeignKey | Not Null | CASCADE | Yes |
| order | ForeignKey | Not Null | CASCADE | Yes |
| quantity | SmallIntegerField | Not Null, Default: 1 |  | No |
| version | SmallIntegerField | Not Null, Default: 1 |  | No |


