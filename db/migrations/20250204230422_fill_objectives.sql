-- migrate:up

INSERT INTO objectives (id, name) VALUES
(1, 'FUERZA'),
(2, 'RESISTENCIA'),
(3, 'HIPERTROFIA'),
(4, 'PÉRDIDA PESO'),
(5, 'FLEXIBILIDAD'),
(6, 'SALUD GENERAL'),
(7, 'REHABILITACIÓN');

-- migrate:down

DELETE FROM objectives;