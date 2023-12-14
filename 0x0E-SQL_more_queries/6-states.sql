-- create the database hbtn_0d_usa and table states
    -- id INT unique, primary key and auto generated
    -- name VARCHAR(255)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE  TABLE IF NOT EXISTS hbtn_0d_usa(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
