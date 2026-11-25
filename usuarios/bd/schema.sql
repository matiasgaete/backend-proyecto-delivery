CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    rut VARCHAR(12) UNIQUE NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    pass_user VARCHAR(255) NOT NULL,
    reset_token_hash VARCHAR(64),
    reset_token_expires_at TIMESTAMPTZ,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE usuarios
    ADD COLUMN IF NOT EXISTS reset_token_hash VARCHAR(64),
    ADD COLUMN IF NOT EXISTS reset_token_expires_at TIMESTAMPTZ;