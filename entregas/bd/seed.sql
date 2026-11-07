INSERT INTO entregas (hora_aceptacion, hora_recogida, hora_entrega, monto, id_local, app)
WITH base AS (
    SELECT
        l.id_local,
        random() AS r_tipo,
        random() AS r_unif,
        sqrt(-2 * ln(1 - random())) * cos(2 * pi() * random()) AS z,
        random() AS r_prep,
        random() AS r_trayecto,
        sqrt(-2 * ln(1 - random())) * cos(2 * pi() * random()) AS z_monto,
        random() AS r_app
    FROM generate_series(1, 170) AS l(id_local)
    CROSS JOIN LATERAL generate_series(1, 85 + floor(random() * 31)::int) AS g(n)
),
t AS (
    SELECT *,
        GREATEST(600, LEAST(1370,
            CASE
                WHEN r_tipo < 0.45 THEN 810  + z * 60
                WHEN r_tipo < 0.85 THEN 1260 + z * 70
                ELSE 600 + r_unif * 780
            END
        )) AS min_acept
    FROM base
),
f AS (
    SELECT *,
        (TIMESTAMP '2026-11-30 00:00:00' AT TIME ZONE 'America/Santiago')
            + make_interval(secs => min_acept * 60) AS acept
    FROM t
)
SELECT
    acept AS hora_aceptacion,
    acept + make_interval(secs => (5 + r_prep * 15) * 60) AS hora_recogida,
    acept + make_interval(secs => ((5 + r_prep * 15) + (8 + r_trayecto * 27)) * 60) AS hora_entrega,
    GREATEST(1100, LEAST(5000,
        round(exp(ln(2300) + 0.38 * z_monto) / 10) * 10
    ))::int AS monto,
    id_local,
    CASE
        WHEN r_app < 0.45 THEN 'PedidosYa'
        WHEN r_app < 0.80 THEN 'Uber Eats'
        ELSE 'Rappi'
    END AS app
FROM f;