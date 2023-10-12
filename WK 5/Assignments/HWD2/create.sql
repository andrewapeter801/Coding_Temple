CREATE TABLE IF NOT EXISTS customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    address VARCHAR (150),
    billing_info VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS concessions(
    cart_id SERIAL PRIMARY KEY,
    item_name VARCHAR (30),
    item_qty INTEGER,
    item_price NUMERIC (8,2),
    sub_total NUMERIC (8,2),
    total NUMERIC (8,2)
    upc INTEGER
    billing_info VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS tickets(
    ticket SERIAL PRIMARY KEY,
    customer_id INTEGER,
    ticket_price NUMERIC(8,2),
    ticket_qty NUMERIC (8,2),
    ticket_type VARCHAR (5),
    film_id INTEGER
    cart_id INTEGER
);

CREATE TABLE IF NOT EXISTS movie(
    film_id SERIAL PRIMARY KEY,
    film_name VARCHAR (150),
    release_year INTEGER
);

CREATE TABLE IF NOT EXISTS cart(
    customer_id SERIAL PRIMARY KEY,
    cart_id INTEGER,
    total_items INTEGER,
    sub_total NUMERIC(8,2)
    total NUMERIC(8,2)
);