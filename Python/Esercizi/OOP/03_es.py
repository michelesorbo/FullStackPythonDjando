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