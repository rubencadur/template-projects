CREATE TABLE `usuario` (
    `usuario_id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(30),
    `nombres` VARCHAR(50),
    `apellidos` VARCHAR(50),
    `email` VARCHAR(100),
    `password` VARCHAR(255),
    `eliminado` TINYINT(1),
    `insert_userid` INT,
    `insert_datetime` DATETIME,
    `update_userid` INT,
    `update_datetime` DATETIME,
    `delete_userid` INT,
    `delete_datetime` DATETIME,
    PRIMARY KEY (`usuario_id`)
);