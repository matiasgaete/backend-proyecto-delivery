
-- 2. Crear la única tabla de esta BD (sin FOREIGN KEY hacia users)
CREATE TABLE user_sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    device_id VARCHAR(255) NOT NULL,
    refresh_token TEXT NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),

    -- Mantiene una sola sesión activa por usuario y dispositivo
    CONSTRAINT unique_user_device UNIQUE (user_id, device_id)
);

-- Índice para acelerar la consulta en el endpoint /refresh
CREATE INDEX idx_user_sessions_lookup ON user_sessions (device_id, refresh_token);