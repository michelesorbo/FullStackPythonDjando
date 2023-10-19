#In Python non esistono gli operatori di incremeto e decremento e non esiste il 
#do while

#Stampare i primi 10 numeri

n = 1 #Indice di partenza

while n <= 10:
    print(n)
    n += 1 #Non posso usare l'operatore incremento quindi si fa n += 1

#Sommare dei numeri finche non si inserisce 0, 
# al termine mostrare la somma e quanti numeri sono staiti inseriti

# somma = 0
# num = int(input("Inserisci un numero, 0 per terminare: "))
# conta_numeri = 0 #Metto 0 così non conto il numero 0 quando viene iserito

# while num != 0:
#     somma += num
#     conta_numeri += 1
#     num = int(input("Inserisci un numero, 0 per terminare: "))

# print(f"La somma dei numeri inseriti è: {somma}, e i numeri inseriti sono {conta_numeri}")

#Per sostituire i do while, quindi far eseguire almeno una volta il ciclo si usa il loop infinito
#e l'istruzione breack per terminare
# somma = 0
# conta_numeri = 0
# #Creo il ciclo infinito
# while True:
#     num = int(input("Inserisci un numero, 0 per terminare: "))
#     if(num == 0): #Controllo l'uscita dal loop infinito
#         break
#     somma += num
#     conta_numeri += 1

# print(f"La somma dei numeri inseriti è: {somma}, e i numeri inseriti sono {conta_numeri}")

#Generare un numero random
#Per poter generare un numero random ci serve la libreria random
#Per richedere una libreria si unsa import <nome_loberia>
import random
n_random = random.randint(1,10) #Uso la libreria random per generare un numero compreso tra 1 e 10 e assegnarlo alla variabile n_random
print(f"Numero randomg generato: {n_random}")

