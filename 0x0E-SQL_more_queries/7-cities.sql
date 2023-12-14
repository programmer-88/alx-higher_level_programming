-- This script creates a database hbtn_0d_usa and the table cities
    -- id INT aoutegenerated, can't be null and is a priary key
    -- state_id INT cannot be null and is foring key refrence to id of states table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT, PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
    name VARCHAR(256) NOT NULL
);
