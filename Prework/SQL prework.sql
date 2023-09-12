CREATE TABLE named_customers (
cust_id int,
cust_name varchar(255),
address varchar(255));

INSERT INTO named_customers (cust_id, cust_name, address) VALUES (1,"John", "123  ABC ST");
INSERT INTO named_customers (cust_id, cust_name, address) VALUES (2,"Mary", "124  ABC ST");
INSERT INTO named_customers (cust_id, cust_name, address) VALUES (3,"Bill", "125  ABC ST")

SELECT * FROM named_customers