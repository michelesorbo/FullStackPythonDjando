#rif: https://www.w3schools.com/python/python_dictionaries.asp

dizionario = {
    "marca" : "Ford",
    "modello" : "Mustang",
    "anno" : 1964
}

#Stampo il dizionario
print(dizionario)

mio_diz = {
    "nome" : "Mario",
    "cognome": "Rossi",
    "eta" : 52,
    "citta": "Milano",
    "linguaggi" : ["JAVA", "Python", "C++"],
    "interessi":{
        "musica":["Rock", "Blues", "Grange"],
        "sport":["calcio","nuoto","tennis"]
    }
}

print(mio_diz)

#Stampo solo le key del dizionario
print(mio_diz.keys())

#Stampo solo i valori del dizionario
print(mio_diz.values())

print("\n\n")
#Stampo le coppie key value
print(mio_diz.items())

#Stampo il valore di una key
print(f"Valore nome nel dizionario {mio_diz['nome']}")
print(f"Stampo con metodo get: {mio_diz.get('cognome')}")

#verificare se nel dizionario è presente la key desiderata
if 'residenza' in mio_diz:
    print(f"Key presente e il valore è: {mio_diz['nome']}")
else:
    print("key non presente")

#Modificare e Aggiungere una key nel dizionario

#1° Metodo bracket
mio_diz["nome"] = "Giuseppe"
print(mio_diz)

#2° Metodo è .update Vine utilizzato anche per aggiungere nuove coppie key value ai dizionari
mio_diz.update({"via" : "via Roma, 12"})
print(mio_diz)
print(mio_diz.get('pizza','Chiave non presente')) #Ritorna il valore della chiave se è presente altrimenti torna il seocndo parametro

#Eliminare un elemento da un dizionario passadogli la key
mio_diz.pop('eta')
print(mio_diz)

del mio_diz["cognome"]
print(mio_diz)

#Per svuotare il dizionario si usa clear
dizionario.clear()
print(dizionario)

#Per stamapre sia le key che i valori di un dizionario si usa un for con 2 indici
for k,v in mio_diz.items():
    print(f"Key: {k} : Value: {v}")

#Per creare una copia di un dizionario
copia_diz = dict(mio_diz)
print(copia_diz)

#Nasted Dictionary
alunni = {
    "alunno1":{
        "nome":"Giuseppe",
        "cognome":"Verdi"
    },
    "alunno2":{
        "nome":"Mario",
        "eta":42
    },
    "alunno3":{
        "cognome": "Rossi",
        "citta":"Modena"
    }
}

print(alunni['alunno1'])

#Altrnativa
alunno1 = {
    "nome" : "Silvia",
    "cognome" : "Drea"
}

alunno2 = {
    "nome" : "Enza",
    "cognome" : "Macrì"
}

mia_classe = {
    "alunno1":alunno1,
    "alunno2":alunno2
}