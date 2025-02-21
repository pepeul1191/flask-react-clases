-- migrate:up

CREATE TABLE members (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40),
  codigo	VARCHAR(5),
  dni	VARCHAR(8),
  email	VARCHAR(40),
  phone	VARCHAR(40)
);

-- migrate:down

DROP TABLE IF EXISTS members;
