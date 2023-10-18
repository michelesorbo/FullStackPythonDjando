#Es1 Chiedere un numero e dire se è pari o dispari

""" numero = int(input("Inserisci un numero: "))

if numero%2 == 0:
    print("Pari")
else:
    print("Dispari") """

#Es2 Far stamapre a video questa figura
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	

#Es3 Chiedere un numero e se è negativo trasformalo in positivo

""" num_es3 = int(input("Dammi un numero: "))

if num_es3 < 0:
    print(-num_es3)
else:
    print(num_es3) """

#Es4 Chiedere 5 muneri da tastiera e stamparne la somma solo se i numeri sono positivi 

somma = 0
controllo = True
for n in range(5):
    num_es4 = int(input("Inserisci un numero: "))

    if num_es4 >= 0:
        somma += num_es4
    else:
        controllo = False

if controllo == True:
    print(f"La somma è: {somma}")
else:
    print("non posso stamapre il risultato")