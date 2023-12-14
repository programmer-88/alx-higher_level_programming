-- This script lists all the cities of california
    -- results must be sorted in ascending order

SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'Carlifonia'
)
ORDER BY id;
