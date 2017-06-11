SET client_encoding='utf-8';

INSERT INTO Kasjer(Imie, Nazwisko) VALUES('Jan', 'Kowalski');
INSERT INTO Kasjer(Imie, Nazwisko) VALUES('Wojciech', 'Nowak');
INSERT INTO Kasjer(Imie, Nazwisko) VALUES('Adam', 'Staszewski');
INSERT INTO Kasjer(Imie, Nazwisko) VALUES('Piotr', 'Andrzejkiewicz');
INSERT INTO Kasjer(Imie, Nazwisko) VALUES('Karol', 'Igrek');
INSERT INTO Kasjer(Imie, Nazwisko) VALUES('Maciej', 'Zetniewski');

INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Mito sushi', 'Morska 220 Rumia', 660550112);
INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Koku sushi', 'Grunwaldzka 515 Gdańsk', 123456899);
INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Izakaya sushi', 'Morska 15 Gdynia', 55132225);
INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Hashi sushi', 'Ujejskiego 4/5 Sopot', 155505595);
INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Handroll', '10 Lutego 73 Gdynia', 998558558);
INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Osaka sushi', 'Koziorozca 27 Gdansk', 664439220);
INSERT INTO Sushi_Bar(Nazwa, Adres, Numer_kontaktowy) VALUES('Fusion sushi', 'Marcowa 16 Sopot', 535009558);

INSERT INTO Menadzer(Imię, Nazwisko, Numer_kontaktowy) VALUES('Patryk', 'Fzetski', 992992992);
INSERT INTO Menadzer(Imię, Nazwisko, Numer_kontaktowy) VALUES('Konrad', 'Fzetski', 1235125645);
INSERT INTO Menadzer(Imię, Nazwisko, Numer_kontaktowy) VALUES('Jakub', 'Monk', 993994995);
INSERT INTO Menadzer(Imię, Nazwisko, Numer_kontaktowy) VALUES('Grzegorz', 'Krymz', 664667996);
INSERT INTO Menadzer(Imię, Nazwisko, Numer_kontaktowy) VALUES('Jacek', 'Piekarz', 660005995);
INSERT INTO Menadzer(Imię, Nazwisko, Numer_kontaktowy) VALUES('Patryk', 'Adamek', 559339229);

INSERT INTO Sushi_Master(Imię, Nazwisko) VALUES ('Kajetan', 'Romski');
INSERT INTO Sushi_Master(Imię, Nazwisko) VALUES ('Arek', 'Romski');
INSERT INTO Sushi_Master(Imię, Nazwisko) VALUES ('Adam', 'Grzybkowski');
INSERT INTO Sushi_Master(Imię, Nazwisko) VALUES ('Patryk', 'Witczak');
INSERT INTO Sushi_Master(Imię, Nazwisko) VALUES ('Jakub', 'Iławski');
INSERT INTO Sushi_Master(Imię, Nazwisko) VALUES ('Franciszek', 'Ikniewski');

INSERT INTO Zamówienie1(Ilość_zestawów) VALUES(1);
INSERT INTO Zamówienie1(Ilość_zestawów) VALUES(4);
INSERT INTO Zamówienie1(Ilość_zestawów) VALUES(4);
INSERT INTO Zamówienie1(Ilość_zestawów) VALUES(1);
INSERT INTO Zamówienie1(Ilość_zestawów) VALUES(2);
INSERT INTO Zamówienie1(Ilość_zestawów) VALUES(1);

INSERT INTO Zestaw_Sushi(Nazwa, Ilość_Kawałków, Cena, Cena_po_obnizce, Opis) VALUES('Futo-Maki Set', 24, 59, 49, 'Zestaw futo-maki');
INSERT INTO Zestaw_Sushi(Nazwa, Ilość_Kawałków, Cena, Cena_po_obnizce, Opis) VALUES('California-Maki Set', 16, 59, 49, 'Zestaw california-maki');
INSERT INTO Zestaw_Sushi(Nazwa, Ilość_Kawałków, Cena, Cena_po_obnizce, Opis) VALUES('Hoso-Maki Set', 24, 39, 29, 'Zestaw hoso-maki');
INSERT INTO Zestaw_Sushi(Nazwa, Ilość_Kawałków, Cena, Cena_po_obnizce, Opis) VALUES('Nigiri Set', 12, 49, 39, 'Zestaw nigiri');
INSERT INTO Zestaw_Sushi(Nazwa, Ilość_Kawałków, Cena, Cena_po_obnizce, Opis) VALUES('Mix Set', 22, 65, 55, 'Zestaw MIX');
INSERT INTO Zestaw_Sushi(Nazwa, Ilość_Kawałków, Cena, Cena_po_obnizce, Opis) VALUES('Grill Set', 20, 85, 75, 'Zestaw grill');

INSERT INTO Kelner(Imię, Nazwisko) VALUES('Tadeusz', 'Kamiński');
INSERT INTO Kelner(Imię, Nazwisko) VALUES('Sylwester', 'Igniński');
INSERT INTO Kelner(Imię, Nazwisko) VALUES('Kazimierz', 'Ortan');
INSERT INTO Kelner(Imię, Nazwisko) VALUES('Wojciech', 'Nowak');
INSERT INTO Kelner(Imię, Nazwisko) VALUES('Maksymilian', 'Arczyński');
INSERT INTO Kelner(Imię, Nazwisko) VALUES('Jan', 'Sobieski');

INSERT INTO Klient(Imię, Adres, Numer_kontaktowy) VALUES('Jan', 'Strzyża 15 Gdynia', 663555553);
INSERT INTO Klient(Imię, Adres, Numer_kontaktowy) VALUES('Jan', 'Grunwaldzka 15 Gdańsk', 663554213);
INSERT INTO Klient(Imię, Adres, Numer_kontaktowy) VALUES('Jan', 'Niepodległości 15 Gsopot', 600055553);
INSERT INTO Klient(Imię, Adres, Numer_kontaktowy) VALUES('Jan', 'Strzyża 11 Gdynia', 622155553);
INSERT INTO Klient(Imię, Adres, Numer_kontaktowy) VALUES('Jan', 'Spokojna 7 Gdynia', 663550403);
INSERT INTO Klient(Imię, Adres, Numer_kontaktowy) VALUES('Jan', 'Wiśniewskiego 192 Gdynia', 660005553);

INSERT INTO Rachunek(Cena) VALUES(59);
INSERT INTO Rachunek(Cena) VALUES(192);
INSERT INTO Rachunek(Cena) VALUES(500);
INSERT INTO Rachunek(Cena) VALUES(123);
INSERT INTO Rachunek(Cena) VALUES(200);
INSERT INTO Rachunek(Cena) VALUES(155);





