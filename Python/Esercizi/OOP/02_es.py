""" 
Esercizio 2
Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”.
Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% se non specificato altrimenti aumento lo stipendio
della percentuale specificata
e il metodo __str__ che stampi tutti i dettagli dell’impiegato, 
ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”. 
"""

class Impiegato:
    #1° cpsa da fare è il costruttore
    def __init__(self, nome,cognome,matricola,stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    #2° non oblbigatoria è definire il metodo __str__ così da evitare la stampa della posizione dell'oggetto in memoria
    def __str__(self):
        return f"Sono l'impiegato {self.nome} {self.cognome} con matricola {self.matricola}"

    def getStimepndio(self):
        return self.stipendio
    
    def aumenta_stipendio(self,aumento=10):
        self.stipendio = (self.stipendio * (100+aumento))/100
    

i1 = Impiegato("Mario","Rossi","MT001",2300)
i2 = Impiegato("Luca","Verdi","MT002",1700)

print(i1)
print(f"Stipendio impiegato 1 {i1.getStimepndio()}")
i1.aumenta_stipendio(22)
print(f"Stipendio impiegato 1 dopo aumento {i1.getStimepndio()}")

print(i2)
print(f"Stipendio impiegato 2 {i2.getStimepndio()}")
i2.aumenta_stipendio()
print(f"Stipendio impiegato 2 dopo aumento {i2.getStimepndio()}")