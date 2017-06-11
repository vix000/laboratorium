SET client_encoding='utf-8';

CREATE TABLE Kasjer (
	ID_kasjera SERIAL NOT NULL,
	Imie varchar(50) NOT NULL,
	Nazwisko varchar(250) NOT NULL,
	CONSTRAINT ID_PK PRIMARY KEY(ID_kasjera)
);

CREATE TABLE Sushi_Bar (
    ID_baru SERIAL NOT NULL,
	Nazwa varchar(250) NOT NULL,	
	Adres varchar(250) NOT NULL,
	Numer_kontaktowy INT NOT NULL,
	CONSTRAINT ID_PK2 PRIMARY KEY(ID_baru)
	
);

CREATE TABLE Menadzer (
	ID_menadzera SERIAL NOT NULL,
	Imię VARCHAR(50),
	Nazwisko VARCHAR(250),
	Numer_kontaktowy INT,
	CONSTRAINT ID_PK3 PRIMARY KEY(ID_menadzera)
);

CREATE TABLE Sushi_Master (
	ID SERIAL NOT NULL,
	Imię VARCHAR(50),
	Nazwisko VARCHAR(250),
	CONSTRAINT ID_PK4 PRIMARY KEY(ID)
);

CREATE TABLE Zamówienie (
	Numer_zamówienia SERIAL NOT NULL,
	Ilość_zestawów INT NOT NULL,
	CONSTRAINT ID_PK5 PRIMARY KEY(Numer_zamówienia)
);

CREATE TABLE Zestaw_sushi (
	ID_zestawu SERIAL NOT NULL,
	Nazwa VARCHAR(50) NOT NULL,
	Ilość_Kawałków INT NOT NULL,
	Cena NUMERIC CHECK (CENA > 0),
	Cena_po_obnizce NUMERIC CHECK (Cena_po_obnizce > 0),
	CHECK (Cena > Cena_po_obnizce),
	Opis VARCHAR(500) DEFAULT 'Brak',
	CONSTRAINT ID_PK6 PRIMARY KEY(ID_zestawu)
);

CREATE TABLE Kelner (
	ID_kelnera SERIAL NOT NULL,
	Imię VARCHAR(50) NOT NULL,
	Nazwisko VARCHAR(250) NOT NULL,
	CONSTRAINT ID_PK7 PRIMARY KEY(ID_kelnera)
);

CREATE TABLE Klient (
	ID_klienta SERIAL NOT NULL,
	Imię VARCHAR(50) NOT NULL,
	Adres VARCHAR(250) NOT NULL,
	Numer_kontaktowy INT NOT NULL,
	CONSTRAINT ID_PK8 PRIMARY KEY(ID_klienta)
);

CREATE TABLE Rachunek (
	Numer_rachunku SERIAL NOT NULL,
	Cena INT NOT NULL,
	Szczególy_zamówienia VARCHAR(500) DEFAULT 'Brak szczegółów',
	CONSTRAINT ID_PK9 PRIMARY KEY(Numer_rachunku)
);

CREATE TABLE Zatrudnienie_kasjera (
	zatr_kasjer INT NOT NULL,
	zatr_bar INT NOT NULL,
	CONSTRAINT zatr_kasjer_FK FOREIGN KEY(zatr_kasjer)
		REFERENCES Kasjer(ID_kasjera)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT zatr_sushi_bar_FK FOREIGN KEY(zatr_bar)
		REFERENCES Sushi_Bar(ID_baru)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Zatrudnienie_menadzera (
	zatr_menadz INT NOT NULL,
	zatr_bar INT NOT NULL,
	CONSTRAINT zatr_menadz_FK FOREIGN KEY(zatr_menadz)
		REFERENCES Menadzer(ID_menadzera)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT zatr_sushi_bar_FK FOREIGN KEY(zatr_bar)
		REFERENCES Sushi_Bar(ID_baru)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Zlecenie (
	zlec_SM INT NOT NULL,
	zlec_menadz INT NOT NULL,
	CONSTRAINT zlec_SM_FK FOREIGN KEY(zlec_SM)
		REFERENCES Sushi_Master(ID)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT zlec_menadz_FK FOREIGN KEY(zlec_menadz)
		REFERENCES Menadzer(ID_menadzera)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Przygotowanie_zamówienia (
	przyg_zam INT NOT NULL,
	przyg_SM INT NOT NULL,
	CONSTRAINT przyg_zam_FK FOREIGN KEY(przyg_zam)
		REFERENCES Zamówienie1(Numer_zamówienia)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT przyg_SM_FK FOREIGN KEY(przyg_SM)
		REFERENCES Sushi_Master(ID)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Co_zawiera_zamówienie (
	zaw_zestaw INT NOT NULL,
	zaw_zam INT NOT NULL,
	CONSTRAINT zaw_zestaw_FK FOREIGN KEY(zaw_zestaw)
		REFERENCES Zestaw_sushi(ID_zestawu)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT zaw_zam_FK FOREIGN KEY(zaw_zam)
		REFERENCES Zamówienie1(Numer_zamówienia)
		ON UPDATE CASCADE ON DELETE CASCADE
);
	
CREATE TABLE Przyjecie_zamówienia (
	przyj_zam INT NOT NULL,
	przyj_kel INT NOT NULL,
	CONSTRAINT przyj_zam_FK FOREIGN KEY(przyj_zam)
		REFERENCES Zamówienie1(Numer_zamówienia)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT przyj_kel_FK FOREIGN KEY(przyj_kel)
		REFERENCES Kelner(ID_kelnera)
		ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Złożenie_zamówienia (
	zloz_zam INT NOT NULL,
	zloz_klient INT NOT NULL,
	CONSTRAINT zloz_zam_FK FOREIGN KEY(zloz_zam)
		REFERENCES Zamówienie1(Numer_zamówienia)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT zloz_klient_FK FOREIGN KEY(zloz_klient)
		REFERENCES Klient(ID_klienta)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Dostarczenie (
	dost_klient INT NOT NULL,
	dost_kelner INT NOT NULL,
	CONSTRAINT dost_klient_FK FOREIGN KEY(dost_klient)
		REFERENCES Klient(ID_klienta)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT dost_kelner_FK FOREIGN KEY(dost_kelner)
		REFERENCES Kelner(ID_kelnera)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Placenie (
	plac_rach INT NOT NULL,
	plac_klient INT NOT NULL,
	CONSTRAINT plac_rach_FK FOREIGN KEY(plac_rach)
		REFERENCES Rachunek(Numer_rachunku)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT plac_klient_FK FOREIGN KEY(plac_klient)
		REFERENCES Klient(ID_klienta)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Przyjecie_rachunku (
	przyj_rach INT NOT NULL,
	przyj_kasjer INT NOT NULL,
	CONSTRAINT przyj_rach_FK FOREIGN KEY(przyj_rach)
		REFERENCES Rachunek(Numer_rachunku)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT przyj_kasjer_FK FOREIGN KEY(przyj_kasjer)
		REFERENCES Kasjer(ID_kasjera)
		ON UPDATE CASCADE ON DELETE CASCADE
);