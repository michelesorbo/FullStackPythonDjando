""" 
Esercizio 3
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
Un array “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
La classe dovrà avere i seguenti metodi:
Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”. (il metodo__str__ che stampa le informazioni del 
prodotto è sempre da fare) 
Creare i metodi aumenta e diminuisco scarte per i prodotti. 
Creare il metodo applicaSconto(self, percentualeSconto) per i prodotti.
es applicaSconto(4) applicherà uno sconto al prezzo del prodotto del 4%.

es:
Costo magazzino è di 1€ per prodotto
Nel magazzino metto Palloni calcio, scorta 5
Palloni bascket socrta 15
Palloni PallaVole 10

Costo toate del meagazzino al mese è = (Scorta palloni calcio * costo Magazzino) + (Scorta palloni bascket * costo Magazzino) +
(Scorta palloni PallaVolo * costo Magazzino) => (5 * 1) + (15 * 1) + (10 * 1) = 30€ mensili

Creo Prodotto PalloneCalcio = "Adidas plus", 15, 10
se applico il metodo Sconto del 50% il nuovo prezzo sarà 7,5

"""
class Prodotto:
    def __init__(self, nome, prezzo,scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

    def __str__(self):
        return f"Prodotto: {self.nome}, prezzo: {self.prezzo}€, quantità in magazzino {self.scorta}"
    
    def applicaSconto(self,sconto):
        self.prezzo = (self.prezzo * (100-sconto))/100
    
    def aumentaScorta(self, qta):
        self.scorta += qta

    def diminuisciScorta(self, qta):
        self.scorta -= qta

#Soluzione con Dizionario  
# class GestoreMagazzino:
#     def __init__(self, costo_magazzino):
#         self.prodotti = {}
#         self.costo_magazzino = costo_magazzino

#     def aggiungi_prodotto(self, prodotto):
#         self.prodotti[prodotto.nome] = prodotto

#     def rimuovi_prodotto(self, nome_prodotto):
#         self.prodotti.pop(nome_prodotto)

#     def calcola_costi_magazzino(self):
#         costi = 0
#         for nome,prodotto in self.prodotti.items():
#             costi += prodotto.scorta * self.costo_magazzino
#         return costi
            
#Soluzione con le liste
class GestoreMagazzino:
    def __init__(self, costo_magazzino):
        self.prodotti = [] #Array vuoto per ricordare i prodotti inseriti nel magazzino
        self.costo_magazzino = costo_magazzino

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def prodotti_in_magazzino(self):
        prodotti_m = ""
        
        for prodotto in self.prodotti:
            prodotti_m += f"\n{prodotto}"
        
        return prodotti_m

    def rimuovi_prodotto(self, nome_prodotto):
        self.prodotti.remove(nome_prodotto)

    def calcola_costi_magazzino(self):
        costi = 0
        for prodotto in self.prodotti:
            costi += prodotto.scorta * self.costo_magazzino
        return costi

p1 = Prodotto("Telefono",500,10)
p2 = Prodotto("MacBook Pro M2", 4000, 5)
p3 = Prodotto("Monitor",120,50)

mz1 = GestoreMagazzino(15)

mz1.aggiungi_prodotto(p1)
mz1.aggiungi_prodotto(p2)
mz1.aggiungi_prodotto(p3)
print(f"Il magazziono ha un costo di {mz1.calcola_costi_magazzino()}€ e ci sono {mz1.prodotti_in_magazzino()} prodotti")