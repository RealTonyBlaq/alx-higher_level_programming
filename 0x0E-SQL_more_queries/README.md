# SQL - More queries

To import the SQL DUMP into the hbtn_0d_usa database:

```cmd
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

File | Description
--- | ---
`0-privileges.sql` | Shows privileges given to a user (in this case `user_0d_1` and `user_0d_2`)
`1-create-user.sql` | Creates a user and grants all privileges on all databases and tables.
`2-create_read_user.sql` | Creates the database `hbtn_0d_2` and user `user_0d_2` and then grants him `SELECT` privileges on all tables in this database.
`3-force_name.sql` | Creates the table `force_name` with two columns; `id` and `name`.
`4-never_empty.sql` | Creates a table with column `id` default to 1.
`5-unique_id.sql`  | Creates a table with column `id` default to 1 and with only unique values.
`6-states.sql` | Creates the database `hbtn_0d_usa` if it doesn't exist and a table with `id` column which is a primary key, auto-generated and is unique.
`7-cities.sql` | Creates the database `hbtn_0d_usa` if it doesn't exist and a table with: `id` column which is a primary key, auto-generated and is unique, `state_id` column which is a foreign key and references the `id` column from another table.
`8-cities_of_california.sql` | Lists all the cities in California by using the foreign key `state_id`.
`9-cities_by_state.sql` | Lists all cities in the database by joining tables.
`10-genre_id_by_show.sql` | Lists all the tv shows in the database `hbtn_0d_tvshows` with at least one genre linked using the JOIN clause.
`11-genre_id_all_shows.sql` | Lists all tv shows in the database with at least 1 genre linked, shows with no genre are represented using NULL by the LEFT JOIN clause.
`12-no_genres.sql` | Lists tv shows with no genre.
`13-count_shows_by_genre.sql` | Lists tv genres and counts the number of shows associated with each in descending order.
`14-my_genres.sql` | Lists all genres of a particular tv show contained in the database using multiple joins.
`15-comedy_only.sql` | Lists only comdey shows.
`16-shows_by_genre.sql` | Lists all shows with all linking genres.
