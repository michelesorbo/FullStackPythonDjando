"""
Prendere un articolo da wikipedia e salvarlo in una variabile.
Far partire un programma che chieda all'utente di cercare una parola nell'aricolo e ritorni:
- Quante volte è ripetuta la parola nell'articolo
- i primi 50 caratteri dalla prima occorrenza della parola cercata
- se la parola non esiste scrivere "parola non trovata.
L'utente può cercare qualsiasi parola finchè non inserisce 0 e il programma termina con la scritta
"Grazie il programma è terminato"
"""

testo = """
È un linguaggio multi-paradigma che ha tra i principali obiettivi: dinamicità, semplicità e flessibilità. Supporta il paradigma object oriented, la programmazione strutturata e molte caratteristiche di programmazione funzionale e riflessione.

Le caratteristiche più immediatamente riconoscibili di Python sono le variabili non tipizzate e l'uso dell'indentazione per la sintassi delle specifiche, al posto delle più comuni parentesi.

Altre caratteristiche distintive sono l'overloading di operatori e funzioni tramite delegati, la presenza di un ricco assortimento di tipi e funzioni di base e librerie standard, sintassi avanzate quali slicing e list comprehension.

Il controllo dei tipi è forte (strong typing) e viene eseguito in runtime (dynamic typing): una variabile è un contenitore a cui viene associata un'etichetta (il nome) che può essere associata a diversi contenitori anche di tipo diverso durante il suo tempo di vita. Fa parte di Python un sistema garbage collector per liberazione e recupero automatico della memoria di lavoro.

Python ha qualche somiglianza con Perl, ma i suoi progettisti hanno scelto una sintassi più essenziale e uniforme con l'obiettivo di migliorare la leggibilità del codice. Analogamente a Perl è classificato spesso come linguaggio di scripting, ma pur essendo utile per scrivere script di sistema, in alternativa per esempio a bash, la grande quantità di librerie disponibili e la facilità con cui il linguaggio permette di scrivere software modulare favoriscono anche lo sviluppo di applicazioni molto complesse.
Sebbene Python venga in genere considerato un linguaggio interpretato, in realtà il codice sorgente non viene convertito direttamente in linguaggio macchina. Infatti passa prima da una fase di pre-compilazione in bytecode, che viene quasi sempre riutilizzato dopo la prima esecuzione del programma, evitando così di reinterpretare ogni volta il sorgente e migliorando le prestazioni. Inoltre è possibile distribuire programmi Python direttamente in bytecode, saltando totalmente la fase di interpretazione da parte dell'utilizzatore finale e ottenendo programmi Python a sorgente chiuso[3].


Menù a tendina dal quale si può eseguire il programma cliccando su "Run Module" o con lo shortcut F5 da windows 10 in poi.
Come il linguaggio Lisp e a differenza del Perl, l'interprete Python supporta anche un modo d'uso interattivo (REPL) attraverso cui è possibile inserire codice direttamente da un terminale, visualizzando immediatamente il risultato.


Esempio di alcuni codici sorgente scritti con l'IDLE di Python 3.8.5
Inoltre l'interprete Python è contenuto nella libreria standard, perciò come in molti altri linguaggi interpretati è possibile far valutare stringhe arbitrarie nel contesto corrente. È possibile passare all'interprete anche un contesto completamente diverso, sotto forma di liste che contengono l'elenco dei simboli definiti.

Python dispone anche di un framework per lo unit testing che supporta lo sviluppo di test unitari automatici.
Se paragonato ai linguaggi compilati statically typed, come ad esempio il C, la velocità di esecuzione non è uno dei punti di forza di Python[4], specie nel calcolo matematico. Inoltre, il programma si basa unicamente su un core, ed il multi-threading è presente al solo livello astratto. Esisteva un'estensione, Psyco[5], il cui sviluppo è terminato nel 2012, che era una sorta di compilatore JIT, in grado di velocizzare in modo notevole alcuni tipi di codice, specialmente l'implementazione di algoritmi, a scapito dell'aumento di memoria utilizzata. Un progetto attuale e attivamente sviluppato per migliorare le prestazioni del codice Python grazie a un compilatore JIT è PyPy[6].

Python permette di aggirare in modo facile l'ostacolo delle performance pure: è infatti relativamente semplice scrivere un'estensione in C o C++ e poi utilizzarla all'interno di Python, sfruttando così l'elevata velocità di un linguaggio compilato solo nelle parti in cui effettivamente serve e sfruttando invece la potenza e versatilità di Python per tutto il resto del software[7].
"""

print(testo)