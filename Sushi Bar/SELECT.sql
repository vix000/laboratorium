SET client_encoding='utf-8';

--Podaj informacje o sushi barach majacych w nazwie 'sushi' malejaco:

SELECT ID_baru, Nazwa, Numer_kontaktowy 
FROM Sushi_Bar
WHERE Nazwa LIKE '%sushi%' ORDER BY Nazwa DESC;


--Podaj wszystkie zestawy o nazwie Futo-Maki Set lub California Set
--których cena przekracza 50 z³otych:

SELECT * FROM Zestaw_sushi 
WHERE (Nazwa = 'Futo-Maki Set' OR
Nazwa = 'California Set') AND Cena > 50;

--Podaj dane dotyczace zestawu ktorego cena po obnizce
--jest zawiera sie w przedziale 10 < Cena_po_obnizce < 30
--u³o¿one rosn¹co

SELECT ID_zestawu, Nazwa, Cena_po_obnizce FROM Zestaw_sushi
WHERE Cena_po_obnizce < 30 AND Cena_po_obnizce > 10
ORDER BY Nazwa ASC;

--Podaj ID Sushi Baru gdzie numer kontaktowy jest podany:

SELECT * FROM Sushi_Bar
WHERE ID_Baru IN
(SELECT ID_Baru FROM Sushi_Bar WHERE Numer_kontaktowy IS NOT NULL );