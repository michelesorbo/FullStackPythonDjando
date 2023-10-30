SELECT main_pazienti.nome, main_pazienti.cognome, main_medici.nome as MedicoNome , main_medici.cognome as MedicoCognome
FROM main_pazienti
INNER JOIN main_medici ON main_pazienti.medico_id = main_medici.id