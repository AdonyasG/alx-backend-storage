-- create trigger before insert
-- updaitng multiple tables using sql script
DELIMITER //
CREATE TRIGGER reset_valid_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = default_value;
  END IF;
END//
DELIMITER ;