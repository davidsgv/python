DROP DATABASE IF EXISTS tienda;
CREATE DATABASE tienda;
USE tienda;

CREATE TABLE productos(
	id int unsigned auto_increment PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    imagen VARCHAR(1000) NOT NULL,
    precio DECIMAL(4,2) NOT NULL
);