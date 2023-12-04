SELECT tv_show_genres.show_id AS id
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
