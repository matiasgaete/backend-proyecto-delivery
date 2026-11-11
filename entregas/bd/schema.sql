CREATE TABLE entregas (
    id SERIAL PRIMARY KEY,
    hora_aceptacion TIMESTAMPTZ NOT NULL,
    hora_recogida TIMESTAMPTZ NOT NULL,
    hora_entrega TIMESTAMPTZ NOT NULL,
    monto INT NOT NULL,
    id_local INT NOT NULL,
    app VARCHAR(50) NOT NULL,

    CONSTRAINT chk_app CHECK (
        app IN ('Uber Eats', 'PedidosYa', 'Rappi')
    ),

    CONSTRAINT chk_secuencia_horas CHECK (
        (hora_recogida IS NULL OR hora_aceptacion <= hora_recogida) AND
        (hora_entrega IS NULL OR (hora_recogida IS NOT NULL AND hora_recogida <= hora_entrega))
    ),

    CONSTRAINT chk_monto CHECK (monto > 0)
);