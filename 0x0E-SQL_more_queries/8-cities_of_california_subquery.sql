-- This script lists all the cities of california
    -- results must be sorted in ascending order

SELECT cities.name AS city_name
FROM cities
WHERE cities.state_id = (
    SELECT states.id
    FROM states
    WHERE name = 'Carlifonia'
)
ORDER BY cities.name ASC;
