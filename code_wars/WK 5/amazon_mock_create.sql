CREATE TABLE IF NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    address VARCHAR (150),
    billing_info VARCHAR(100)
);

-- Brand TABLE Creation
CREATE TABLE IF NOT EXISTS brand(
    seller_id SERIAL PRIMARY KEY,
    brand_name VARCHAR (150),
    contact_number VARCHAR(15),
    address VARCHAR(150)
);

-- INVENTORY Table Creation
CREATE TABLE IF NOT EXISTS invnetory(
    upc SERIAL PRIMARY KEY,
    product_number INTEGER
);

-- Product TAble 
CREATE TABLE IF NOT EXISTS product(
    item_id SERIAL PRIMARY KEY,
    amount NUMERIC (5,2),
    prod_name VARCHAR(100),
    upc INTEGER NOT NULL,
    FOREIGN KEY(seller_id) REFERENCES brand(seller_id)
    FOREIGN Key (upc) REFERENCES invnetory(upc)  
);

-- Orders Table
CREATE TABLE IF NOT EXISTS orders(
    order_id SERIAL PRIMARY Key,
    order_date DATE DEFAULT CURRENT_DATE,
    sub_total NUMERIC (8,2),
    total_cost NUMERIC (8,2),
    upc INTEGER NOT NULL,
    FOREIGN KEY(upc) REFERENCES invnetory(upc)

);

--Cart Table
CREATE TABLE IF NOT EXISTS cart(
    cart_id SERIAL PRIMARY Key,
    customer_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    FOREIGN Key (customer_id) REFERENCES customer(customer_id),
    FOREIGN Key (order_id) REFERENCES orders(order_id)
);