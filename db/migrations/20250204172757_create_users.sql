-- migrate:up

CREATE TABLE users (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  user_name	VARCHAR(20),
  password	VARCHAR(250),
  member_id	INTEGER,
  FOREIGN KEY (member_id) REFERENCES members (id)
);

-- migrate:down

DROP TABLE IF EXISTS users;
