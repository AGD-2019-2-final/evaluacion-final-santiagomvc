-- 
-- Pregunta
-- ===========================================================================
--
-- Para resolver esta pregunta use el archivo `data.tsv`.
--
-- Escriba una consulta que devuelva los cinco valores diferentes más pequeños 
-- de la tercera columna.
--
-- Escriba el resultado a la carpeta `output` de directorio de trabajo.
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
DROP TABLE IF EXISTS thive3;
CREATE TABLE thive3 (
    letra STRING,
    fecha STRING,
    numero INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

LOAD DATA LOCAL INPATH  'data.tsv' OVERWRITE INTO TABLE thive3;

INSERT OVERWRITE LOCAL DIRECTORY 'output' ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
SELECT DISTINCT numero
FROM thive3
ORDER BY numero
LIMIT 5;