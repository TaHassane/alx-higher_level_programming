-- Database Creation:
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; -- This query ensures the creation of the database 'hbtn_0d_usa' if it doesn't already exist.
-- Switch to the 'hbtn_0d_usa' database:
USE hbtn_0d_usa;
-- Table Creation:
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities ( -- This query creates the table 'cities' within the 'hbtn_0d_usa' database if it doesn't already exist.
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE, -- Each entry in the 'cities' table will have a unique 'id' assigned automatically.
state_id INT NOT NULL, -- 'state_id' column stores the ID of the state to which the city belongs and cannot be null.
name VARCHAR(256) NOT NULL, -- The 'name' column in the 'cities' table will store names of cities and cannot be null.
FOREIGN KEY (state_id) REFERENCES states(id)); -- This defines a foreign key constraint, ensuring that the 'state_id' column references the 'id' column in the 'states' table.
