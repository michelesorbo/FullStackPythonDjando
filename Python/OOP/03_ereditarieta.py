"""

Personale Scolastico:

Insegnati: Nome, Cognome, eta, Materia Insegnata
Studenti: Nome, Cognome, eta, Classe
Personale di Segreteria: Nome, Coognome, eta, ruolo
Bidelli: Nome, Cognome, eta, ala di competenza

Vado ad accorpare le caratteristiche comuni mnella classe Persona: Nome cognome ed eta

"""

#Vado a creare la classe Padre
class Persona:
    def __init__(self, nome, cognome,eta) -> None:
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    def __str__(self) -> str:
        return f"Nome: {self.nome} Cognome: {self.cognome} eta: {self.eta}"
    
    def sauta(self):
        return f"Ciao da {self.nome} {self.cognome}"
    
class Studente(Persona):
    #Riscrivo il costruttore inserendo i campi specifici dello studente
    def __init__(self, nome, cognome, eta, classe) -> None:
        super().__init__(nome, cognome, eta) #Vado a prendere il costruttore di mio padre
        self.classe = classe #Inizializzo la mia proprietà

    def getClasse(self):
        return self.classe
    #OverLoad di un metodo. Sovrascivo un metodo ereditato da mio padre
    def sauta(self):
        return f"Ciao sono lo studente {self.nome} {self.cognome}"
    

class Insegnante(Persona):
    def __init__(self, nome, cognome, eta, *materie):
        super().__init__(nome, cognome, eta)
        self.materie = materie #Materie è un array quindi self.materie è a sua volta un array
    
    def sauta(self):
        return f"Buongiorno sono l'insegnante {self.nome} {self.cognome}"
    
    def getMaterie(self):
        materie = "Materie inegnate: "
        
        for m in self.materie:
            materie += f"{m}, "

        return materie
    
class Segreteria(Persona):
    def __init__(self, nome, cognome, eta, ruolo) -> None:
        super().__init__(nome, cognome, eta)
        self.ruolo = ruolo

    def salutoMio(self):
        return f"Mio saluto + Persona {super().sauta()}"

p1 = Persona("Luca","Verdi",25)
ins1 = Insegnante("Giovanni", "Marrone",46,"Matematica","Fisica")
ins2 = Insegnante("Veronica","De Rossi", 43,"Italiano","Storia","Geografia")
s1 = Studente("Mario","Rossi",15, "3A")
sg1 = Segreteria("Luisa","Bianchi",54,"Applicato")

print(f"{ins1} Materie: {ins1.getMaterie()}")
print(f"{ins2} Materie: {ins2.getMaterie()}")
