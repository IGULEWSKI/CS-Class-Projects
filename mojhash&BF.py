haslo='pass1'
def hashin(nap,prim=31):
    hash=0
    for el in nap:
        hash=(hash*prim+ord(el))%1111111111111111111
    return hex(hash)
tab=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def lamhash(hash,le=1,lhash=''):#le is length of password
    if hashin(lhash)==hash:
        print(f"Access Granted hasło: {lhash}")
    if le==len(lhash):
        pass
    else:
        for el in tab:
            lamhash(hash,le,lhash+el)
def lamhash2(hash,le):#le is max length of password
    for i in range(1,le+1):
        lamhash(hash,i)
#Brute force works but hash has problem that multiple password may have same hash
print(hashin(haslo))
lamhash2(hashin(haslo),5)



