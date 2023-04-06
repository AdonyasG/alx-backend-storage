-- create trigger before insert
-- updaitng multiple tables using sql script
CREATE TRIGGER reset_valid_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;