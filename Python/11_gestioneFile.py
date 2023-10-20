#Vado ad aprire e scrivere un file un file con Python
#file_txt = open("file_esempio.txt","a")#Nome del file da aprire, modalità di apertura w,r,a
#Modalità di Apertura di un file
#Apertura in modalità r (read) è quella di default. Serve solo per poter leggere un file e non scriverci sopra
#Apertura in modalità w (write). Se il file esiste lo apre altrimenti lo crea e lo apre e sovrascrive il vecchio contenuto
#Apertura in modalità a (append). Se il file esiste lo apre altrimeti lo crea. Se esiste s iposizionerà alla fine del file e continua 
# a scrivere al suo interno. Se voglio andare a capo nel file inserisco \n

"""
Per poter scrivere all'interno di un file dobbiamo aprire il file con i giusti permessi specificati nella funzione open:

    r: apre il file in sola lettura (modalità di default)
    r+: apre i file in lettura e scrittura, il puntatore viene posizionato all'inzio del file.
    w: apre il file in sola scrittura, se il file esiste lo sovrascrive, se non esiste lo crea.
    w+: apre il file in lettura e scrittura, se il file esiste lo sovrascrive, se non esiste lo crea.
    a: apre il file in scrittura senza sovrascrivere il contenuto corrente.
    a+: apre il file in lettura e scrittura senza sovrascrivere il contenuto corrente. Se il file non esiste lo crea.
Quindi come puoi capire non definendo un permesso apriamo automaticamente il file in lettura. Proviamo ad aprire il file in scrittura per l'aggiunta di contenuti (append).

"""


# file_txt.write("\nTi saluto per la quinta volta")#Vado a scrivere sul file
# file_txt.close()#Chiudo il collegamneto con il file DA FARE SEMPRE

#Leggere un file
#file_txt = open("file_esempio.txt", "r")
# contenuto = file_txt.read()
# print(contenuto)

#Voglio leggere le singole righe
#print(file_txt.readlines())

# for line in file_txt.readlines():
#     print(f"Riga: {line}")
# file_txt.close()

#Creo delle funzioni per operare sui file
def scriviSuFile(file_name, testo):
    file_txt = open(file_name, "a")
    file_txt.write('\n')#Creo una nuova riga
    file_txt.write(testo)#Scrivo il tespo passato nel file
    file_txt.close() #chiudo il file

#Funzione per leggere il contenuto del file
def readFile(file_name):
    file_txt = open(file_name, "r")
    contenuto = file_txt.read() #Leggo il contenuto del file e lo salvo nella variabile contenuto
    file_txt.close()#Chiudo il file
    return contenuto #Ritorno il contenuto del file

def ricercaFile(file_name, cerca):
    file_txt = open(file_name, "r")
    conenuto = ""

    for line in file_txt.readlines():
        if line.lower().count(cerca.lower()) > 0:
            conenuto += line
    
    return conenuto

url_file = "File/file_esempio.txt"

scriviSuFile(url_file,"Scrivo tramite la funzione per la seconda volta")
print(ricercaFile(url_file, "funzione"))

#Aprire un file sia un lettura che in una modalità di scrittura
# file_txt = open("file_esempio.txt", "a")
# testo = '\n'
# testo += input("Cosa vuoi aggiungere: ")
# #Scrivo sul file
# file_txt.write(testo)
# #Dopo aver scritto alla fine del file per stampare devo spostare il puntatore all'inizio del file con seek(0)
# file_txt.seek(0)
# for line in file_txt.readlines:
#     print(f"Riga: {line}")

