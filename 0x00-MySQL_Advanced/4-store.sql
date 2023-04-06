-- create trigger before insert
-- updaitng multiple tables using sql script
CREATE TRiGGER decrease_quantity
BEFORE INSERT ON orders
FOR EACH ROW
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE NAME = NEW.item_name;