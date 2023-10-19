""" 
Scrivere un programma che generi un numero casuale compreso tra 1 e 100
e chiedere all'utente di indovinare il numero. 
Quando l'utente inserisce il numero il programma, in caso di errore, dirà se il numero
inserito è maggiore o minore del numero da indovinare.

Quando l'utente indovina il numero il programma dirà "Bravo ha indovinato in <tot> tentativi"
"""
import random #Importo la libreria Random
n_random = random.randint(1,100) # Genero il numero casuale da indovinare

tenttivi = 0 #Ricordo il numero dei tentativi

while True:
    num = int(input("Indovina il numero: "))
    tenttivi += 1 #Incremento i tentativi
    if(num == n_random): #Caso indovinato
        print(f"Bravo hai indovinato in {tenttivi} tentativi")
        break
    elif num > n_random:
        print("Sbagliato il numero insetito è maggiore del numero da indovinare")
    else:
        print("Sbagliato il numero insetito è minore del numero da indovinare")