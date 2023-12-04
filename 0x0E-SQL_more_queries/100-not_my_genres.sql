-- Script lists all genres not linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
NATURAL JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
