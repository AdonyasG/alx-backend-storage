-- create trigger before insert
-- updaitng multiple tables using sql script
CREATE TRiGGER reset_attribute
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    UPDATE users
    SET NEW.valid_email = default_value;
    END IF;
END;