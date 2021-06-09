
"""
liste=[i for i in range(1,9)]
print(liste)

row=["piyon" for i in range(1,9)]
print(row)
"""

"""
haftaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
Haftanin 1. Günü Pazartesi, Haftanin 2. Günü Salı ....
inline for 

haftaninGünleri = ["pazartesi" , "salı" , "çarşamba" , "perşembe" , "cuma" , "cumartesi", "pazar"]
liste = [f"haftanın {i}. günü → {haftaninGünleri[i-1]}"  for i in range(1,8) if i<3]
print(liste)
"""
liste=[]
while True:
    fav=input("cıkmak için -1 favori ay\t=")
    if fav =="-1":
        break   
    
    if fav in liste:
        print("daha önce eklediniz")
    else:
        liste.append(fav)
    
print(liste)
