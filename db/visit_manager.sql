DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    continent VARCHAR(255)
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    city_id SERIAL NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    country_id SERIAL NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN,
    review TEXT
);