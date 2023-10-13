CREATE TABLE IF NOT EXISTS customer(
    cust_id SERIAL PRIMARY KEY,
    cust_full_name VARCHAR(250),
    cust_address VARCHAR (150),
    billing_info VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS car_inventory(
    serial_number SERIAL PRIMARY KEY,
    car_make VARCHAR (155),
    car_model VARCHAR (155),
    car_year INTEGER,
    amount NUMERIC (8,2),
);

CREATE TABLE IF NOT EXISTS service_team(
    service_id SERIAL PRIMARY KEY,
    invoice_id INTEGER,
    service_team_name VARCHAR(30),
);

CREATE TABLE IF NOT EXISTS service_dept(
    service_perf SERIAL PRIMARY KEY,
    invoice_id INTEGER,
    service_date DATE,
    serial_number VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS parts(
    part_no SERIAL PRIMARY KEY,
    invoice_id INTEGER,
    service_date DATE,
    amount NUMERIC(8,2)
);

CREATE TABLE IF NOT EXISTS invoice(
    invoice_id SERIAL PRIMARY KEY,
    item_desc VARCHAR(155),
    part_no INTEGER,
    amount NUMERIC (8,2),
    cust_id INTEGER,
    cust_full_name VARCHAR(250),
    service_id INTEGER,
    cust_address VARCHAR (250),
    billing_info NUMERIC(8,2),
    serial_number VARCHAR(25),
    service_date DATE
);

CREATE TABLE IF NOT EXISTS salesperson(
    seller_id SERIAL PRIMARY KEY,
    seller_name VARCHAR (250),
    serial_number VARCHAR(25)
);

CREATE TABLE IF EXISTS bill_of_sale(
    serial_number PRIMARY KEY INTEGER,
    car_make VARCHAR(155),
    car_model VARCHAR (155),
    car_year INTEGER,
    amount NUMERIC (8,2),
    cust_full_name VARCHAR(250),
    seller_id INTEGER
    cust_address VARCHAR(250),
    billing_info NUMERIC(16),
    serial_number VARCHAR(25),
    seller_id NUMERIC,
    seller_name VARCHAR(250)
);