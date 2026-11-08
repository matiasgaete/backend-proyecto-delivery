DO $$
DECLARE
    i INT;
    nombres TEXT[] := ARRAY[
        'Panadería El Sol', 'Botillería Don Pedro', 'Café Central', 'Farmacia La Fe', 
        'Bar Italia', 'Supermercado Cordillera', 'Restaurant El Arriero', 'Pizzería Napolitana', 
        'Verdulería Don Pepe', 'Librería Providencia', 'Ferretería El Candado', 'Boutique Bellavista'
    ];
    calles TEXT[] := ARRAY[
        'Av. Libertador Bernardo O''Higgins', 'Av. Providencia', 'Av. Apoquindo', 
        'Av. Vicuña Mackenna', 'Av. Irarrázaval', 'Gran Avenida José Miguel Carrera', 
        'Av. Matta', 'Av. Recoleta', 'Av. Independencia', 'Av. Brasil', 'Av. Concha y Toro'
    ];
    comunas TEXT[] := ARRAY[
        'Santiago', 'Providencia', 'Las Condes', 'Ñuñoa', 
        'La Florida', 'San Miguel', 'Recoleta', 'Maipú', 'Puente Alto'
    ];
    titulos TEXT[] := ARRAY[
        'Local nuevo', 
        'Local cerrado', 
        'Local ya no existe'
    ];
    
    nombre_rand TEXT;
    direccion_rand TEXT;
    titulo_rand TEXT;
    descripcion_rand TEXT;
    lat NUMERIC;
    lon NUMERIC;
    fecha_rand TIMESTAMP;
BEGIN
    FOR i IN 1..5000 LOOP
        -- Selección aleatoria de datos de prueba
        nombre_rand := nombres[1 + floor(random() * array_length(nombres, 1))::int] || ' #' || i;
        direccion_rand := calles[1 + floor(random() * array_length(calles, 1))::int] || ' #' || floor(random() * 8000 + 100)::text || ', ' || comunas[1 + floor(random() * array_length(comunas, 1))::int];
        titulo_rand := titulos[1 + floor(random() * array_length(titulos, 1))::int];
        
        -- Lógica contextual para la descripción según el reporte
        IF titulo_rand = 'Local nuevo' THEN
            descripcion_rand := 'El usuario reporta que en esta ubicación abrió un nuevo establecimiento que no figura en el mapa de la app.';
        ELSIF titulo_rand = 'Local cerrado' THEN
            descripcion_rand := 'El usuario indica que el local existe en el sistema, pero se encuentra cerrado al momento de la visita.';
        ELSE
            descripcion_rand := 'El usuario acudió a las coordenadas registradas por la app, pero el local ya no existe en el sitio.';
        END IF;

        -- Generar coordenadas dentro del rango urbano de Santiago (-33.35 a -33.60 Lat, -70.75 a -70.52 Lon)
        lat := -33.35 - (random() * 0.25);
        lon := -70.75 + (random() * 0.23);
        
        -- Fecha aleatoria comprendida dentro del último año
        fecha_rand := NOW() - (random() * 365 || ' days')::INTERVAL;

        INSERT INTO reportes_locales (
            nombre_local, 
            direccion, 
            ubicacion, 
            titulo_reporte, 
            descripcion_reporte, 
            creado_en
        )
        VALUES (
            nombre_rand,
            direccion_rand,
            ST_SetSRID(ST_MakePoint(lon, lat), 4326)::geography,
            titulo_rand,
            descripcion_rand,
            fecha_rand
        );
    END LOOP;
END $$;