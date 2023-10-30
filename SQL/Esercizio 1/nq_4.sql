/*Elenco degli smartphone di marca Samsung posseduti da Mario Rossi. */
SELECT smartphone.modello, smartphone_posseduti.data_acquisto
FROM smartphone_posseduti
INNER JOIN persone ON smartphone_posseduti.id_persona = persone.id
INNER JOIN smartphone ON smartphone_posseduti.id_smartphone = smartphone.id
WHERE persone.nome = 'Mario' AND persone.cognome