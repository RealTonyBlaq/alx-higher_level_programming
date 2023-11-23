-- Script lists all tv shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC
