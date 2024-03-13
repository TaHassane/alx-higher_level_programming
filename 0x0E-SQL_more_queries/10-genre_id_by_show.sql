-- Below is a script to list all cities contained in the database:
SELECT tv_shows.title AS show_title, tv_show_genres.genre_id -- This query selects the 'title' of TV shows (aliased as show_title) and the 'genre_id' from the 'tv_shows' table.
FROM tv_shows -- We're selecting data from the 'tv_shows' table.
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id -- We're joining the 'tv_shows' table with the 'tv_show_genres' table based on the 'id' column in 'tv_shows' matching the 'show_id' column in 'tv_show_genres'.
ORDER BY tv_shows.title, tv_show_genres.genre_id; -- The results are ordered by the title of the TV show and the genre ID.
