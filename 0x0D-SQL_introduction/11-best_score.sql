-- Lists values from second_table and sorts in DESC order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
