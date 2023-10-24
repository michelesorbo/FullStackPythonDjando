"""
Creare una classe Auto con i seguenti attributi
- Marca
- Modello
- Anno di costruzione

Creare un costruttore, le variabili dovranno essere tutte private.
Generare i get e setter di tutte le variabili e il metodo costruttore e toString.

Il set dell'anno deve verificare che l'anno inserito sia numerico e di lunghezza 4
"""

class Auto:
    def __init__(self, marca, modello, anno) -> None:
        self.__marca = marca
        self.__modello = modello
        #self.__anno = anno
        self.setAnno(anno)
    
    def __str__(self) -> str:
        return f"Dati Auto:\nMarca: {self.__marca}\nModello: {self.__modello}\nAnno: {self.__anno}"
    
    #Genero Get e Set per le variabili
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca = marca

    def getModello(self):
        return self.__modello
    
    def setModello(self, modello):
        self.__modello = modello
    
    def getAnno(self):
        return self.__anno
    
    def setAnno(self, anno):
        if anno > 3 and anno < 5:
            self.__anno = anno
        else:
            return "Anno non valido"



#Dopo la classe
a1 = Auto("Ford","Mustang",1979)
a2 = Auto("AUDI","A3",19785)
print(a1)
print(a2)
print(f"La marca è: {a1.getMarca()}")
a1.setMarca("AUDI")
print(f"La marca è: {a1.getMarca()}")

a1.setAnno("Ciao")
print(f"Anno {a1.getAnno()}")