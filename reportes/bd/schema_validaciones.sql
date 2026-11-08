CREATE TABLE validaciones (
    id SERIAL PRIMARY KEY,
    valido BOOLEAN NOT NULL,
    id_reporte INT NOT NULL,
    CONSTRAINT fk_validaciones_reportes_locales 
        FOREIGN KEY (id_reporte) 
        REFERENCES reportes_locales (id) 
        ON DELETE CASCADE
);