-- migrate:up

CREATE TABLE objectives (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(10)
);

-- migrate:down

DROP TABLE IF EXISTS objectives;
