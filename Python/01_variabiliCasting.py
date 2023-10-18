#Per creare una variabile bisogna solo dichiare il nome
nome = "Mario" #Variabile di tipo stringa

#Per stampare a temrinale il risultato uso print()
print(type(nome)) #type serve a conosce la tipologia della variabile

#i tipi interi sono tutti i numeri naturali es -1, 0, 1, 3
#i tipi float sono tutti in umri con la , (in informatica la vigola per iniziare i decimali viene sostituita dal .)
numero = 5.4
print(type(numero))

bolean = True
print(type(bolean))

#Dichiarazione dell'array
ar = ["roma","napoli","milano",12, [12,"cioa"] ]
print(type(ar))

tupla = ("roma", "milano","napoli")
print(type(tupla))

dizionario = {
    "nome":"Mario",
    "cognome":"Rossi",
    "eta": 60
}
print(type(dizionario))

#CASTING sono int() str() float()
n1 = 3
n2 = "5"
n3 = "3.7"
#Cast per sommare. Trasformo n2 in intero
print(n1 + int(n2))

#Voglio concatenare. Trasfomo n1 in stringa
print(n2 + str(n1))

print(float(n3))