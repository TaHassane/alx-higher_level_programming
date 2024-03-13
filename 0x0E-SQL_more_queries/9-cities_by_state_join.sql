-- Below is a script to list all cities contained in the database, along with their respective states:
SELECT cities.id, cities.name AS city_name, states.name AS state_name -- This query selects the 'id' of cities, the 'name' of cities (aliased as city_name), and the 'name' of states (aliased as state_name).
FROM cities -- We're selecting data from the 'cities' table.
JOIN states ON cities.state_id = states.id; -- We're joining the 'cities' table with the 'states' table based on the 'state_id' column in 'cities' matching the 'id' column in 'states'. This allows us to fetch cities along with their respective states.
