# Calcolo nuovo orario partendo da un orario iniziale e sommandolo in secondi inseriti in input dall'utente

print("CALCOLO NUOVO ORARIO")

i=0

h=-10
while h<0 or h>23:
    h=int(input("Inserire ora (0-23): "))
                
m=-10
while m<0 or m>59:
    m=int(input("Inserire minuti (0-59): "))

s=-10
while s<0 or s>59:
    s=int(input("Inserire secondi (0-59): "))

s2=int(input("Inserire secondi da sommare: "))      # si da per inteso che il valore sia positivo e pertanto non ho inserito un controllo

print("Orario iniziale:", h, ":", m, ":", s)

# Calcolo del nuovo orario

h_diff=s2//3600         
m_diff=(s2%3600)//60
s_diff=s2%60

# queste 3 stampe servono per verificare i calcoli vengano eseguiti correttamente, una volta verificati si possono commentare per non visualizzarli nel programma

print(h_diff)
print(m_diff)
print(s_diff)

s+=s_diff
m_diff+=s//60
s%=60

m+=m_diff
h_diff+=m//60
m%=60

h+=h_diff
if h>23:
    i=h//24
    h%=24

if i>0:
    giorno= ("giorno +" +str(i))
else:
    giorno=""

print("Il nuovo orario è: ",h, ":", m, ":", s, giorno)

# fine del programma
       