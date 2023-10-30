/*Marca e modello degli smartphone. 
Evitare che lo stesso modello di una marca compaia più volte a schermo nel risultato della query.*/

SELECT DISTINCT modello, marca
FROM smartphone