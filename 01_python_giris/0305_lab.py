
secim=input('uygulamadan çıkmak için "ç"')
i=1

ort=0
while secim !="ç":
    vize=int(input(f"{i}. öğrencinin vize notunu girin:"))
    final=int(input(f"{i}. öğrencinin final notunu girin:"))
    i+=1
    secim=input('uygulamadan çıkmak için "ç"')
    ort+=(vize+final)/2
print(i)
genelort=ort/(i-1)    
print(genelort)
"""
i,j=0,0
while i<4:
    whilej<4:
    """




    

