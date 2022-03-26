CREATE TABLE IF NOT EXISTS `departamentos` (
    `id_departamento` INT,
    `nombre_departamento` VARCHAR(255) NOT NULL,
    CONSTRAINT pk_user_id_departamento PRIMARY KEY (`id_departamento`)
);