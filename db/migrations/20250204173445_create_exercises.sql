-- migrate:up

CREATE TABLE exercises (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40),
  image_url	VARCHAR(40),
  body_part_id	INTEGER,
  FOREIGN KEY (body_part_id) REFERENCES body_parts (id)
);

-- migrate:down

DROP TABLE IF EXISTS exercises;
