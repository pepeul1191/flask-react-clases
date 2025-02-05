-- migrate:up

INSERT INTO body_parts (id, name) VALUES (1, 'PECHO');
INSERT INTO body_parts (id, name) VALUES (2, 'ESPALDA');
INSERT INTO body_parts (id, name) VALUES (3, 'PIERNAS');
INSERT INTO body_parts (id, name) VALUES (4, 'BRAZOS');
INSERT INTO body_parts (id, name) VALUES (5, 'HOMBROS');
INSERT INTO body_parts (id, name) VALUES (6, 'ABDOMEN');

-- migrate:down

DELETE FROM body_parts;