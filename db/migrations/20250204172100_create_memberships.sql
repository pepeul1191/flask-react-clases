-- migrate:up

CREATE TABLE memberships (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  begining	DATE,
  ending	DATE,
  member_id	INTEGER,
  FOREIGN KEY (member_id) REFERENCES members (id)
);

-- migrate:down

DROP TABLE IF EXISTS memberships;
