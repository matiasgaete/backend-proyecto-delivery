CREATE TABLE entregas (
    id SERIAL PRIMARY KEY,
    hora_aceptacion TIMESTAMPTZ,
    hora_recogida TIMESTAMPTZ,
    hora_entrega TIMESTAMPTZ,
    monto INT NOT NULL,
    id_local INT NOT NULL,
    app VARCHAR(50) NOT NULL
);