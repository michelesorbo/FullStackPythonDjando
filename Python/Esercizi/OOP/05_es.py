"""
E' necessario scrivere una applicazione che simula il funzionamento di un frammento del sistema
informativo di un operatore di telefonia cellulare.

Si devono quindi rappresentare i dati relativi ad una carta SIM ed in particolare:
- il numero di telefono
- il credito disponibile in euro
- la lista delle telefonate effettuate (da conservare in un file .txt nominato <numero_sim>.txt)

Per ciascuna telefonata deve essere rappresentata la durata in minuti

La classe SIM dovrà fornire le seguenti funzionalità:
- un costruttore parametrizzato che crea una SIM con numero di telefono, un credito e
la lista delle telefonate vuota

- un metodo per l'inserimento di una telefonata con i dati forniti dall'utente.

- una funzione per il calcolo dei minuti totali di conversazione.

- una funzione per il calcolo delle telefonate effettuate verso un certo numero SE RIUSCITE

- una procedura per la stampa dei dati della SIM e l'elenco delle telefonate.

ES:
s1 = SIM("3372345654", 15.84)
dopo vado a leggere se è presente altrimento lo creo il file 3372345654.txt

Il file txt per singolo numero sarà organizzato 

<numero chiamato> <tempo in secondi della telefonato>
3358969785 125
3358969785 45
55899669 32
"""
