-- migrate:up

CREATE TABLE body_parts (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(10)
);

-- migrate:down

DROP TABLE IF EXISTS body_parts;
