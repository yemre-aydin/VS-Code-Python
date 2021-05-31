#region  örnek 1
"""
toplam, sayi=0, 0
while True:
    sayi_girin=int(input("sayı girin çıkmak için -1\t:"))
    if sayi_girin==-1:
        break
    sayi+=1
    if sayi_girin%2==0:
        print("çif sayı girdiniz.")
        continue
    toplam+=sayi_girin

    print("girilen sayiların toplama {0}dir.".format(toplam))
    """
#endregion

#region örnek 2 açıl susam açıl

while True:
    b=input("gizli kelimeyi girin:\t:")
    if b=="susam":
        print("kapı açıldı")
        break
    print("Tekrar deneyiniz.")
    
