-- Below is a script to list all the cities of California registered in the database:
SELECT id, name -- This query selects the 'id' and 'name' columns from the 'cities' table.
FROM cities -- We're selecting data from the 'cities' table.
WHERE state_id = ( -- This subquery retrieves the ID of California from the 'states' table.
SELECT id
FROM states
WHERE name = "California"); -- We're finding the state with the name "California" to get its ID.
