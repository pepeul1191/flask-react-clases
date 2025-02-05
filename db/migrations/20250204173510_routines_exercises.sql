-- migrate:up

CREATE TABLE routines_exercies (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  body_part_id	INTEGER,
  routine_id	INTEGER,
  exercise_id INTEGER,
  exercise_order INTEGER,
  steps INTEGER,
  reps INTEGER,
  FOREIGN KEY (routine_id) REFERENCES routines(id),
  FOREIGN KEY (body_part_id) REFERENCES body_parts(id)
);

-- migrate:down

DROP TABLE IF EXISTS routines_exercies;
