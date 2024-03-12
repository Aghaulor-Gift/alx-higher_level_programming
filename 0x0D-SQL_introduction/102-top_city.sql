-- Script: 102-top_city.sql
-- Description: Displays the top 3 cities' temperatures during July and August ordered by temperature (descending)

SELECT city, temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
