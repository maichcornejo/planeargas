INSERT INTO artefactos (nombre, tipo, orientacion, imagen, dimensiones)
VALUES 
('Calefactor Tiro Balanceado Lateral', 'Calefactor', 'Norte', pg_read_binary_file('/ruta/a/imagen_norte.png'), '{"ancho": 60, "alto": 40}'),
('Calefactor Tiro Balanceado Lateral', 'Calefactor', 'Sur', pg_read_binary_file('/ruta/a/imagen_sur.png'), '{"ancho": 60, "alto": 40}'),
('Calefactor Tiro Balanceado Lateral', 'Calefactor', 'Este', pg_read_binary_file('/ruta/a/imagen_este.png'), '{"ancho": 60, "alto": 40}'),
('Calefactor Tiro Balanceado Lateral', 'Calefactor', 'Oeste', pg_read_binary_file('/ruta/a/imagen_oeste.png'), '{"ancho": 60, "alto": 40}');
