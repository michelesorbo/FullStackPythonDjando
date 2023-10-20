"""
Scrivere un programma che crei un file chiamato "rubrica.txt"
Chieda all'utente le seguenti opzioni:
1) Inserisci nuovo contatto
2) Cerca Contatto
3) Visualizza tutti i contatti
4) Chiudi programma

Quando si scegli 1 il programma chiederà:
->Nome contatto:
->Cognome contatto:
->Telefono contatto:
Dopo far apparire un messaggio di conferma di inserimento e ritornare al menù principale
Il programma verifica se il contatto inserito è già presente

Quando si sceglie 2 il programma chiederà:
->Inserisci o il nome o il congome o il numero da cercare
il programma mostra quanti contatti ha trovato e il dettaglio dei contatti e poi il menù pricipale

Quando si sceglie 3:
il programma mostrerà tutti i contatti e il numero totale dei contatti in rubrica

Quando si sceglie 4:
Il programma saluta e si chiude
"""

def scriviSuFile(file_name):
    file_txt = open(file_name, "a")
    nome = input("Nome contatto: ")
    cognome = input("Cogome contatto: ")
    tel = input("Telefono contatto: ")
    if ricercaFile(file_name, f"{nome.lower()} {cognome.lower()} {tel}")['contatti'] > 0:
        print("Contatto già presente")
    else:
        file_txt.write(f"{nome.lower()} {cognome.lower()} {tel}\n")#Scrivo il tespo passato nel file
        print("Contatto Inserito Correttamente")
    file_txt.close() #chiudo il file

#Funzione per leggere il contenuto del file
def readFile(file_name):
    file_txt = open(file_name, "r")
    i = 0
    for line in file_txt.readlines():
        print(line)
        i += 1
    print(f"Contatti totali: {i}")


def ricercaFile(file_name, cerca):
    file_txt = open(file_name, "r")
    contenuto = "" #Serve per ricordare le righe trovate
    i = 0 #Contatore di contatti trovati
    for line in file_txt.readlines():
        if line.lower().count(cerca.lower()) > 0:
            contenuto += line
            i += 1
    return {"contenuto":contenuto, "contatti":i}

file_name = "File/rubrica.txt"

while True:
    scleta = input("MENU PRINCIPARLE\n1) Inserisci nuovo contatto\n2) Cerca Contatto\n3) Visualizza tutti i contatti\n4) Chiudi programma\n")

    if scleta == '1':
        scriviSuFile(file_name)
    elif scleta == '2':
        cerca = input("Inserisci o il nome o il congome o il numero da cercare: ")
        risultato = ricercaFile(file_name, cerca)
        print(risultato['contenuto'])
        print(f"Contatti totali: {risultato['contatti']} ")
    elif scleta == '3':
        readFile(file_name)
    elif scleta == '4':
        print("Grazie...programma chiuso")
        break
    else:
        print("Operazione non valida. Scegli una delle operazioni del menu")