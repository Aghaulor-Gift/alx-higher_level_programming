-- Script that lists all the cities of California registered in the database
-- Query to list all cities of California

SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California"
	)
ORDER BY id ASC;
