var kullanicilar=[
    {email:"engindemirog@gmail.com",sifre:"12345"},
    {email:"derindemirog@gmial.com",sifre:"12345"}
]
var tivitler=[
    {email:"engindemirog@gmail.com",tivit:"bugün hava çok güzel"},
    {email:"engindemirog@gmail.com",tivit:"bugün hava çok güzel 2"},
    {email:"derindemirog@gmail.com",tivit:"Kapıyı ben açacağım"},
]
prompt("email?")
var sifre=prompt("sifre?")
 if((email==kullanicilar[0].email && sifre==kullanicilar[0].sifre)||
    (email==kullanicilar[1].email && sifre==kullanicilar[1].sifre)){
        console.log(tivitler)    
    }else{
        console.log("Kullanıcı adı veya şifre hatalı")
    }

/*
function giris(){
    if((email==kullanicilar[0].email && sifre==kullanicilar[0].sifre)||
    (email==kullanicilar[1].email && sifre==kullanicilar[1].sifre)){
        console.log(tivitler)    
    }else{
        console.log("Kullanıcı adı veya şifre hatalı")
    }
}
giris(email,sifre)
*/