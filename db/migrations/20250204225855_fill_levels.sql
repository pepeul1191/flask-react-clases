-- migrate:up

INSERT INTO levels (id, name) VALUES
(1, 'PRINCIPIANTE'),
(2, 'BÁSICO'),
(3, 'INTERMEDIO'),
(4, 'AVANZADO'),
(5, 'EXPERTO'),
(6, 'CARDIO INTENSO'),
(7, 'FUERZA Y RESISTENCIA'),
(8, 'HIPERTROFIA'),
(9, 'PÉRDIDA DE PESO'),
(10, 'ATLETA ÉLITE');


-- migrate:down

DELETE FROM levels;