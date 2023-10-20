#1° Metodo 
from datetime import datetime, date, timedelta
import time

data_corrente = date.today() #La data verrà stampata in formato americano "Anno - Mese - Giorno"
print(data_corrente)

print(f"Anno: {data_corrente.year}") 
print(f"Mese: {data_corrente.month}")
print(f"Giorno: {data_corrente.day}")

data_corrente_completa = datetime.now()
print(f"Stampo la da completa: {data_corrente_completa}")

#Fomrattare la data secondo lo standard Italiano
data_italiana = data_corrente_completa.strftime("Oggi è %A %d %B %Y  e sono le %H:%M")
print(f"Data in formato italiano: {data_italiana}")

#Tutte le opzioni di strftime: https://www.programiz.com/python-programming/datetime/strftime

#Creazione di un timer
# for n in range(10,0,-1):
#     print(f"Mancano {n} secondi")
#     time.sleep(1) #Significa attendi 1 secondo e poi riprendi


#Confronto tra date
mia_data = datetime(2020,10,21)
data_oggi = datetime.now()

if data_oggi > mia_data:
    print("La data è passata")
else:
    print("La data è futura")

giorni_passati = (data_oggi - mia_data).total_seconds()

print(timedelta(seconds=giorni_passati))
