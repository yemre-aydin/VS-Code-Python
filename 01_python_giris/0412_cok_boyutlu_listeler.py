#region cok boyutlu listeler matrisler
"""
matris yapıları oluşturma
veri tabanı mimarisine benzer satır sütun yapıları oluşturma


a=[[1,2,3,4],[5,6,7,8]]
print(a)
"""
#endregion

"""
Örn. kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Desktop_Test    %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe
"""
kurumCihazlari=[
    [1,"Desktop_Test",56,"chrome.exe"],
    [2,"Guest101",60,"excel.exe"],
    [3,"Kat-1_Laptop",90,"camtasia.exe, chrome.exe"]]
for i in range(len(kurumCihazlari)):
    for j in range(len(kurumCihazlari[i])):
        print(kurumCihazlari[i][j],end="  ")
    print("")

"""
ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]

for i in ogrenciler : 
    print(i[0],i[1],end="  ")
    ortalama=(i[2]+i[3])/2
    if ortalama>50:
        print(f"geçtiniz.ortalamanız:{ortalama}")
    else:
        print(f"kaldınız.ortalamanız:{ortalama}")
"""



