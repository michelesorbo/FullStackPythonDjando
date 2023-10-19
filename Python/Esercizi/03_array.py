#Es1: Creare una lista che contenga 5 numeri presi random compresi tra 1 e 10, tutti diversi
import random
ar_random = [] #Creo Array vuoto

while len(ar_random) < 5:
    n = random.randint(1,10) #Estraggo il numero casuale
    if ar_random.count(n) == 0: #Se il count del numero estratto è 0 significa che non ci sono numeri uguali
        ar_random.append(n)
print(f"Arry random con numeri diverisi {ar_random}")

#Es2: Chiedere di inserire numeri finchè non si inserisce 0.
#Dividere i numeriin due liste, una contenente i numeri pari e una contenente i numeri dispari.
#Visualizzare un errore se il numero inseirto è gia stato inserito in precedenza

ar_pari = []
ar_dispari = []

while True:
    num = int(input("Inserisci un numero. 0 per terminare: "))
    #Cotrollo se il numero è pare e non è presente nell'array pari
    if num == 0: #Controllo se inserisce 0 per terminare
        break #Termino il ciclo while
    else:
        if num%2 == 0 and ar_pari.count(num) == 0:
            ar_pari.append(num)
        elif num%2 == 1 and ar_dispari.count(num) == 0:
            ar_dispari.append(num)
        else:
            print("Numero già inserito, prova un numero nuovo.")
    
print(f"Numeri pari inseirti {ar_pari}")
print(f"Numeri dispari inseirti {ar_dispari}")