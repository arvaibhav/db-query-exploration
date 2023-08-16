CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(256),
    parent_id INTEGER REFERENCES category(id),
    CHECK (id > 0)
);

CREATE TABLE coupon (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    coupon_code VARCHAR(32),
    campaign_type SMALLINT,
    discount_type SMALLINT,
    discount_value SMALLINT,
    CHECK (id > 0)
);

CREATE TABLE store (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    name VARCHAR(128),
    phone_number INTEGER,
    lat FLOAT,
    lng FLOAT,
    CHECK (id > 0)
);

CREATE TABLE storecoupon (
    id SERIAL PRIMARY KEY,
    coupon_id INTEGER REFERENCES coupon(id) ON DELETE CASCADE,
    store_id INTEGER REFERENCES store(id) ON DELETE CASCADE,
    CHECK (id > 0)
);

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    name VARCHAR(128),
    phone_number INTEGER,
    CHECK (id > 0)
);

CREATE TABLE customercoupon (
    id SERIAL PRIMARY KEY,
    coupon_id INTEGER REFERENCES coupon(id),
    customer_id INTEGER REFERENCES customer(id),
    CHECK (id > 0)
);

CREATE TABLE customeraddress (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    lat FLOAT,
    lng FLOAT,
    text TEXT,
    customer_id INTEGER REFERENCES customer(id),
    CHECK (id > 0)
);

CREATE TABLE customeraddresshistory (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    lat FLOAT,
    lng FLOAT,
    customer_address_id INTEGER REFERENCES customeraddress(id),
    CHECK (id > 0)
);

CREATE TABLE productdetail (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    name VARCHAR(256),
    image_urls TEXT,
    CHECK (id > 0)
);

CREATE TABLE libraryproduct (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    sp SMALLINT CHECK (sp > 0),
    mrp SMALLINT,
    detail_id INTEGER REFERENCES productdetail(id),
    parent_product_id INTEGER REFERENCES libraryproduct(id),
    CHECK (id > 0)
);

CREATE TABLE libraryproductpricechangelog (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    sp SMALLINT CHECK (sp > 0),
    mrp SMALLINT,
    library_product_id INTEGER REFERENCES libraryproduct(id),
    CHECK (id > 0)
);

CREATE TABLE storeproduct (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    mrp SMALLINT,
    sp SMALLINT CHECK (sp > 0),
    in_stock BOOLEAN,
    detail_id INTEGER REFERENCES productdetail(id),
    store_id INTEGER REFERENCES store(id),
    CHECK (id > 0)
);

CREATE TABLE ordersession (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    CHECK (id > 0)
);

CREATE TABLE "order" (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    customer_id INTEGER REFERENCES customer(id),
    customer_location_id INTEGER REFERENCES customeraddresshistory(id),
    order_session_id INTEGER REFERENCES ordersession(id),
    store_id INTEGER REFERENCES store(id),
    CHECK (id > 0)
);

CREATE TABLE orderproduct (
    id SERIAL PRIMARY KEY,
    created_on TIMESTAMP DEFAULT current_timestamp,
    is_active BOOLEAN,
    library_product_price_log_id INTEGER REFERENCES libraryproductpricechangelog(id) ON DELETE CASCADE,
    order_id INTEGER REFERENCES "order"(id) ON DELETE CASCADE,
    CHECK (id > 0)
);