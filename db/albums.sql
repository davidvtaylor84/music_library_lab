DROP TABLE IF EXISTS albums;

    CREATE TABLE albums(
        id SERIAL PRIMARY KEY,
        album_name VARCHAR(255),
        artist VARCHAR(255)
    );

    