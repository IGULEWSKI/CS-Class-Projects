from math import gcd,sqrt
#może się zdarzyć że nawet jak e jest w tablicy to wyrzuci błąd o nieprawidłowym e pokombinuj coś z tym (naprawione chyba)
#p i q musi być pierwsze i różne
pliktek=open("wiadomość do zaszyfrowania.txt", encoding="utf-8")
plikzasz=open("zaszyfrowana wiadomość.txt", encoding="utf-8")


def prime(a):
    if a<2:
        return 0
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return 0
    return 1


def znajdz_e(p,q):#Funkcja oddająca tablice z możliwymi e
    tab=[]
    t=(p-1)*(q-1)
    for i in range(13,t):
        guard=True
        o=t//i
        r=t%i
        if r!=0:
            o2=i//r
            r2=i%r
            if r2!=1:
                guard=False
            elif r2!=0:
                if r//r2==1:
                    guard=False
        if i>1 and t%(o)!=0 and gcd(i,t)==1 and guard==True and i//r!=1 and i%r!=0 and r%o2!=0:
            tab.append(i)
    return tab

def RSA(p,q,e):
    if e not in znajdz_e(p,q):
        return 'Błąd podano nieprawidłowy klucz e'
    N=p*q
    t=(p-1)*(q-1)
    #krok Pierwszy Algorytm Euklidesa
    a=t
    b=e
    guard=True
    l=0
    while True:
        l+=1
        o=a//b # ile razy można zmieścić a w b
        r=a%b
        #print(a,b,o,r)
        if guard==True:# po to żeby tylko za pierwszym razem
            o1=o
            guard=False
        if r==1 or o==1:
            x=o
            y=r
            break
    #krok drugi
        a=b
        b=r
    d=o1*o+1
    tab=[(e,N),(d,N)]
    return tab

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

print(f"""Szyfr RSA
Podaj dwie róźne liczby pierwsze:""")
p=int(input())
q=int(input())
if p==q:
    print("Podano te same liczby")
elif prime(p)==0 or prime(q)==0:
    print("Podane liczby nie są pierwsze")
else:
    if len(znajdz_e(p,q))<1:
        print("Dla podanych liczb pierwszych nie ma klucza e")
    else:
        print(znajdz_e(p,q))
        e=int(input("Wybierz jeden z kluczy e w tablicy: "))
        if e in znajdz_e(p,q):
            RSA(p,q,e)
            print("""Co zrobić?
1. Wyświetlić klucz prywatny i publiczny
2. Zaszyfrować wpisaną wiadomość przy pomocy klucza publicznego
3. Odszyfrować wpisaną wiadomość przy pomocy klucza prywatnego
4. Zaszyfrować wiadomość z pliku przy pomocy klucza publicznego
5. Odszyfrować wiadomość z pliku przy pomocy klucza prywatnego""")

            wybor=int(input())
            if wybor==1:
                print("Klucz Publczny",RSA(p,q,e)[0])
                print("Klucz Prywatny",RSA(p,q,e)[1])
                print("Pierwsza wartość to klucz a druga to iloczyn cyfr pierwszych")
            elif wybor==2:
                tekst=str(input("Podaj tekst do zaszyfrowania: "))
                print(Szyfr(RSA(p,q,e)[0][0],RSA(p,q,e)[0][1],tekst))
            elif wybor==3:
                zasz=str(input("Podaj tekst do odszyfrowania: "))
                print(Deszyfr(RSA(p,q,e)[1][0],RSA(p,q,e)[1][1],zasz))
            elif wybor==4:
                tekst=pliktek.read()
                print(Szyfr(RSA(p,q,e)[0][0],RSA(p,q,e)[0][1],tekst))
            elif wybor==5:
                zasz=plikzasz.read()
                print(Deszyfr(RSA(p,q,e)[1][0],RSA(p,q,e)[1][1],zasz))
            else:
                print("Podaj cyfre od 1 do 5")
        else:
            print("Podanego klucza e nie ma w tablicy")





#aby zapisać klucz publiczny trzeba zarówno wziąść wartość (e,N) a prywatny (d,N)
