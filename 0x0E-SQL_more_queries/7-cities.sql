-- script creates a database (if it doesn't exist) and
-- a table "states" with a "state_id" having a foreign key
-- that references the primary key in another table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
    state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
