-- script lists all cities contained in the database hbtn_0d_usa
SELECT id, name, states.name
FROM cities
RIGHT JOIN states
ON states.key = cities.key
ORDER BY cities.id ASC;
