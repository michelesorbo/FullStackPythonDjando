#Link documentazione ufficiale: https://docs.python.org/3/library/array.html#module-array

#Creare un array (lista)
ar_numri = [12,34,5,34] #Array di numeri
print(type(ar_numri))

#Stamapre il contenuto dell'array
print(ar_numri)
#Se voglio stampare i singoli elemnti dell'array
for el in ar_numri:
    print(el)

ar_testo = ["Mario","Luigi","Giuseppe"] #Array testuale
ar_misto = [12,True,"Ciao",[1,"Hello"]] #Array Misto
print(ar_misto[3][1])

#Funzioni Liste di Python
ar = [1,3,5,67,8,6,45,6,78,6,4,34,23,6,8,23,5,43,9,87,8]
#Conoscere la lunghezza di un array
print(f"Nell'array ar ci sono {len(ar)} elementi")
#Stampare solo una parte dell'array
print(ar[4:12]) #Stampo dall'inidce 4 fino all'indice 12 escluso
print(ar[4:]) #Stampo dall'indice 4 fino alla fine
print(ar[:4])#Stampo dall'inizio fino all'indice 4 escluso
print(ar[-4:]) #Stampo gli ultimi 4 elementi dell'array


#Ordinare una Lista per poterlo fare la lista deve avere gli elementi dello stesso tipo
#Rif: https://www.w3schools.com/python/ref_list_sort.asp
ar_1 = [2,4,6,1]
#sort() ordina in modo crescente sort(reverse=True) ordina in modo decrescente
ar_1.sort(reverse=True) #Ordino l'array in modo crescente
print(f"Stampo ar_1 ordinato: {ar_1}")

ar_1a = ["Mirko", "Alessio", "Carlo", "12","2"]
ar_1a.sort()
print(f"Stampo ar_1a ordinato: {ar_1a}")

#Come capovolgere gli elementi di un array senza ordinarli
ar_1b = ["Mario","Giuseppe","Luigi"]
ar_1b.reverse()
print(f"Il reverse di ar_1b è: {ar_1b}")


#Come aggiungere elemnti ad una lista
#Metodo append, inserisce l'elemento alla fine della lista Rif: https://www.w3schools.com/python/ref_list_append.asp
ar_2 = ['mele', 'fragole', 'pere']
ar_2.append('limone')
print(f"Stampo ar_2 {ar_2}")

#Metodo insert(<indice>, <elemento>) permette di inserire un elemento ad un determinato indice. In automatico verranno ricalcolati gli indici dell'array
ar_2.insert(1,'banane')
print(f"Stampo ar_2 {ar_2}")

#Come rimuovere elementi da una lista
#Il metodo pop() se non viene specificato l'indice elimina sempre l'ultimo elemento della lista.
#Se specifico l'indice es: ar.pop(2) elieminerà l'elemento all'indice 2
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.pop(1)
print(f"Stampo array Fruits {fruits}")

#Come eliminare un elemento tramite il contenuto e non l'indice
fruits2 = ['apple', 'banana', 'cherry', 'orange', 'banana']
fruits2.remove('banana') #Elimina la prima occorrenza della stringa cercata
print(f"Stampo array Fruit2 {fruits2}")

#Come svuotare una lista
fruits2.clear()
print(f"Stampo array Fruit2 dopo il metodo clear {fruits2}")

#come contare il numero di elementi uguali presenti in una lista
alunni = ["Mirko", "Carlo", "Alessio","Carlo","Ludmila","Carlo"]
print(f"Alunni con il nome Carlo: {alunni.count('Carlo')}")

#Copiare una lista
numeri = [12,4,3,65,1]
numeri_copia = numeri.copy() #Creo una copia della lista numeri
numeri.sort()
print(f"I numeri ordinati sono {numeri} e la disposizione originale era {numeri_copia}")

#Come unire due liste (estendere)
numeri_2 = [2,"Michele",True]
numeri.extend(numeri_2)
print(f"La lista numeri estesa è: {numeri}")

#Come trovare l'indice di un elemento nella lista. Index('elemento') ritorna sempre l'indice della prima occorrenza trovata
ar_3 = ['ananas','apple', 'banana', 'cherry','apple']
print(f"L'indice dell'elemento 'apple' è: {ar_3.index('apple')}")