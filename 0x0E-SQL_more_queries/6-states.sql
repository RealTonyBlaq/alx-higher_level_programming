-- script creates a new database, a new table with:
-- id: an integer having unique, non-null auto-generated values and is a
-- primary key. name: a varchar which can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL
);
