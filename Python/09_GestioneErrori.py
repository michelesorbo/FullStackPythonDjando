#Link documentazione: https://docs.python.org/3/tutorial/errors.html
""" n1 = input("Inserisci un numero: ")
n2 = input("Inserisci un numero: ")

somma = int(n1) + int(n2) #Se va male il cast si blocca il programma

print(f"La somma è: {somma}") """

#Faccio la stessa cosa ma provo a gestire l'errore

try:
    n1 = input("Inserisci un numero: ")
    n2 = input("Inserisci un numero: ")

    somma = int(n1) + int(n2) #Se va male il cast si blocca il programma
    print("La somma è: " + str(somma)) 

except ValueError:
    print("Attenzione non puoi inserire lettere")
except NameError:
    print("Una o più variabili non sono state dichiarate")
except TypeError:
    print("Puoi stamapre solo stringhe")
except: #L'eccezione generica va sempre messa per ultima eccezzione
    print("Errore generico")
finally: #Finally vine sempre scritta alla fine di tutte le eccezzioni e non è obbligatoria
    print("Finally viene sempre eseguita sia se si va in errore sia che vada tutto bene")



def dividi(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        result = "non posso dividere per 0"
    return result


print(dividi(8,0))


print("Altre operazioni dopo la somma")