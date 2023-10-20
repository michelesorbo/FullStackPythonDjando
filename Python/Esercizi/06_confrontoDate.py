"""
Chiedere due date da tastiera, le date dovranno essere inserite nel formato gg/mm/aaaa
passare i parametri alla funzione datetime e dire quale data è maggiore
"""
from datetime import datetime

data1 = input("Inserisci la data nel formato gg/mm/aaaa: ")
data2 = input("Inserisci la data nel formato gg/mm/aaaa: ")

#Trasformo le date da stringhe ad array es gg/mm/aaaa
data1_ar = data1.strip().split('/')
data2_ar = data2.strip().split('/')

print(data1_ar)

#Provo a trasformare le date da array in formato date. Per farlo faccio il cast del contunto degli array
try:
    d1 = datetime(int(data1_ar[2]), int(data1_ar[1]), int(data1_ar[0])) #Anno mese giorno
    d2 = datetime(int(data2_ar[2]), int(data2_ar[1]), int(data2_ar[0])) #Anno mese giorno

    if d1 > d2:
        print(f"La data {data1} è successiva alla data {data2}")
    elif d2 > d1:
        print(f"La data {data2} è successiva alla data {data1}")
    else:
        print("La date sono uguali")
except ValueError:
    print("Puoi inserire solo formati di data gg/mm/aaaa")
except Exception as e:
    print(f"Errore: {e}")