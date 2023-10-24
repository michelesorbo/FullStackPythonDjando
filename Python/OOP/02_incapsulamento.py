#Incapsulamento: è la tecnica che rende gli attributi gestibili sono all'interno della classe.
#Per getire gli attibuti privati su usa la tecnica del Getter e Setter. Si creano metodi pubblici per gestire l'inserimento e la visualizzazione degli attributi

#I metodi Getter (abbreviati in get) servono per poter visualizzare il contenuto di un attributo es: 
# def getNome(self): 
#   return self.__nome

#I metodi Setter (abbreviati con set) servono per settare il contenuto dell'attriburo es:
# def setNome(self, nome):
#    self.__nome = nome
class Persona:
    #Creo il costruttore
    def __init__(self,nome,cap) -> None:
        #Gli attributi della classe sono visibili pubblicamente di default
        #Per rendere privato l'attibuto (la variabile self.<nome_variabile>) dopo il self inizio il nome della variabile con _ o __
        self.nome = nome #Pubblic
        self.__cap = cap #Private, cioè lo posso utilizzare solo nella classe

    def __str__(self) -> str:
        return f"Nome: {self.nome} CAP: {self.__cap}"
    #Serve per visualizzare il CAP all'esterno della Classe
    def getCAP(self): 
        return self.__cap
    
    #Per settare un nuovo valore di CAP
    def setCAP(self, nuovo_cap):
        if nuovo_cap.isalpha():
            print("Errore solo numeri")
        else:
            self.__cap = nuovo_cap
    

p1 = Persona("Mario","00100")

print(f"Il nome è: {p1.nome}")
print(f"Il cap è: {p1.getCAP()}")
p1.setCAP("Test")
print(f"Il nuovo CAP è: {p1.getCAP()}")