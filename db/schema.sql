CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE body_parts (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(10)
);
CREATE TABLE members (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40),
  codigo	VARCHAR(5),
  dni	VARCHAR(8),
  email	VARCHAR(40),
  phone	VARCHAR(40)
);
CREATE TABLE levels (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(20)
);
CREATE TABLE objectives (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(10)
);
CREATE TABLE memberships (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  begining	DATE,
  ending	DATE,
  member_id	INTEGER,
  FOREIGN KEY (member_id) REFERENCES members (id)
);
CREATE TABLE users (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  user_name	VARCHAR(20),
  password	VARCHAR(250),
  member_id	INTEGER,
  FOREIGN KEY (member_id) REFERENCES members (id)
);
CREATE TABLE exercises (
  id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name	VARCHAR(40),
  image_url	VARCHAR(40),
  body_part_id	INTEGER,
  FOREIGN KEY (body_part_id) REFERENCES body_parts (id)
);
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
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20250204165849'),
  ('20250204170648'),
  ('20250204171606'),
  ('20250204171728'),
  ('20250204172100'),
  ('20250204172757'),
  ('20250204173445'),
  ('20250204173505'),
  ('20250204173510'),
  ('20250204180337'),
  ('20250204225118'),
  ('20250204225855'),
  ('20250204230422'),
  ('20250204232115'),
  ('20250204232628');
