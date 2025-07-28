# in questo esercizio trovo il maggiore tra tre numeri con uguaglianza sfruttando strutture decisionali

a=int(input("Inserisci il primo numero: "))
b=int(input("Inserisci il secondo numero: "))
c=int(input("Inserisci il terzo numero: "))
if a>b:
    if a>c:
        print("Il maggiore è: ", a)
    elif a<c:
        print("Il maggiore è: ", c)
    else:
        print("I numeri sono uguali", a)
elif b>a:
    if b>c:
        print("Il maggiore è: ", b)
    elif b<c:
        print("Il maggiore è: ", c)
    else:
        print("I numeri sono uguali", a)
else:
    print("I numeri sono uguali" ,a,b,c)


# fine esercizio