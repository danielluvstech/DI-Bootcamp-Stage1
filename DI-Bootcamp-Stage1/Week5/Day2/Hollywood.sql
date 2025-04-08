-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";
-- CREATE DATABASE "Hollywood"
--    WITH
--    OWNER = postgres
--    ENCODING = 'UTF8'
--    LC_COLLATE = 'en-US'
--    LC_CTYPE = 'en-US'
--    LOCALE_PROVIDER = 'libc'
--    TABLESPACE = pg_default
--    CONNECTION LIMIT = -1
--    IS_TEMPLATE = False;

/*CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);*/

-- SELECT * FROM actors order by actor_id;

-- SELECT * FROM actors WHERE first_name != 'Matt';

/*
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5),
      ('George','Clooney','06/05/1961', 2),
	  ('Gal','Gadot','01/01/1985', 1),
	  ('Bruce','Springsteen','06/08/1971', 3),
	  ('Jennifer','Aniston','07/07/1973', 2);
	  */

SELECT * FROM actors	

/*SELECT * FROM actors LIMIT 4;
SELECT * FROM actors ORDER BY last_name DESC LIMIT 4;
SELECT * FROM actors WHERE first_name LIKE '%e%';
SELECT * FROM actors WHERE number_oscars >= 5;*/

UPDATE actors 
SET age = '1971-02-02'
WHERE actor_id = 1
	

	

