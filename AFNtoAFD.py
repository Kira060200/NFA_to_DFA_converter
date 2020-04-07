f=open("data.in")
g=open("data.out","w")
a=[['0' for x in range(100)] for y in range(100)] #matricea initiala a relatiilor
b=[['0' for x in range(100)] for y in range(100)] #matricea finala a AFD-ului obtinut
def lexicographic_sort(s):
    return sorted(sorted(s), key=str.upper)
nr=int(f.readline())
#v=[int(x) for x in f.readline().split()]
#print(ord('c')-ord('a'))
maxim_st=0; #numarul maxim de stari
maxim_lit=0;    #numarul maxim de litere
for i in range(nr):
    x = f.readline().split()
    if int(x[0])>maxim_st:
        maxim_st=int(x[0])
    if int(x[1])>maxim_st:
        maxim_st=int(x[1])
    if ord(x[2])-ord('a')+1>maxim_lit:
        maxim_lit=ord(x[2])-ord('a')+1
    a[int(x[0])][ord(x[2])-ord('a')+1]=x[1]+(str(a[int(x[0])][ord(x[2])-ord('a')+1]) if str(a[int(x[0])][ord(x[2])-ord('a')+1])!='0' else '')
start=int(f.readline()) #starea initiala
final=[]    #starile finale
for x in f.readline().split():
    final.append(int(x))
for i in range(1,maxim_st+1):   #decomentati liniile de printare pentru a vedea cum este construita matricea initiala a relatiilor
    for j in range(1,maxim_lit+1):
        a[i][j]=''.join(sorted(str(a[i][j])))
        #print(a[i][j],end=' ')
    #print('')
#print(start)
#print(final)
parcurs=[] #vector in care retinem nodurile prin care am trecut
b[1][1]=a[start][1]
b[1][2]=a[start][2]
parcurs.append(a[start][1])
parcurs.append(a[start][2])
poz=0   #variabila cu care determin litera de legatura din alfabet
indice=1    #indice de linie in noua matrice a relatiilor
b[indice][1]=a[1][1]
b[indice][2]=a[1][2]
indice+=1
for x in parcurs:
    poz=0   #litera de legatura
    while poz<maxim_lit:
        curent = ''
        if len(x)>1:
            ind=0
            while(ind<len(x)):
                for j in range(len(str(a[int(x[ind])][poz % maxim_lit+1]))):
                    if a[int(x[ind])][poz % maxim_lit+1][j]!='0' and a[int(x[ind])][poz % maxim_lit+1][j] not in curent:
                        curent=curent+a[int(x[ind])][poz % maxim_lit+1][j]
                ind+=1
            curent=''.join(sorted(curent))
        elif a[int(x)][poz % maxim_lit+1]!='0':
            curent=a[int(x)][poz % maxim_lit+1]
        if curent!='':
            b[indice][poz % maxim_lit + 1]=curent
        if curent!='' and curent not in parcurs:
            parcurs.append(curent)
        poz+=1
    indice+=1
#afiseaza matricea finala a relatiilor
for i in range(1,len(parcurs)+2):
    for j in range(1,maxim_lit+1):
        print(b[i][j],end=' ')
    print()
def verify(x):  #verifica daca starea obtinuta x este finala sau nu
    for k in final:
        for l in range(len(x)):
            if k == int(x[l]):
                return 1
    return 0
parcurs.insert(0,str(start))    #adaug si starea din care am inceput parcurgerea
print("AFD-ul obtinut este:")
for i in range(1,len(parcurs)+1):
    for j in range(1,maxim_lit+1):
        if b[i][j]!='0':
            print(parcurs[i-1],b[i][j],chr(j-1+ord('a')))
print("Stari finale:",end='')
for x in parcurs:
    if verify(x):
        print(x,end=' ')