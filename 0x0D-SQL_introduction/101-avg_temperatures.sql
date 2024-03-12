-- Script: 18-average_temperature.sql
-- Description: Displays the average temperature (in Fahrenheit) by city ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temperature
FROM temperatures
GROUP BY city
ORDER BY avg_temperature DESC;
