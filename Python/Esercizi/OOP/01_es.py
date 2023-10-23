""" 
Esercizio 1
Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”, se non è presente nell'elenco "Non conosco la specie".
Creare sempre il metodo per stampare la classe come stringa ( def __str__(self): )

"""

class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
    
    def __str__(self):
        return f"Sono {self.nome} e sono un {self.specie}"

    def emetti_suono(self):
        if self.specie == "gatto":
            return "Miao!"
        elif self.specie == "cane":
            return "Bau!"
        else:
            return "Non conosco la specie"

cane1 = Animale("Fido", "cane")
gatto1 = Animale("Fuffy", "gatto")

print(f"{gatto1} il mio verso è {gatto1.emetti_suono()}")
print(gatto1.emetti_suono())
print(cane1.emetti_suono())