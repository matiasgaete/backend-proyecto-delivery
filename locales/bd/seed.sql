INSERT INTO locales (nombre, direccion, ubicacion) VALUES
-- 1. Santiago (Centro)
('McDonald''s Plaza de Armas', 'Plaza de Armas 920', ST_SetSRID(ST_MakePoint(-70.65083333, -33.43750000), 4326)::geography),
('Burger King Ahumada', 'Paseo Ahumada 137', ST_SetSRID(ST_MakePoint(-70.65138889, -33.44027778), 4326)::geography),
('KFC Estado', 'Estado 235', ST_SetSRID(ST_MakePoint(-70.64944444, -33.44083333), 4326)::geography),
('Dominó Huérfanos', 'Huérfanos 1044', ST_SetSRID(ST_MakePoint(-70.65305556, -33.43944444), 4326)::geography),
('Fuente Alemana Alameda', 'Av. Libertador Bernardo O''Higgins 58', ST_SetSRID(ST_MakePoint(-70.63777778, -33.43805556), 4326)::geography),

-- 2. Providencia
('Tarragona Tobalaba', 'Av. Providencia 2653', ST_SetSRID(ST_MakePoint(-70.60305556, -33.41777778), 4326)::geography),
('Pedro, Juan & Diego Patio Bellavista', 'Pío Nono 59', ST_SetSRID(ST_MakePoint(-70.63444444, -33.43444444), 4326)::geography),
('Burger King Providencia', 'Av. Providencia 2140', ST_SetSRID(ST_MakePoint(-70.61250000, -33.42416667), 4326)::geography),
('Doggis Manuel Montt', 'Av. Providencia 1344', ST_SetSRID(ST_MakePoint(-70.62194444, -33.42638889), 4326)::geography),
('Wendy''s Encomenderos', 'Encomenderos 201', ST_SetSRID(ST_MakePoint(-70.60250000, -33.41527778), 4326)::geography),

-- 3. Las Condes
('McDonald''s Parque Arauco', 'Av. Presidente Kennedy 5413', ST_SetSRID(ST_MakePoint(-70.57888889, -33.40138889), 4326)::geography),
('Johnny Rockets Alto Las Condes', 'Av. Presidente Kennedy 9001', ST_SetSRID(ST_MakePoint(-70.54777778, -33.39138889), 4326)::geography),
('Burger King Escuela Militar', 'Av. Apoquindo 4501', ST_SetSRID(ST_MakePoint(-70.58555556, -33.41361111), 4326)::geography),
('Carl''s Jr. Rosario Norte', 'Rosario Norte 555', ST_SetSRID(ST_MakePoint(-70.56944444, -33.40472222), 4326)::geography),
('Little Caesars Los Dominicos', 'Av. Apoquindo 6410', ST_SetSRID(ST_MakePoint(-70.56305556, -33.41027778), 4326)::geography),

-- 4. Vitacura
('McDonald''s Vitacura', 'Av. Vitacura 5450', ST_SetSRID(ST_MakePoint(-70.57638889, -33.38388889), 4326)::geography),
('Shake Shack Casacostanera', 'Nueva Costanera 3900', ST_SetSRID(ST_MakePoint(-70.59861111, -33.39916667), 4326)::geography),
('Burger King Lo Curro', 'Av. Vitacura 7120', ST_SetSRID(ST_MakePoint(-70.55805556, -33.37694444), 4326)::geography),
('Dominó Alonso de Córdova', 'Av. Vitacura 3600', ST_SetSRID(ST_MakePoint(-70.59583333, -33.39444444), 4326)::geography),
('Subway Luis Pasteur', 'Luis Pasteur 6600', ST_SetSRID(ST_MakePoint(-70.56388889, -33.37444444), 4326)::geography),

-- 5. Lo Barnechea
('McDonald''s Portal La Dehesa', 'Av. La Dehesa 1445', ST_SetSRID(ST_MakePoint(-70.51527778, -33.36027778), 4326)::geography),
('Burger King Los Trapenses', 'Av. Los Trapenses 3515', ST_SetSRID(ST_MakePoint(-70.53694444, -33.34861111), 4326)::geography),
('KFC Mall Vivo Los Trapenses', 'Av. Los Trapenses 3200', ST_SetSRID(ST_MakePoint(-70.53750000, -33.35194444), 4326)::geography),
('Doggis El Rodeo', 'Av. El Rodeo 12850', ST_SetSRID(ST_MakePoint(-70.51611111, -33.35388889), 4326)::geography),
('Papa John''s La Dehesa', 'Av. El Tranque 10370', ST_SetSRID(ST_MakePoint(-70.52194444, -33.35027778), 4326)::geography),

-- 6. Ñuñoa
('McDonald''s Irarrázaval', 'Av. Irarrázaval 2782', ST_SetSRID(ST_MakePoint(-70.60694444, -33.45444444), 4326)::geography),
('Burger King Plaza Ñuñoa', 'Av. Irarrázaval 3620', ST_SetSRID(ST_MakePoint(-70.59666667, -33.45305556), 4326)::geography),
('Doggis Portal Ñuñoa', 'Av. José Pedro Alessandri 1166', ST_SetSRID(ST_MakePoint(-70.59777778, -33.46861111), 4326)::geography),
('Pedro, Juan & Diego Plaza Egaña', 'Av. Larraín 5862', ST_SetSRID(ST_MakePoint(-70.57750000, -33.45277778), 4326)::geography),
('Papa John''s Ñuñoa', 'Av. Simón Bolívar 4800', ST_SetSRID(ST_MakePoint(-70.58027778, -33.45055556), 4326)::geography),

-- 7. La Reina
('McDonald''s Príncipe de Gales', 'Av. Príncipe de Gales 6700', ST_SetSRID(ST_MakePoint(-70.56083333, -33.44277778), 4326)::geography),
('Burger King Tobalaba', 'Av. Larraín 5961', ST_SetSRID(ST_MakePoint(-70.57611111, -33.45222222), 4326)::geography),
('KFC Mall Plaza Egaña', 'Av. Larraín 5862', ST_SetSRID(ST_MakePoint(-70.57722222, -33.45250000), 4326)::geography),
('Subway Carlos Antúnez / Bilbao', 'Av. Francisco Bilbao 6200', ST_SetSRID(ST_MakePoint(-70.56583333, -33.43722222), 4326)::geography),
('Papa John''s La Reina', 'Av. Larraín 6666', ST_SetSRID(ST_MakePoint(-70.56500000, -33.44916667), 4326)::geography),

-- 8. Peñalolén
('McDonald''s Consistorial', 'Av. Consistorial 2100', ST_SetSRID(ST_MakePoint(-70.54861111, -33.47527778), 4326)::geography),
('Burger King Grecia', 'Av. Grecia 8500', ST_SetSRID(ST_MakePoint(-70.53972222, -33.47194444), 4326)::geography),
('Doggis Paseo Quilín', 'Av. Américo Vespucio 3300', ST_SetSRID(ST_MakePoint(-70.57388889, -33.48638889), 4326)::geography),
('KFC Paseo Quilín', 'Av. Américo Vespucio 3300', ST_SetSRID(ST_MakePoint(-70.57416667, -33.48666667), 4326)::geography),
('Papa John''s Peñalolén', 'Av. Consistorial 2700', ST_SetSRID(ST_MakePoint(-70.54750000, -33.48111111), 4326)::geography),

-- 9. Macul
('McDonald''s Macul', 'Av. José Pedro Alessandri 3170', ST_SetSRID(ST_MakePoint(-70.59750000, -33.49138889), 4326)::geography),
('Burger King Pedrero', 'Av. Vicuña Mackenna 6100', ST_SetSRID(ST_MakePoint(-70.61083333, -33.50722222), 4326)::geography),
('Tarragona Macul', 'Av. Macul 2800', ST_SetSRID(ST_MakePoint(-70.60027778, -33.48583333), 4326)::geography),
('Subway Campus San Joaquín', 'Av. Vicuña Mackenna 4860', ST_SetSRID(ST_MakePoint(-70.61500000, -33.49722222), 4326)::geography),
('Papa John''s Macul', 'Av. Macul 3400', ST_SetSRID(ST_MakePoint(-70.60055556, -33.49250000), 4326)::geography),

-- 10. La Florida
('McDonald''s Bellavista de La Florida', 'Av. Vicuña Mackenna 6969', ST_SetSRID(ST_MakePoint(-70.59972222, -33.52000000), 4326)::geography),
('Burger King Mallplaza Vespucio', 'Av. Vicuña Mackenna 7110', ST_SetSRID(ST_MakePoint(-70.59805556, -33.52138889), 4326)::geography),
('Pedro, Juan & Diego Florida Center', 'Av. Vicuña Mackenna 6100', ST_SetSRID(ST_MakePoint(-70.60805556, -33.51055556), 4326)::geography),
('KFC Patio La Florida', 'Av. La Florida 8988', ST_SetSRID(ST_MakePoint(-70.57527778, -33.53944444), 4326)::geography),
('Doggis Walker Martínez', 'Av. Walker Martínez 1400', ST_SetSRID(ST_MakePoint(-70.58916667, -33.52694444), 4326)::geography),

-- 11. Puente Alto
('McDonald''s Plaza de Puente Alto', 'Av. Concha y Toro 145', ST_SetSRID(ST_MakePoint(-70.57583333, -33.61000000), 4326)::geography),
('Burger King Mallplaza Tobalaba', 'Av. Camilo Henríquez 3692', ST_SetSRID(ST_MakePoint(-70.54805556, -33.56777778), 4326)::geography),
('Completon Creta', 'Av. Creta 0450', ST_SetSRID(ST_MakePoint(-70.58222222, -33.59555556), 4326)::geography),
('Pedro, Juan & Diego Plazuela Independencia', 'Av. Concha y Toro 26', ST_SetSRID(ST_MakePoint(-70.57555556, -33.61111111), 4326)::geography),
('Doggis Espacio Urbano Puente Alto', 'Av. Concha y Toro 1149', ST_SetSRID(ST_MakePoint(-70.57638889, -33.60416667), 4326)::geography),

-- 12. San Bernardo
('McDonald''s San Bernardo Plaza', 'Eyzaguirre 650', ST_SetSRID(ST_MakePoint(-70.70416667, -33.59277778), 4326)::geography),
('Burger King Mallplaza Sur', 'Av. Jorge Alessandri 20040', ST_SetSRID(ST_MakePoint(-70.70888889, -33.61944444), 4326)::geography),
('Doggis Paseo San Bernardo', 'Eyzaguirre 540', ST_SetSRID(ST_MakePoint(-70.70500000, -33.59250000), 4326)::geography),
('Pedro, Juan & Diego Mallplaza Sur', 'Av. Jorge Alessandri 20040', ST_SetSRID(ST_MakePoint(-70.70916667, -33.61972222), 4326)::geography),
('KFC San Bernardo Centro', 'Covadonga 510', ST_SetSRID(ST_MakePoint(-70.70611111, -33.59194444), 4326)::geography),

-- 13. El Bosque
('McDonald''s Gran Avenida Paradero 31', 'Av. Gran Avenida José Miguel Carrera 10200', ST_SetSRID(ST_MakePoint(-70.67000000, -33.55583333), 4326)::geography),
('Doggis Gran Avenida 11000', 'Av. Gran Avenida José Miguel Carrera 11100', ST_SetSRID(ST_MakePoint(-70.67305556, -33.56500000), 4326)::geography),
('Tarragona El Bosque', 'Av. Gran Avenida José Miguel Carrera 9800', ST_SetSRID(ST_MakePoint(-70.66916667, -33.55194444), 4326)::geography),
('Papa John''s El Bosque', 'Av. Gran Avenida José Miguel Carrera 10500', ST_SetSRID(ST_MakePoint(-70.67138889, -33.55888889), 4326)::geography),
('Telepizza El Bosque', 'Av. Gran Avenida José Miguel Carrera 11500', ST_SetSRID(ST_MakePoint(-70.67361111, -33.56861111), 4326)::geography),

-- 14. La Pintana
('Doggis Santa Rosa Paradero 38', 'Av. Santa Rosa 12400', ST_SetSRID(ST_MakePoint(-70.63416667, -33.57694444), 4326)::geography),
('Tarragona La Pintana', 'Av. Santa Rosa 11800', ST_SetSRID(ST_MakePoint(-70.63472222, -33.57138889), 4326)::geography),
('Telepizza La Pintana', 'Av. Santa Rosa 10900', ST_SetSRID(ST_MakePoint(-70.63527778, -33.56277778), 4326)::geography),
('Fuente de Soda El Rincón Pintanino', 'Av. Lo Blanco 0120', ST_SetSRID(ST_MakePoint(-70.64083333, -33.58000000), 4326)::geography),
('Comida Rápida El Buen Sabor', 'Baldomero Lillo 1850', ST_SetSRID(ST_MakePoint(-70.63388889, -33.58194444), 4326)::geography),

-- 15. San Ramón
('Doggis Metro Santa Rosa', 'Av. Américo Vespucio 01100', ST_SetSRID(ST_MakePoint(-70.64416667, -33.53583333), 4326)::geography),
('Tarragona San Ramón', 'Av. Santa Rosa 8200', ST_SetSRID(ST_MakePoint(-70.63694444, -33.52444444), 4326)::geography),
('Telepizza Santa Rosa', 'Av. Santa Rosa 9000', ST_SetSRID(ST_MakePoint(-70.63722222, -33.53333333), 4326)::geography),
('Fuente de Soda San Ramón', 'Av. Santa Rosa 8600', ST_SetSRID(ST_MakePoint(-70.63705556, -33.52888889), 4326)::geography),
('Comida Rápida El Tío', 'Av. Doñihue 1700', ST_SetSRID(ST_MakePoint(-70.64166667, -33.53111111), 4326)::geography),

-- 16. La Granja
('McDonald''s Santa Rosa', 'Av. Santa Rosa 7954', ST_SetSRID(ST_MakePoint(-70.63583333, -33.52222222), 4326)::geography),
('Doggis Espacio Urbano La Granja', 'Av. Santa Rosa 7954', ST_SetSRID(ST_MakePoint(-70.63555556, -33.52250000), 4326)::geography),
('Tarragona Américo Vespucio', 'Av. Américo Vespucio 0033', ST_SetSRID(ST_MakePoint(-70.62722222, -33.53555556), 4326)::geography),
('Pedro, Juan & Diego La Granja', 'Av. Santa Rosa 7950', ST_SetSRID(ST_MakePoint(-70.63611111, -33.52194444), 4326)::geography),
('Papa John''s La Granja', 'Av. San José de la Estrella 0400', ST_SetSRID(ST_MakePoint(-70.62083333, -33.53916667), 4326)::geography),

-- 17. San Joaquín
('McDonald''s Vicuña Mackenna Paradero 6', 'Av. Vicuña Mackenna 3400', ST_SetSRID(ST_MakePoint(-70.62416667, -33.48194444), 4326)::geography),
('Doggis Carlos Valdovinos', 'Av. Vicuña Mackenna 3900', ST_SetSRID(ST_MakePoint(-70.62027778, -33.48750000), 4326)::geography),
('Tarragona San Joaquín', 'Av. Santa Rosa 2500', ST_SetSRID(ST_MakePoint(-70.64277778, -33.47888889), 4326)::geography),
('Subway Campus San Joaquín USM', 'Av. Vicuña Mackenna 3939', ST_SetSRID(ST_MakePoint(-70.61944444, -33.48833333), 4326)::geography),
('Papa John''s San Joaquín', 'Av. Carlos Valdovinos 200', ST_SetSRID(ST_MakePoint(-70.63500000, -33.48277778), 4326)::geography),

-- 18. San Miguel
('McDonald''s Gran Avenida Paradero 12', 'Av. Gran Avenida José Miguel Carrera 4800', ST_SetSRID(ST_MakePoint(-70.65888889, -33.50194444), 4326)::geography),
('Burger King El Llano', 'Av. Gran Avenida José Miguel Carrera 3100', ST_SetSRID(ST_MakePoint(-70.65222222, -33.48361111), 4326)::geography),
('Doggis Gran Avenida 3600', 'Av. Gran Avenida José Miguel Carrera 3600', ST_SetSRID(ST_MakePoint(-70.65444444, -33.49111111), 4326)::geography),
('KFC San Miguel', 'Av. Gran Avenida José Miguel Carrera 5100', ST_SetSRID(ST_MakePoint(-70.66000000, -33.50472222), 4326)::geography),
('Papa John''s San Miguel', 'Av. Gran Avenida José Miguel Carrera 4300', ST_SetSRID(ST_MakePoint(-70.65694444, -33.49694444), 4326)::geography),

-- 19. Pedro Aguirre Cerda (PAC)
('Doggis Lo Valledor', 'Av. Carlos Valdovinos 2700', ST_SetSRID(ST_MakePoint(-70.68305556, -33.47777778), 4326)::geography),
('Tarragona Pedro Aguirre Cerda', 'Av. Clotario Blest 2400', ST_SetSRID(ST_MakePoint(-70.67638889, -33.48027778), 4326)::geography),
('Telepizza PAC', 'Av. Carlos Valdovinos 2200', ST_SetSRID(ST_MakePoint(-70.67805556, -33.47694444), 4326)::geography),
('Fuente de Soda El Clotario', 'Av. Clotario Blest 2800', ST_SetSRID(ST_MakePoint(-70.67833333, -33.48500000), 4326)::geography),
('Comida Rápida Central PAC', 'Av. Central 4500', ST_SetSRID(ST_MakePoint(-70.67500000, -33.48861111), 4326)::geography),

-- 20. Lo Espejo
('Doggis Mercado Lo Valledor', 'Av. Maipú 3301', ST_SetSRID(ST_MakePoint(-70.68777778, -33.48194444), 4326)::geography),
('Tarragona Lo Espejo', 'Av. Central Cardenal Raúl Silva Henríquez 7200', ST_SetSRID(ST_MakePoint(-70.68694444, -33.51500000), 4326)::geography),
('Telepizza Lo Espejo', 'Av. Lo Ovalle 3100', ST_SetSRID(ST_MakePoint(-70.69194444, -33.51138889), 4326)::geography),
('Fuente de Soda Silva Henríquez', 'Av. Central 8000', ST_SetSRID(ST_MakePoint(-70.68833333, -33.52222222), 4326)::geography),
('Comida Rápida Vespucio Sur', 'Av. Américo Vespucio 2900', ST_SetSRID(ST_MakePoint(-70.68722222, -33.53277778), 4326)::geography),

-- 21. La Cisterna
('McDonald''s Intermodal La Cisterna', 'Av. Gran Avenida José Miguel Carrera 5000', ST_SetSRID(ST_MakePoint(-70.66444444, -33.52666667), 4326)::geography),
('Burger King Gran Avenida', 'Av. Gran Avenida José Miguel Carrera 6500', ST_SetSRID(ST_MakePoint(-70.66250000, -33.51388889), 4326)::geography),
('Doggis Gran Avenida 7500', 'Av. Gran Avenida José Miguel Carrera 7500', ST_SetSRID(ST_MakePoint(-70.66305556, -33.52194444), 4326)::geography),
('KFC Intermodal La Cisterna', 'Av. Gran Avenida José Miguel Carrera 5000', ST_SetSRID(ST_MakePoint(-70.66416667, -33.52694444), 4326)::geography),
('Papa John''s La Cisterna', 'Av. El Parrón 0200', ST_SetSRID(ST_MakePoint(-70.66694444, -33.51944444), 4326)::geography),

-- 22. Cerrillos
('McDonald''s Mallplaza Oeste', 'Av. Américo Vespucio 1501', ST_SetSRID(ST_MakePoint(-70.71694444, -33.51500000), 4326)::geography),
('Burger King Mallplaza Oeste', 'Av. Américo Vespucio 1501', ST_SetSRID(ST_MakePoint(-70.71722222, -33.51527778), 4326)::geography),
('Pedro, Juan & Diego Mallplaza Oeste', 'Av. Américo Vespucio 1501', ST_SetSRID(ST_MakePoint(-70.71666667, -33.51472222), 4326)::geography),
('KFC Pedro Aguirre Cerda', 'Av. Pedro Aguirre Cerda 6400', ST_SetSRID(ST_MakePoint(-70.71805556, -33.49611111), 4326)::geography),
('Doggis Mallplaza Oeste', 'Av. Américo Vespucio 1501', ST_SetSRID(ST_MakePoint(-70.71750000, -33.51555556), 4326)::geography),

-- 23. Maipú
('McDonald''s Plaza de Maipú', 'Av. Pajaritos 2150', ST_SetSRID(ST_MakePoint(-70.75694444, -33.50888889), 4326)::geography),
('Burger King Arauco Maipú', 'Av. Américo Vespucio 399', ST_SetSRID(ST_MakePoint(-70.75138889, -33.48027778), 4326)::geography),
('Carl''s Jr. Mall Arauco Maipú', 'Av. Américo Vespucio 399', ST_SetSRID(ST_MakePoint(-70.75166667, -33.48055556), 4326)::geography),
('Johnny Rockets Arauco Maipú', 'Av. Américo Vespucio 399', ST_SetSRID(ST_MakePoint(-70.75111111, -33.48000000), 4326)::geography),
('Doggis Plaza Maipú', 'Av. Pajaritos 2000', ST_SetSRID(ST_MakePoint(-70.75750000, -33.51027778), 4326)::geography),

-- 24. Estación Central
('McDonald''s Terminal Alameda', 'Av. Libertador Bernardo O''Higgins 3850', ST_SetSRID(ST_MakePoint(-70.68694444, -33.45361111), 4326)::geography),
('Burger King Estación Central', 'Av. Libertador Bernardo O''Higgins 3250', ST_SetSRID(ST_MakePoint(-70.68083333, -33.45222222), 4326)::geography),
('KFC Mall Arauco Estación', 'Av. Libertador Bernardo O''Higgins 3250', ST_SetSRID(ST_MakePoint(-70.68111111, -33.45250000), 4326)::geography),
('Pedro, Juan & Diego Terminal Borja', 'San Borja 122', ST_SetSRID(ST_MakePoint(-70.68000000, -33.45388889), 4326)::geography),
('Doggis Estación Central', 'Av. Libertador Bernardo O''Higgins 3170', ST_SetSRID(ST_MakePoint(-70.67888889, -33.45166667), 4326)::geography),

-- 25. Lo Prado
('Doggis Metro Lo Prado', 'Av. San Pablo 5700', ST_SetSRID(ST_MakePoint(-70.71333333, -33.44333333), 4326)::geography),
('Tarragona San Pablo', 'Av. San Pablo 5900', ST_SetSRID(ST_MakePoint(-70.71555556, -33.44305556), 4326)::geography),
('Telepizza Lo Prado', 'Av. San Pablo 6100', ST_SetSRID(ST_MakePoint(-70.71805556, -33.44277778), 4326)::geography),
('Fuente de Soda Neptuno', 'Av. Neptuno 700', ST_SetSRID(ST_MakePoint(-70.71972222, -33.44611111), 4326)::geography),
('Comida Rápida San Pablo', 'Av. San Pablo 5400', ST_SetSRID(ST_MakePoint(-70.71000000, -33.44388889), 4326)::geography),

-- 26. Pudahuel
('McDonald''s Aeropuerto Santiago T2', 'Av. Armando Cortinez Norte 2150', ST_SetSRID(ST_MakePoint(-70.79444444, -33.39305556), 4326)::geography),
('Burger King Aeropuerto Santiago', 'Av. Armando Cortinez Norte 2150', ST_SetSRID(ST_MakePoint(-70.79472222, -33.39333333), 4326)::geography),
('Doggis San Pablo Pudahuel', 'Av. San Pablo 8400', ST_SetSRID(ST_MakePoint(-70.74805556, -33.44194444), 4326)::geography),
('Tarragona Pudahuel', 'Av. Teniente Cruz 700', ST_SetSRID(ST_MakePoint(-70.74444444, -33.44555556), 4326)::geography),
('Papa John''s Pudahuel', 'Av. Enea 1000', ST_SetSRID(ST_MakePoint(-70.76861111, -33.43194444), 4326)::geography),

-- 27. Cerro Navia
('Doggis Mapocho Cerro Navia', 'Camino Mapocho 7300', ST_SetSRID(ST_MakePoint(-70.73916667, -33.42777778), 4326)::geography),
('Tarragona San Francisco', 'Av. San Francisco 7000', ST_SetSRID(ST_MakePoint(-70.73500000, -33.42888889), 4326)::geography),
('Telepizza Cerro Navia', 'Av. José Joaquín Pérez 6500', ST_SetSRID(ST_MakePoint(-70.72888889, -33.43055556), 4326)::geography),
('Fuente de Soda El Buenísimo', 'Av. Huelén 1600', ST_SetSRID(ST_MakePoint(-70.73222222, -33.43166667), 4326)::geography),
('Comida Rápida Mapocho', 'Camino Mapocho 6800', ST_SetSRID(ST_MakePoint(-70.73194444, -33.42805556), 4326)::geography),

-- 28. Quinta Normal
('McDonald''s Matucana', 'Av. Matucana 500', ST_SetSRID(ST_MakePoint(-70.67805556, -33.44250000), 4326)::geography),
('Doggis Carrascal', 'Av. Carrascal 4500', ST_SetSRID(ST_MakePoint(-70.69444444, -33.42805556), 4326)::geography),
('Tarragona Quinta Normal', 'Av. San Pablo 3500', ST_SetSRID(ST_MakePoint(-70.68694444, -33.44194444), 4326)::geography),
('Telepizza Mapocho', 'Av. Mapocho 4100', ST_SetSRID(ST_MakePoint(-70.68888889, -33.43333333), 4326)::geography),
('Papa John''s Quinta Normal', 'Av. Matucana 800', ST_SetSRID(ST_MakePoint(-70.68111111, -33.43805556), 4326)::geography),

-- 29. Renca
('Doggis Plaza de Renca', 'Av. Blanco Encalada 1330', ST_SetSRID(ST_MakePoint(-70.71027778, -33.40444444), 4326)::geography),
('Tarragona Renca', 'Av. Blanco Encalada 1250', ST_SetSRID(ST_MakePoint(-70.70916667, -33.40472222), 4326)::geography),
('Telepizza Renca', 'Av. Dorsal 1500', ST_SetSRID(ST_MakePoint(-70.70416667, -33.40777778), 4326)::geography),
('Fuente de Soda Renca Centro', 'Av. Senador Jaime Guzmán 1400', ST_SetSRID(ST_MakePoint(-70.71194444, -33.40388889), 4326)::geography),
('Comida Rápida El Rey del Completo', 'Av. Vicuña Mackenna Renca 2000', ST_SetSRID(ST_MakePoint(-70.71444444, -33.40111111), 4326)::geography),

-- 30. Quilicura
('McDonald''s Mall Arauco Quilicura', 'O’Higgins 681', ST_SetSRID(ST_MakePoint(-70.72944444, -33.36166667), 4326)::geography),
('Burger King Easton Outlet Mall', 'Av. Presidente Eduardo Frei Montalva 9709', ST_SetSRID(ST_MakePoint(-70.71444444, -33.34888889), 4326)::geography),
('KFC Arauco Quilicura', 'O’Higgins 681', ST_SetSRID(ST_MakePoint(-70.72916667, -33.36194444), 4326)::geography),
('Pedro, Juan & Diego Quilicura', 'José Francisco Vergara 300', ST_SetSRID(ST_MakePoint(-70.72805556, -33.36500000), 4326)::geography),
('Doggis Quilicura Centro', 'José Francisco Vergara 400', ST_SetSRID(ST_MakePoint(-70.72888889, -33.36444444), 4326)::geography),

-- 31. Conchalí
('McDonald''s Independencia Conchalí', 'Av. Independencia 3800', ST_SetSRID(ST_MakePoint(-70.67444444, -33.39194444), 4326)::geography),
('Doggis Metro Conchalí', 'Av. Independencia 3700', ST_SetSRID(ST_MakePoint(-70.67388889, -33.39305556), 4326)::geography),
('Tarragona Conchalí', 'Av. Independencia 3400', ST_SetSRID(ST_MakePoint(-70.67194444, -33.39777778), 4326)::geography),
('Telepizza Conchalí', 'Av. Dorsal 1400', ST_SetSRID(ST_MakePoint(-70.66888889, -33.40000000), 4326)::geography),
('Papa John''s Conchalí', 'Av. Pedro Fontova 3900', ST_SetSRID(ST_MakePoint(-70.66944444, -33.38888889), 4326)::geography),

-- 32. Independencia
('McDonald''s Mall Barrio Independencia', 'Av. Independencia 565', ST_SetSRID(ST_MakePoint(-70.65305556, -33.42861111), 4326)::geography),
('Burger King Mall Barrio Independencia', 'Av. Independencia 565', ST_SetSRID(ST_MakePoint(-70.65333333, -33.42888889), 4326)::geography),
('KFC Hipódromo', 'Av. Hipódromo Chile 1600', ST_SetSRID(ST_MakePoint(-70.66111111, -33.40944444), 4326)::geography),
('Doggis Hospital J.J. Aguirre', 'Santos Dumont 900', ST_SetSRID(ST_MakePoint(-70.65388889, -33.41916667), 4326)::geography),
('Pedro, Juan & Diego Independencia', 'Av. Independencia 600', ST_SetSRID(ST_MakePoint(-70.65361111, -33.42805556), 4326)::geography),

-- 33. Huechuraba
('McDonald''s Mallplaza Norte', 'Av. Américo Vespucio 1737', ST_SetSRID(ST_MakePoint(-70.67805556, -33.36444444), 4326)::geography),
('Burger King Ciudad Empresarial', 'Av. del Valle 600', ST_SetSRID(ST_MakePoint(-70.61750000, -33.38444444), 4326)::geography),
('Carl''s Jr. Mallplaza Norte', 'Av. Américo Vespucio 1737', ST_SetSRID(ST_MakePoint(-70.67833333, -33.36472222), 4326)::geography),
('KFC Ciudad Empresarial', 'Av. del Valle 750', ST_SetSRID(ST_MakePoint(-70.61861111, -33.38333333), 4326)::geography),
('Pedro, Juan & Diego Mallplaza Norte', 'Av. Américo Vespucio 1737', ST_SetSRID(ST_MakePoint(-70.67777778, -33.36416667), 4326)::geography),

-- 34. Recoleta
('McDonald''s Bellavista Recoleta', 'Pío Nono 100', ST_SetSRID(ST_MakePoint(-70.63472222, -33.43388889), 4326)::geography),
('Doggis La Vega Central', 'Antonia López de Bello 743', ST_SetSRID(ST_MakePoint(-70.64805556, -33.43000000), 4326)::geography),
('Tarragona Patronato', 'Av. Patronato 300', ST_SetSRID(ST_MakePoint(-70.64416667, -33.42944444), 4326)::geography),
('Pedro, Juan & Diego Recoleta', 'Av. Recoleta 300', ST_SetSRID(ST_MakePoint(-70.64527778, -33.43111111), 4326)::geography),
('Papa John''s Recoleta', 'Av. Recoleta 1200', ST_SetSRID(ST_MakePoint(-70.64472222, -33.42083333), 4326)::geography);