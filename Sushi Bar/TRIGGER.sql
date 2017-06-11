--Procedura wyzwalana maj¹ca na celu uniemo¿liwienie wprowadzenia do bazy danych rachunku o ujemnej wartoœci:

SET client_encoding='utf-8';

CREATE FUNCTION przykladowy_trigger() RETURNS trigger AS $_trigger$
    BEGIN
        -- Sprawdzenie
        IF NEW.Cena < 0 THEN
            RAISE EXCEPTION 'Rachunek nie moze byc ujemny!';
        END IF;
    END;
	
$_trigger$ LANGUAGE plpgsql;

CREATE TRIGGER przykladowy_trigger BEFORE INSERT OR UPDATE ON Rachunek
    FOR EACH ROW EXECUTE PROCEDURE przykladowy_trigger();