CREATE TABLE IF NOT EXISTS bank(
customer_id INT NOT NULL,
account_number INT NOT NULL,
balance NUMERIC (10,2),
age INT,
CONSTRAINT above_zero CHECK(balance >=0),
CONSTRAINT pri_key_bank PRIMARY KEY (customer_id, account_number)
);
SELECT * 
FROM bank;

INSERT INTO bank
VALUES (,,,,'Randall', 'THOMAS');

ALTER TABLE bank
ADD first_name VARCHAR(255);

ALTER TABLE bank
ADD last_name VARCHAR(255);

INSERT INTO bank
VALUES(2,2,5000,25,'JAMES', 'STRATTON');

ALTER TABLE bank
DROP CHECK above_zero;

ALTER TABLE bank
MODIFY COLUMN last_name VARCHAR(255) AFTER first_name;

SELECT * 
FROM bank;

UPDATE bank
SET balance = 10000000.00
WHERE age = 25;

CREATE VIEW high_rollers AS
SELECT customer_id, CONCAT(first_name," ",last_name) as full_name, balance
FROM bank
WHERE balance > 100000;

SELECT *
FROM high_rollers;