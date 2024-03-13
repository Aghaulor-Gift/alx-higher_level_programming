-- This script lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database.
-- Get the genre IDs linked to Dexter
SELECT genre_id
FROM tv_show_genres
WHERE show_id = (
    SELECT id
    FROM tv_shows
    WHERE title = 'Dexter'
);

-- Get all genres not linked to Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
ORDER BY name ASC;






