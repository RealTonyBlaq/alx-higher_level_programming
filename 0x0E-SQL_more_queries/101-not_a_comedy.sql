-- Script lists all shows without the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
	SELECT tv_show_genres.show_id AS id
	FROM tv_show_genres
	INNER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name != 'Comedy'
) AS new_table
ON tv_shows.id = new_table.id
ORDER BY tv_shows.title ASC;
