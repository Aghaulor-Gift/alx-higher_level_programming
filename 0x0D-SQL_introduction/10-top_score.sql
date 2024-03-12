-- Script: 10-top_score.sql
-- Description: Lists all records of the table second_table ordered by score

SELECT score, name
FROM second_table
ORDER BY score DESC;
