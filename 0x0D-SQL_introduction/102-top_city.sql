-- script lists the top 3 cities ordered by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
WHERE month IS BETWEEN 7 AND 8
ORDER BY avg_temp DESC
LIMIT 3;
