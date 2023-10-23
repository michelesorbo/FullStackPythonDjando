"""
Le classi sono uno strumento che ci permette di raggruppare variabili e funzioni 
nei nostri programmi in maniera logica e riutilizzabile.

Voglio Gestire gli alunni di una scuola. Le caratteristiche degli alunni saranno: 
- Nome
- Cognome
- Classe
- Matricola
"""
studente = ["Luca","Rossi","3A", "MT001"]
studente2 = ["Mario","Verdi","4A", "MT002"]
#Per creare una classe si unsa la key class, e il nome della classe con iniziale MAIUSCOLA
class Studente:
    ore_settimanali = 36 #Vsriabile di classe è uguale per tutte le istanze

    #Prorietà della classe, con il metodo costruttore della classe
    #Il metodo costruttore è il primo metodo chiamato appena si istanzia la calsse
    def __init__(self, nome, cognome, classe, matricola):
        #Vado a definire gli attributi della classe
        self.nome = nome #self.nome è una variabile di istanza (visibile e utilizzabile da tutta la classe e da tutte le istanze). Sono diverse per le varie istanze
        self.cognome = cognome
        self.classe = classe
        self.matricola = matricola
    
    #Dichiaro il metodo presentaStudente.
    def presentaStudente(self):
        if self.classe == "3A":
            rientro = "No" #Variabile di metodo ed è visibile solo nel metodo
        else:
            rientro = "Si"
        return f"\n\nMi chiamo {self.nome} {self.cognome}.\nLa mia classe è: {self.classe}\nLa mia matricola è: {self.matricola}.\nLe mie ora settimanali sono: {self.ore_settimanali}\nRientro: {rientro}"


#Creo l'istanza della classe
s1 = Studente("Luca","Rossi","3A","MT001") #Creo un istanza della classe studente
s2 = Studente("Mario","Verdi","4A","MT002")

print(f"{s1.nome} {s1.classe}")
print(s2.nome)
print(s1.presentaStudente())
print(s2.presentaStudente())

import random
print(random.randrange(3,15))