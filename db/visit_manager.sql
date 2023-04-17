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
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN,
    review TEXT
);