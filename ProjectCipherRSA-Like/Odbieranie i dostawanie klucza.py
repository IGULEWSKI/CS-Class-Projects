klucz=(61, 299) #klucz należy wpisać tu

tekst='Ą_::xt' #Tutaj wpisujemy tekst zaszyfrowany lub do zaszyfrowania

def Szyfr(e,N,tekst):
    zasz=''
    for i in range(len(tekst)):
        c=chr((ord(tekst[i])**e)%N)
        zasz+=c
    return zasz

def Deszyfr(d,N,zasz):
    dezasz=''
    for i in range(len(zasz)):
        n=chr((ord(zasz[i])**d)%N)
        dezasz+=n
    return dezasz
print("""1. Używasz klucza publicznego
2. Używasz klucza prywatnego
3. Użyj wiadomości w pliku""")
wybor=int(input())

if wybor==1:
    print(Szyfr(klucz[0],klucz[1],tekst))
elif wybor==2:
    print(Deszyfr(klucz[0],klucz[1],tekst))
elif wybor==3:
    plik=open("zaszyfrowana wiadomość.txt", encoding="utf-8")
    tekst=plik.read()
    print(Deszyfr(klucz[0],klucz[1],tekst))
else:
    print("Trzeba podać liczbę 1 lub 2 lub 3")


