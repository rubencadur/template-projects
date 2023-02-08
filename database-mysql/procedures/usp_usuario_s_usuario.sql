DELIMITER $$

DROP PROCEDURE IF EXISTS `usp_usuario_s_usuario`$$

/*
    AUTHOR:         Ruben Cadenas
    DATE:           20230124
    DESCRIPTION:    Returns the data of aa user
    EXAMPLE:
        CALL usp_usuario_s_usuario('admin');
*/
CREATE PROCEDURE usp_usuario_s_usuario(
    IN p_username VARCHAR(50)
)
BEGIN

    SELECT 
        `usuario_id`,
        `username`,
        `email`,
        `password`
    FROM
        `usuario`
    WHERE 
        `eliminado` = 0
        AND `username` = p_username;

END$$

DELIMITER ;