# realizzazione di una tavola pitagorica 

print("TAVOLA PITAGORICA")
print("")

N=int(input("Inserisci un numero: "))
print("*", end="\t")

for i in range (1,N+1):
    print(i, end="\t")
print("")

for i in range (1,N*9):
    print("-", end="")
print("")

for i in range (1,N+1):
    print(i, end="\t|")
    for j in range (1,N+1):
        print(i*j, end="\t")
    print("")








      
