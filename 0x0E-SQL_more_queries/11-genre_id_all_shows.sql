-- Script that lists all cities contained in the database
-- Query to list all shows with their corresponding genre IDs
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;