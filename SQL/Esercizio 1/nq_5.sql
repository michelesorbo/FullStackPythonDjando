/*Elenco delle persone che hanno almeno un numero telefonico con la compagnia "TIM".*/
SELECT DISTINCT persone.*
FROM numeri_telefonici
INNER JOIN persone ON numeri_telefonici.id_persona = persone.id
WHERE compagnia_telefonica = 'TIM'