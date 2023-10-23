"""
Creare una classe ccCorrente in grado di simulare un cc corrente reale, 
quindi con versamenti, prelievi, stampa saldo e dammi la lista degli ultimi 5 movimenti.
Costruttore: Saldo iniziale, Proprietario, N° cc

Fare tutto su un solo correntista

Far partire una schermata con le opzioni es:
Benvenuto nel tuo cc
1) Versa
2) Preleva
3) Saldo Attuale
4) Ultimi 5 movimenti (Da fare con l'array ATTENZIONE SOLO ULTIMI 5 MOVIMENTI)
5) Info cc (Restituisce Proprietario e N° cc da fare con il metodo __str__)
0) Esci

"""
class ContoCorrente:
    def __init__(self, saldo_iniziale, proprietrio, n_cc) -> None:
        self.saldo = saldo_iniziale
        self.proprietario = proprietrio
        self.n_cc = n_cc
        self.movimenti = [] #Ricordo i movimenti del cc

    def __str__(self) -> str:
        return f"Proprietario: {self.proprietario}. N° cc: {self.n_cc}"

    def versa(self, importo):
        self.saldo += importo
        movimento = f"Versato {importo}"
        self.movimenticc(movimento)
    
    def preleva(self,importo):
        self.saldo -= importo
        movimento = f"Prelevato {importo}"
        self.movimenticc(movimento)

    def getSaldo(self):
        return self.saldo
    
    def movimenticc(self, movimento):
        if len(self.movimenti) > 4:
            self.movimenti.pop(0) #Elimino il movimento più vecchio
            self.movimenti.append(movimento) #Inserisco il nuovo movimento alla fine della lista
        else:
            self.movimenti.append(movimento)

    def stampaMovimenti(self):
        for m in self.movimenti:
            print(m)


cc = ContoCorrente(15000,"Luca Rossi", "CC001")


while True:
    print("\nBenvenuto nel tuo cc")
    print("1) Versa")
    print("2) Preleva")
    print("3) Saldo Attuale")
    print("4) Ultimi 5 movimenti")
    print("5) Info ContoCorrente")
    print("0) Esci")

    scelta = input("Inserisci il numero dell'opzione desiderata: ")

    if scelta == "1":
        importo = float(input("Inserisci l'importo da versare: "))
        cc.versa(importo)
    elif scelta == "2":
        importo = float(input("Inserisci l'importo da prelevare: "))
        cc.preleva(importo)
    elif scelta == "3":
        print(cc.getSaldo())
    elif scelta == "4":
       cc.stampaMovimenti()
    elif scelta == "5":
        print(cc)
    elif scelta == "0":
        print("Grazie per aver utilizzato il servizio.")
        break
    else:
        print("Scelta non valida. Riprova.")