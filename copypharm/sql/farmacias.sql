CREATE TABLE IF NOT EXISTS `farmacias` (
    `id` INT,
    `nombre` VARCHAR(255) NOT NULL,
    `id_localidad` INT NOT NULL,
    `id_departamento` INT NOT NULL,
    `codigo_postal` INT NOT NULL, 
    `domicilio` VARCHAR(255) NOT NULL,
    CONSTRAINT pk_user_id_farmacias PRIMARY KEY (`id`)
);