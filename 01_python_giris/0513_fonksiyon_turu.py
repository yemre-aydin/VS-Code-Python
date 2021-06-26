

"""
fonksiyon tanımlama anında argüman alır, 

"""
"""
def mDeger(a):
    if str(a).isdigit:
    if a<0:
        a*=-1
    return a

print(mDeger(10))
print(mDeger("on"))
"""
"""
def ciftMİ(a):
    if a%2 ==0:
        return True

print(ciftMİ(14))
"""
"""
sonuc()
s1, s2 değerleri alınacak
digit kont.
s1 s2 den büyük ise çıkarma
s1 s2 den küçük ise toplama
eşit ise eşitlik dönecek
"""

def sonuc():
    s1=input("1.sayı girin:")
    s2=input("2.sayı girin:")
    if s1.isdigit() and s2.isdigit():
        s1,s2 =int(s1),int(s2)
        if s1>s2 :
            return s1-s2
        elif s2>s1:
            return s1+s2
        else:
            return s1,s2
    else:
        return "String deger giremez"
    

print(sonuc())



    
