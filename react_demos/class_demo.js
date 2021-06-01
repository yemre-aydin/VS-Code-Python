class Personel{
    constructor(ad,soyad){
       this.ad;
       this.soyad;     
    }

    kaydet(){
        console.log('Personel Kaydedildi :'+this.ad);
    }
}

const personel=new Personel("Engin","Demirog")//classlarda direk clası yazamayız değişken oluşturup onun içine çağırırız

personel.kaydet();
 personel.ad="Engin"
 console.log(personel.ad);
