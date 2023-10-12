INSERT INTO customer(
    customer_id,
    first_name,
    last_name,
    address,
    billing_info
);

VALUES(
    1,
    'Andrew',
    'Peterson',
    '5094 N Grey Hawk Dr',
    'VISA ENDING IN 1491'
);
VALUES(
    2,
    'Kayla',
    'Haliczer',
    '520 W Lowell',
    'Master ENDING IN 1234'
);

INSERT INTO concessions(
    cart_id,
    item_name,
    item_qty,
    item_price,
    sub_total,
    total,
    upc,
    billing_info
);
VALUES(
    32,
    'Twix',
    2,
    1.99,
    3.98,
    5.00
    123456789,
    'Master ENDING IN 1234'
);
VALUES(
    12,
    'LG Pop-corn',
    2
    2.50,
    5.00,
    6.08,
    'VISA ENDING IN 1491'
);

INSERT INTO tickets(
    ticket,
    customer_id,
    ticket_price,
    ticket_qty,
    ticket_type,
    film_id,
    cart_id
);
VALUES(
    1,
    1,
    5.00,
    1,
    'Adult',
    59,
    32
);
VALUES(
    2,
    2,
    10.00,
    'Adult',
    12,
    12
);

INSERT INTO movie(
    film_id,
    film_name,
    release_year
);
VALUES(
    59,
    'Dazed and Confused',
    1993
);
VALUES(
    32,
    'Dune',
    2021
);

INSERT INTO cart(
    customer_id,
    cart_id,
    total_items,
    sub_total,
    total
);
VALUES(
    1,
    32,
    3,
    10.00,
    12.50
);
VALUES(
    2,
    12,
    4,
    15.00,
    17.38
);


