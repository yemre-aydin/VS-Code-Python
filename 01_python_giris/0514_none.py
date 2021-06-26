

a=None
print (id(a))
def mDeger(a):
    if a<0:
        a*=-1
    return a
print(mDeger(10))
a=10
print(10)
print(id(a))


def birlestir() :
    ad1= input("lütfen ad giriniz. ")
    soyad1= input("lütfen soyad giriniz.")
    return f"{ad1.title()} {soyad1.title()}"

print(birlestir())

