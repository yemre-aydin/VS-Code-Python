#region örnek 4
"""
Ad-Soyad Giriniz, Çıkmak İçin -1   : Doğanay Bil
Doğanay Bil 1.snv Notu : 60
Doğanay Bil 2.snv Notu : 90
Ad-Soyad Giriniz, Çıkmak İçin -1   : Elif Aslan
Doğanay Bil 1.snv Notu : 60
Doğanay Bil 2.snv Notu : 80
Ad-Soyad Giriniz, Çıkmak İçin -1   : Dilara Özmen
Doğanay Bil 1.snv Notu : 80
Doğanay Bil 2.snv Notu : 80
Öğrenci Ortlama Listesi:
============
75.0
70.0
80.0
Min → 70
Mak → 80
"""
ortalamalar =[]
while True:
    ad =input("Ad,Soyad giriniz, çıkmak için -1 :")
    if ad=="-1":
        break
    s1=int(input(f"{ad} 1.sınav notu giriniz: "))
    s2=int(input(f"{ad} 2.sınav notu giriniz: "))
    ort=(s1+s2)/2
    ortalamalar.append(ort)
for i in ortalamalar:
    print(i)
    
print(f"maksimum not -> {max(ortalamalar)}")
print(f"minimum  not -> {min(ortalamalar)}")





#endregion 
#region 