-- Script lists all genres not linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.id = (
	SELECT id
	FROM tv_shows
	WHERE title = 'Dexter'
)
ORDER BY tv_genres.name ASC
