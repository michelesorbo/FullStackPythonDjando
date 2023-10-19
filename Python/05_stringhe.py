#Pagina principale
#Rif https://www.w3schools.com/python/python_ref_string.asp

testo = "ciao dal corso di python, python è il linguaggio del momento"

#IMPOTANTE le stringhe sono array di caratteri
print(testo[1])

#per conoscere la lunghezza di una stringa uso il metodo len(stringa da contare)
print(f"La lunghezza del testo è {len(testo)}")

#Restituisce il numeri di volte che il termine cercato è presente nella stringa. count è case sensitive
#rif: https://www.w3schools.com/python/ref_string_count.asp
print(f"La parola 'Python' compare {testo.count('python')} volte")

#Trasformare solo la prima lettere di una stringa in maiuscolo
#rif: https://www.w3schools.com/python/ref_string_capitalize.asp
print(f"Tresformo solo la prima lettera in maiuscolo: {testo.capitalize()}")

#Trasformare tutte le iniziali delle parole in MAIUSCOLO
#rif: https://www.w3schools.com/python/ref_string_title.asp
print(f"Tutte le iniziali in Maiuscolo: {testo.title()}")

#Trasformare tutta la stringa in MAIUSCOLO
#rif: https://www.w3schools.com/python/ref_string_upper.asp
print(f"Tutta la stringa in maiuscolo: {testo.upper()}")

#Trasformare tutta la stringa in minuscolo
#rif: https://www.w3schools.com/python/ref_string_lower.asp
print(f"Tutta la stringa in minuscolo: {testo.lower()}")

#Per modificare il testo in una stringa
#rif: https://www.w3schools.com/python/ref_string_replace.asp
print(f"Cambio parola python con JavaScript: {testo.replace('python','JavaScript')}")

#Per eliminare gli spazzi prima e dopo la stringa
#Rif: https://www.w3schools.com/python/ref_string_strip.asp
testo1 = "    Ciao    "
print(f"Con spazzi: {testo1} dopo testo")
print(f"Senza spazzi: {testo1.strip()} dopo testo") 
print(f"Senza spazzi a sinistra: {testo1.lstrip()} dopo testo") 
print(f"Senza spazzi a destra: {testo1.rstrip()} dopo testo") 

testo2 = ",,,,..-,tk,,Ciao, sono tk e sto. nel centro...,,"
print(f"Senza vigole iniziali: {testo2.strip(',.-tk')}")


#Per trasformare una stringa in un array
#Rif: https://www.w3schools.com/python/ref_string_split.asp
testo3 = "benvenuti nel corso di python"
ar_testo3 = testo3.split() #Se non specifico nulla di default è lo spazzio
print(f"Array testo3: {ar_testo3}")

testo3_a = "#python#developer#corso"
ar_testo3a = testo3_a.split('#',2)
print(f"Array testo3_a: {ar_testo3a}")

#Splitto con la nuova linea
#Rif: https://www.w3schools.com/python/ref_string_splitlines.asp
testo4 = "Benvenuto.\nIn questo paragrafo parliamo di Python.\nPython è un linguaggio molto versatile."
print(testo4)
ar_testo4 = testo4.splitlines()
print(f"Array da split line: {ar_testo4}")

#Trovare l'indice di inizio della parola cercata
#Rif: https://www.w3schools.com/python/ref_string_rindex.asp
testo5 = "Mi casa, su casa"
print(f"Indice inizio della prima occorrenza di casa {testo5.index('casa')}")
print(f"Indice inizio dell'ultima occorrenza di casa {testo5.rindex('casa')}")

#Come verificare se il contenuto di una stringa è di tipo numerico o stringa o float
testo6 = "1221"
print(f"Il tipo del testo6 è: {type(testo6)}")
print(f"Il contenuto del testo6 è numerico?: {testo6.isnumeric()}")

#Vedere se è alfanumerico isalnum()
#Rifhttps://www.w3schools.com/python/ref_string_isalnum.asp

#Vedere se è solo caratteri e non numeri isalpha()
#https://www.w3schools.com/python/ref_string_isalpha.asp
nome = "Carlo II"
print(f"Il campo nome contiene solo caratteri?: {nome.isalpha()}")