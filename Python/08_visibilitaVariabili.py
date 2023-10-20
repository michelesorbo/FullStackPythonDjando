x = 3 #è una x globale del file .py
global nome #Global viene messo in automatico alle variabili create fuori dalle funzioni

def esempio():
    x = 5 #è una x visibile solo nella funzione
    print(f"X nella funzione {x}") 

esempio() #Valore di x nella funzione

print(f"X fuori dalla funzione {x}") #Valore di x nel print

print("Funzione con x Globale")
def esempio2():
    global x #Faccio riferimento alla x dichiarata alla linea 1
    x += 2

esempio2()

print(f"Valore della x dopo la funzione con global x {x}")

def esempio3(x):
    x += 10
    print(x)

#Ora la mia x globale vale 5
esempio3(x)
print(f"Valore di x fouri dalla funzione 3 {x}")

somma = 0 #La rendo globale e visibile a tutti i costrutti if, else, elif, e while sotto di me

while True:
    num = int(input("Inserisi numero, 0 termina: "))

    if num == 0:
        break
    else:
        somma += num

def stampaSomma():
    pippo = "Ciao da pippo" #Visibile solo nella funzione
    #global somma #Se la funzione è scritta nello stesso file della varibile viene fatta in automatico, 
    #sempre se non dichiaro una variabile dello stesso nome all'interno della funzione
    print(f"La somma è: {somma}")

stampaSomma()
#print(pippo) #Mi da errore perchè voglio stampare una variabile creata nella funzione e di conseguenza non visibile globalmente