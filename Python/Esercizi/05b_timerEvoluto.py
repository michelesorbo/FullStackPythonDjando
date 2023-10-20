from datetime import timedelta
import time

total_time = 0 #Imposto il valore di default
try:
    ore = int(input("Inserisci le ore: "))
    minuti_ins = int(input("inserisci i minuti, compresi tra 1 e 60, se sbagli verrà inserito 0: "))
    secondi_ins = int(input("inserisci i secondi, compresi tra 1 e 60, se sbagli verrà inserito 0: "))
    minuti = minuti_ins if minuti_ins > 0 and minuti_ins <61 else 0 #Operatore ternario
    secondi = secondi_ins if secondi_ins > 0 and secondi_ins <61 else 0 #Operatore ternario

    total_time = secondi + (minuti * 60) + (ore * 60 * 60)
    print(f"{total_time}")
    print(f"Da secondi a ore minuti secondi {timedelta(seconds=total_time)}")
except ValueError:
    print("Solo numeri")

#Funzione timer
def startTimer(secondi):
    for n in range(secondi,0,-1):
        print(f"Mancano {timedelta(seconds=n)}")
        time.sleep(1)
        if(n == 1):
            print("FINE TIMER")

startTimer(total_time)