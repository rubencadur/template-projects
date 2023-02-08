DELIMITER $$

DROP PROCEDURE IF EXISTS `usp_usuario_s_generarToken`$$

/*
    AUTHOR:         Ruben Cadenas
    DATE:           20230124
    DESCRIPTION:    
    EXAMPLE:
        CALL usp_usuario_s_generarToken('admin', @o);
        select @o;
*/
CREATE PROCEDURE usp_usuario_s_generarToken(
    IN p_username VARCHAR(50),
    OUT o_token varchar(250)
)
BEGIN

    IF (EXISTS(SELECT `usuario_id` FROM `usuario` WHERE `eliminado` = 0 AND `username` = p_username)) THEN
		SET o_token = UUID();
        UPDATE `usuario` SET token = o_token WHERE `username` = p_username;
    END IF;

END$$

DELIMITER ;