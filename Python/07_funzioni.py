#Servono a scrivere dei blocchi di codice riutilizzabili

#Per dichiarare una funzione = def nome_funzione(eventuali_parametri):
def saluta():
    print("Ciao Mondo")
    print("Sono python")

#Per chiamre (Invocare) una funzione bisogna scrivere il nome_della_funzione()
saluta()
saluta()
saluta()
saluta()

#Una funzione può ricevere parametri
def salutaNome(nome):
    print(f"Ciao da {nome}")

salutaNome("Alessio")
nome = "Carlo"
salutaNome(nome)

#Funzioni che hanno un ritorno
def somma(n1,n2):
    return n1+n2

print(somma(4,7))

somma = somma(6,78)
print(somma)

#Creaiamo una funzione per stapare gli elementi di un array

def arToStr(ar):
    testo = ""
    for el in ar:
        testo += f"{el} "
    return testo

ar = [1,4,3,6,7]
ar_2 = ['Michele','Silvia','Stefania']

print(arToStr(ar_2))

#Funzione per formattare una stringa
def pulisciStringa(testo):
    testo = testo.strip()
    testo = testo.replace(",", "")
    testo = testo.replace(".", "")
    testo = testo.replace("  ", " ")
    testo = testo.lower()
    return testo

parola = "   Ciao da PYthon  "
print(pulisciStringa(parola))

#Funzioni con parametri di Default
def preparaPrimo(tipo_pasta = 'rigatoni', sugo = True):
    print(f"La pasta scelta è: {tipo_pasta}")
    if sugo:
        print("Preparo anche il sugo")
    else:
        print("Pasta in bianco")

preparaPrimo()
preparaPrimo("Penne", False)
preparaPrimo("Tortellini")

def patente(eta, nazionalita):
    if eta >= 18 and nazionalita == "Italia":
        print("Puoi guidare")
    else:
        print("non puoi guidare")

#Invocare una funzione con KeyArguments
patente(nazionalita="Italia", eta=22)

#Funzioni con parametri variabili
def sommaNumeri(*numeri):
    somma = 0
    for el in numeri:
        somma += el
    return somma

print(sommaNumeri(2,5))
print(sommaNumeri(4,5,8,98,78))
print(sommaNumeri(2,5,98,34,2,34,5,76,8,9,45))

def operazioniMultiple(operando, *numeri):
    risultato = 0

    if operando == '+':
        for el in numeri:
            risultato += el
    elif operando == '-':
        for el in numeri:
            risultato -= el
    elif operando == '*' or operando == 'x':
        risultato = 1
        for el in numeri:
            risultato *= el
    elif operando == '/' or operando == ':':
        if numeri.count(0) > 0:
            print("Non posso dividere con 0")
            risultato = "Impossibile"
        else:
            for el in numeri:
                risultato /= el
    else: 
        print("Operazione non consentita")

    return f"Operazione {operando} Risultato: {risultato}"

print(operazioniMultiple("/", 3,6,7,23,5))
print(operazioniMultiple("+", 46,7,23,5,89))
print(operazioniMultiple("*", 46,7,23,5,89))
print(operazioniMultiple("-", 46,7,23,5,89))
print(operazioniMultiple("/", 3,6,7,23,0))