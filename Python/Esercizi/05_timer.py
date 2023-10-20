"""
Creare un software che chiede di quanti secondi deve essere il timer
Dopo che l'untete inserisci i secondi far partire il timer a video con la scritta
"Mancano <secondi> alla fine del timer"

Controllare che non ci siano errori bloccanti al codice con i try esception


--Modifica successiva anche da fare dopo il corso o nel fine settimana
Chedere Ore, minuti e secondi per settare la durata del timer.
Ricorda che timer.sleep() accetta solo secondi
es:
->Inserisci le ore: 2
->Inserisci i minuti: 20
->Inserisci i secondi: 10

mancano 2:20:09
mancano 2:20:08
mancano 2:20:07
mancano 2:20:06
...
mancano 2:10:09
....
mancano 0:00:01
FINE TIMER
"""
import time
from datetime import timedelta
#Soluzione prime metodo
try:
    secondi_es1 = int(input("inserisci i secondi: "))
    for n in range(secondi_es1,0,-1):
        print(f"Mancano {n} alla fine")
        time.sleep(1)
        if n == 1:
            print("Fine Timer")
except ValueError:
    print("Puoi inserire solo numeri")


#Timedelta trasforma i secondi in ore minuti e secondi
print(f"3600 secondi in ore minut secondi {timedelta(seconds=3600)}")