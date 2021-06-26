#region 

"""
+ yazıTura()
.random değere göre -> "yazı" - "tura" return 
. while True içinde sonsuz döngü içinde yazı için "y",
tura için 't', çıkmak içim 'ç'
her döngü de skor ekrana yazılacak 
"""

def yazıTura():
    import random
    if random.randint(1,2)==1:
        return "yazı"
    else:
        return "tura"

def skorBoard():
    print(f"Skorda son durum -> {oSkor}-{bSkor}")

def skorKontrol(o,b):
    if o>=5:
        return "kazanan Oyuncudur"
    elif b>=5:
        return "kazana Pc"

oSkor,bSkor=0,0


while True:
    skorBoard(oSkor,bSkor)
    sec = input("yazı için 'y', tura için 't', çıkmak için 'ç'")
    if sec.lower()=="ç":
        break
    if sec =="y":
        if yazıTura()== "yazı":
            oSkor +=1
        else:
            bSkor+=1
    elif sec== "t":
        if yazıTura()=="t":
            oSkor+=1
        else:
            bSkor+=1
    else:
        print("Hatalı Seçim")
        continue
    if not skorKontrol(oSkor,bSkor)==None:
        print(skorKontrol(oSkor,bSkor))
        break

"""doğrusu


def yazıTura():
    import random
    if random.randint(1, 2) == 1:
        return "yazı"
    else:
        return "tura"


def skorBoard(o, b):
    print(f"Skorda Son Durum → Oyuncu Skor : {o} - PC Skor : {b}")

def skorKontrol(o, b):
    if o>=5:
        return "kazanan oyuncudur"
    elif b>=5:
        return "kazanan pc"

oSkor, bSkor = 0, 0
while True:
    skorBoard(oSkor, bSkor)
    sec = input("yazı için 'y', tura için 't', çıkmak için 'ç'")
    if sec.lower() == "ç":
        break
    if sec == "y":
        if yazıTura() == "yazı":
            oSkor += 1
        else:
            bSkor += 1
    elif sec == "t":
        if yazıTura() == "t":
            oSkor += 1
        else:
            bSkor += 1
    else:
        print("Hatalı Seçim")
        continue

"""




#endregion