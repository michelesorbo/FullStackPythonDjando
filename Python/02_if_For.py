#Per prendere un input da tastiera uso input()

# nome = input("inserisci il tuo nome: ")
# print("Hai inserito: " + nome)
# #Input ritorna stringa
# n1 = input("Inserisci il primo numero: ")
# n2 = float(input("inserisci il secondo numero: ")) #n2 sarà sempre int e se inserisco una lettera si blocca qui
# print(float(n1)+n2) #Se n1 non è un numero il programma si blocca qui per il cast

#IF
#Controllo se sei maggiorenne
eta = 30
if eta >= 18:
    print("Sei maggiorenne")
    print("Puoi guidare")
else:
    print("Sei minorenne")
    #scrivo ancora la condizione else
#sono fuori dalla condizione
paese = "Italia"
if eta >= 20:
    print("sei maggiorenne")
    if paese == "Italia":
        print("Puoi guidare")
    else:
        print("Non puoi guidare")
else:
    print("Sei minorenne")

#Usiamo gli operatori logici and && e or ||
if eta >= 18 and paese == "Italia":
    print("puoi guidare")
else:
    print("non puoi guidare")


#Troviamo l'utente
utente = "carlo"

if utente == "carlo":
    print("Ciao Amministratore")
elif utente == "mirko":
    print("Ciao Grafico")
elif utente == "Fabio":
    print("Ciao Utente")
else:
    print("non ti conosco")

#FOR
#range(stop) Parte da 0 e si ferma allo stop escluso
#range(start, stop) parte da start incluso e si ferma a stop escluso
#range(start, stop, incremento) posso decidere come deve incrementare

#Stampare i primi 10 muneri
for n in range(1, 20, 4):
    print(n)

for pippo in range(10, -1, -1):
    print(pippo)

#Come leggere un array
numeri = [5,9,6,85] #Fare la somma dei numeri nell'array?
somma = 0
for el in numeri:
    somma += el
    print(el)

print(f"La somma dei numeri è: {somma}") #tipo backtic

