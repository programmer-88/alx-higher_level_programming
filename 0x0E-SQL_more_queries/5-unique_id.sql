-- This script creates a table unique_id
    -- id INT default 1 must be unique
    -- name VARCHAR(256)
    -- if table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id(
    id INT default 1,
    name VARCHAR(256)
);
