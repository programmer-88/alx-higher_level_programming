-- This script creates the table id_not_null
    -- id INT with default value of 1
    -- name  VARCHAR(256)
    --  if table exists , script should not fail

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT NOT NULL,
    name VARCHAR(256)
);
