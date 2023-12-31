-- Script lists all genres not linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
	SELECT tv_show_genres.genre_id AS id
	FROM tv_show_genres
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter'
) AS new_table
ON tv_genres.id = new_table.id
WHERE new_table.id IS NULL
ORDER BY tv_genres.name ASC;
