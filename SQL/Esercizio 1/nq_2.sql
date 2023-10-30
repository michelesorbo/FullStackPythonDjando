/*Le informazioni delle persone che hanno almeno un numero telefonico. Evitare i duplicati in output.*/
SELECT DISTINCT numeri_telefonici.id_persona, persone.nome, persone.cognome
FROM persone
INNER JOIN numeri_telefonici ON numeri_telefonici.id_persona = persone.id