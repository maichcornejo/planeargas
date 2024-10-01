CREATE TABLE artefactos_unicos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) UNIQUE,
    tipo VARCHAR(255),
    orientacion VARCHAR(255)
);

CREATE TABLE planos (
    id SERIAL PRIMARY KEY,
    nombre_plano VARCHAR(255) UNIQUE
);

CREATE TABLE posiciones_artefactos (
    id SERIAL PRIMARY KEY,
    artefacto_id INT REFERENCES artefactos_unicos(id),
    plano_id INT REFERENCES planos(id),
    coordenada_x FLOAT,
    coordenada_y FLOAT
);
