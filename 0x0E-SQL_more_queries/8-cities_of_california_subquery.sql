-- script lists all the cities in California contained in tables
SELECT *
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = "California"
)
ORDER BY id ASC;
