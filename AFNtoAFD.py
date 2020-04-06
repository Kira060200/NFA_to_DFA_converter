f=open("data.in")
g=open("data.out","w")
a=[['0' for x in range(100)] for y in range(100)] #matricea initiala a relatiilor
b=[['0' for x in range(100)] for y in range(100)] #matricea finala a AFD-ului obtinut
def lexicographic_sort(s):
    return sorted(sorted(s), key=str.upper)
nr=int(f.readline())
#v=[int(x) for x in f.readline().split()]
#print(ord('c')-ord('a'))
maxim_st=0;
maxim_lit=0;
for i in range(nr):
    x = f.readline().split()
    if int(x[0])>maxim_st:
        maxim_st=int(x[0])
    if int(x[1])>maxim_st:
        maxim_st=int(x[1])
    if ord(x[2])-ord('a')+1>maxim_lit:
        maxim_lit=ord(x[2])-ord('a')+1
    a[int(x[0])][ord(x[2])-ord('a')+1]=x[1]+(str(a[int(x[0])][ord(x[2])-ord('a')+1]) if str(a[int(x[0])][ord(x[2])-ord('a')+1])!='0' else '')
start=int(f.readline())
final=[]
for x in f.readline().split():
    final.append(int(x))
for i in range(1,maxim_st+1):
    for j in range(1,maxim_lit+1):
        a[i][j]=''.join(sorted(str(a[i][j])))
        print(a[i][j],end=' ')
    print('')
print(start)
print(final)
parcurs=[] #vector in care retinem nodurile prin care am trecut
b[1][1]=a[1][1]
b[1][2]=a[1][2]
parcurs.append(a[1][1])
parcurs.append(a[1][2])
poz=0   #variabila cu care determin litera de legatura din alfabet
for x in parcurs:
    curent=''
    if len(x)>1:
        ind=0
        while(ind<len(x)):
            if a[int(x[ind])][poz % maxim_lit+1]!='0' and a[int(x[ind])][poz % maxim_lit+1] not in curent:
                curent=curent+a[int(x[ind])][poz % maxim_lit]
            ind+=1
        curent=''.join(sorted(curent))
    elif a[int(x)][poz % maxim_lit+1]!='0':
        curent=a[int(x)][poz % maxim_lit+1]
    #print(curent,int(x),poz % maxim_lit+1)
    if curent!='' and curent not in parcurs:
        parcurs.append(curent)
    poz+=1
print(parcurs)


#for i in range(1,maxim_st+1):
    #for j in range(1,maxim_lit+1):