CREATE EXTENSION IF NOT EXISTS postgis;

-- 2. Eliminar la tabla si ya existe para empezar limpio
DROP TABLE IF EXISTS reportes_locales;

-- 3. Crear la tabla reportes_locales desde cero
CREATE TABLE reportes_locales (
    id SERIAL PRIMARY KEY,
    nombre_local VARCHAR(255) NOT NULL,
    direccion TEXT NOT NULL,
    ubicacion GEOGRAPHY(Point, 4326) NOT NULL,
    titulo_reporte VARCHAR(255) NOT NULL,
    descripcion_reporte TEXT,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_titulo_reporte CHECK (titulo_reporte IN ('Local nuevo', 'Local cerrado', 'Local ya no existe'))
);

CREATE INDEX idx_reportes_locales_ubicacion ON reportes_locales USING GIST (ubicacion);