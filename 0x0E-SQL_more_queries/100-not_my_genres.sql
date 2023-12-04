-- Script lists all genres not linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
INNER JOIN (
	SELECT tv_show_genres.genre_id
	FROM tv_show_genres
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
)
ON tv_genres.genre_id = genre_id
ORDER BY tv_genres.name ASC;

