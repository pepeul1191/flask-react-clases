-- migrate:up

INSERT INTO exercises (id, name, image_url, body_part_id) VALUES
(1, 'PRESS BANCA', 'press_banca.jpg', 1),
(2, 'APERTURAS', 'aperturas.jpg', 1),
(3, 'PULL OVER', 'pull_over.jpg', 1),
(4, 'DOMINADAS', 'dominadas.jpg', 2),
(5, 'REMO CON BARRA', 'remo_barra.jpg', 2),
(6, 'PESO MUERTO', 'peso_muerto.jpg', 2),
(7, 'SENTADILLAS', 'sentadillas.jpg', 3),
(8, 'PRENSA', 'prensa.jpg', 3),
(9, 'EXTENSION CUADRICEPS', 'extension_cuadriceps.jpg', 3),
(10, 'CURL BICEPS', 'curl_biceps.jpg', 4),
(11, 'FONDOS TRICEPS', 'fondos_triceps.jpg', 4),
(12, 'PRESS MILITAR', 'press_militar.jpg', 5),
(13, 'ELEVACIONES LATERALES', 'elevaciones_laterales.jpg', 5),
(14, 'PLANCHA', 'plancha.jpg', 6),
(15, 'ABDOMINALES CRUNCH', 'abdominales_crunch.jpg', 6),
(16, 'HIP THRUST', 'hip_thrust.jpg', 3),
(17, 'ZANCADAS', 'zancadas.jpg', 3),
(18, 'FACE PULL', 'face_pull.jpg', 5),
(19, 'PRESS FRANCES', 'press_frances.jpg', 4),
(20, 'PULL UPS', 'pull_ups.jpg', 2),
(21, 'DIPS', 'dips.jpg', 4),
(22, 'ELEVACION PIERNAS', 'elevacion_piernas.jpg', 6),
(23, 'GIROS RUSOS', 'giros_rusos.jpg', 6),
(24, 'BURPEES', 'burpees.jpg', 6),
(25, 'SALTO CAJA', 'salto_caja.jpg', 3),
(26, 'CURL MARTILLO', 'curl_martillo.jpg', 4),
(27, 'FLEXIONES', 'flexiones.jpg', 1),
(28, 'REMO CON MANCUERNA', 'remo_mancuerna.jpg', 2),
(29, 'PRESS ARNOLD', 'press_arnold.jpg', 5),
(30, 'ELEVACIONES FRONTALES', 'elevaciones_frontales.jpg', 5);

-- migrate:down

DELETE FROM exercises;