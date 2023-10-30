CREATE TABLE libri (
	"id" INTEGER,
	"titolo" varchar(150) NOT NULL,
	"descrizione" varchar(250),
	"anno_pubblicazione" date,
	PRIMARY KEY ("id" AUTOINCREMENT)
);