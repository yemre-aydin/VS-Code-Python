var kullanicilar=[
    {email:"engindemirog@gmail.com",sifre:"12345"},
    {email:"derindemirog@gmial.com",sifre:"12345"}
]
var tivitler=[
    {email:"engindemirog@gmail.com",tivit:"bugün hava çok güzel"},
    {email:"engindemirog@gmail.com",tivit:"bugün hava çok güzel 2"},
    {email:"derindemirog@gmail.com",tivit:"Kapıyı ben açacağım"},
]
var email= prompt("email?")
var sifre=prompt("sifre?")
console.log("çalışıyor")
 function kullaniciVarmi(email,sifre){
     for(i=0;kullanicilar.length;i++){
         if(kullanicilar[i]==email && kullanicilar[i].sifre==sifre){
             return true;
         }
     }
     return false;
 }


function giris(){
    console.log(email);
    console.log(sifre);

    if(kullaniciVarmi(email,sifre)){
        console.log(tivitler)    
    }else{
        console.log("Kullanıcı adı veya şifre hatalı")
    }
}
