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
    corpo_studentesco = 0 #Mi serve per vedere quante volte ho istanziato la classe stundente

    #Prorietà della classe, con il metodo costruttore della classe
    #Il metodo costruttore è il primo metodo chiamato appena si istanzia la calsse
    def __init__(self, nome, cognome, classe, matricola):
        #Vado a definire gli attributi della classe
        self.nome = nome #self.nome è una variabile di istanza (visibile e utilizzabile da tutta la classe e da tutte le istanze). Sono diverse per le varie istanze
        self.cognome = cognome
        self.classe = classe
        self.matricola = matricola
        Studente.corpo_studentesco += 1 #Ogni volta che creo un nuovo studente la variabile viene incrementata di 1
    
    #per evitare di far stampare la posizione della memoria quando si stamapa solo l'istanza, creo il motodo toString che stampa la classe come stringa
    def __str__(self):
        return f"Sono lo studnete {self.nome} {self.cognome}"
    
    #Dichiaro il metodo presentaStudente.
    def presentaStudente(self):
        if self.classe == "3A":
            rientro = "No" #Variabile di metodo ed è visibile solo nel metodo
        else:
            rientro = "Si"
        return f"\n\nMi chiamo {self.nome} {self.cognome}.\nLa mia classe è: {self.classe}\nLa mia matricola è: {self.matricola}.\nLe mie ora settimanali sono: {self.ore_settimanali}\nRientro: {rientro}"

class Scuola:
    def __init__(self, nomeScuola):
        self.nome = nomeScuola
        self.studenti = []

    def __str__(self):
        return f"Il nome della scuola è: {self.nome}"

    def aggiungiStudente(self, studente): #il metodo accetterà oggetti della classe studente come parametro
        self.studenti.append(studente)
    
    def studentiScuola(self):
        for st in self.studenti:
            print(st.presentaStudente())


#Creo l'istanza della classe
istituto = Scuola("A. Manzoni")
s1 = Studente("Luca","Rossi","3A","MT001") #Creo un istanza della classe studente
s2 = Studente("Mario","Verdi","4A","MT002")
s3 = Studente("Giuseppe", "Verdi", "3A", "MT003")

istituto.aggiungiStudente(s1)
istituto.aggiungiStudente(s2)

istituto.studentiScuola()

# print(f"{s1.nome} {s1.classe}")
# print(s2)
# print(s1.presentaStudente())
# print(s2.presentaStudente())

# print(f"Il numero totale di stundeti creati è: {Studente.corpo_studentesco}")

# import random
# print(random.randrange(3,15))