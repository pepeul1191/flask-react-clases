-- migrate:up

CREATE TABLE routines (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  created DATE,
  endend DATE,
  medical_obs BOOLEAN,
  warm_ups INTEGER,
  level_id	INTEGER,
  objective_id	INTEGER,
  member_id	INTEGER,
  FOREIGN KEY (level_id) REFERENCES levels (id),
  FOREIGN KEY (objective_id) REFERENCES lbjectivels (id),
  FOREIGN KEY (member_id) REFERENCES members (id)
);
-- migrate:down


DROP TABLE IF EXISTS routines;
