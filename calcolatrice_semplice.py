# semplice esercizio di calcolatrice in Python

print("CALCOLATRICE SEMPLICE")

n1=int(input("Inserisci il primo numero: "))
n2=int(input("Inserisci il secondo numero: "))

somma=n1+n2
sottrazione=n1-n2
moltiplicazione=n1*n2
divisione=n1/n2

print("Scegli l'operazione da eseguire:")

operazione=input("1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\n")
                 
if operazione == "1":
    print("Il risultato della somma è:", somma)
elif operazione == "2":
    print("Il risultato della sottrazione è:", sottrazione)
elif operazione == "3":
    print("Il risultato della moltiplicazione è:", moltiplicazione)
elif operazione == "4":
    if n2 != 0:
        print("Il risultato della divisione è:", divisione)
    else:
        print("Errore: Divisione per zero non permessa.")
else:
    print("Operazione non valida. Per favore, scegli un numero tra 1 e 4.")

print("Grazie per aver usato la calcolatrice semplice!")



