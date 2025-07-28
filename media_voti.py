# esercizio con media aritmetica dei voti, con l'utilizzo di ciclo while e operatore logico and

print("MEDIA VOTI")
somma=0
i=0
voto=int(input("Inserisci un voto: "))

if voto>=0:
    while voto>=18 and voto<=30:
        somma+=voto
        i=i+1
        voto=int(input("Inserisci un voto (18-30, -1 per terminare): "))
    print("Media dei voti:", float(somma)/i)
else:
    print("Voto non valido. Inserisci un voto compreso tra 18 e 30.",)









  


