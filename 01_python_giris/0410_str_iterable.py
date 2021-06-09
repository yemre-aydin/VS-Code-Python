"""
e → 1
o → 2
a → 1
i → 1
"""


kurum ="ecodation"

liste=["a","e","o","ö","ı","i","u","ü"]

for i in liste:
    if i in kurum:
        print(f"{i} -> {kurum.count(i)}")
        
