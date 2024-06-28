import os

class Musteri():

    def __init__(self,ad_soyad,tc,sifre):
        self.ad_soyad=ad_soyad
        self.tc=tc
        self.sifre=sifre
        self.bakiye=0


class Banka():
    def __init__(self):
        self.musteriler=list()

    def musteri_ol(self, ad_soyad, tc,sifre):
        self.musteriler.append(Musteri(ad_soyad,tc,sifre))
        print("Hoş geldiniz! Müşterimiz olmak istediğiniz için sizi tebrik ederim!")

banka = Banka()

menu= "Ana menüye dönmek için Enter'a basınız."
while True:
    os.system("cls")
    print("""
        Şevin Bankasına Hoş Geldiniz!
        
        1) Müşteriyim
        2) Müşteri Olmak İstiyorum
        Q) Çıkış
    """)

    secim= input("Seçim yapınız: ")

    if secim=="1":
        girilen_tc = input("TC no: ")
        tc_nolar = [a.tc for a in banka.musteriler]
        if girilen_tc in tc_nolar:
            for musteri in banka.musteriler:
                if girilen_tc==musteri.tc:
                    girilen_sifre = input("Şifreniz: ")
                    if girilen_sifre == musteri.sifre:
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("""
                                Hoş Geldiniz Sayın {}
                                
                            1) Bakiye Sorgulama
                            2) Para Yatır
                            3) Para Transfer Et
                            4) Para Çek
                            Q) Çıkış
                            """.format(musteri.ad_soyad))
                            secim2= input("İşlem numarasını giriniz: ")

                            if secim2=="1":
                                print("Bakiyeniz: {}".format(musteri.bakiye))
                                input(menu)

                            elif secim2=="2":
                                yatirilan_tutar= int(input("Miktar: "))
                                onay= input("Kendi hesabınıza {} TL para yatırmayı onaylıyor musunuz? (E/H) :".format(yatirilan_tutar))
                                if onay== "e" or onay=="E":
                                    musteri.bakiye += yatirilan_tutar
                                    print("Paranız yatırıldı.")
                                    input(menu)
                                elif onay=="h" or onay=="H":
                                    print("İşleminiz iptal edildi")
                                    input(menu)
                                else:
                                    print("Hatalı seçim yaptınız")
                                    input(menu)

                            elif secim2=="3":
                                hedef_tc = input("Para göndermek istediğiniz hesabın TC numarası:")
                                if hedef_tc in tc_nolar:
                                    for transfer in banka.musteriler:
                                        if hedef_tc == transfer.tc:
                                            hedef_ad_soyad = input("Ad Soyad: ")
                                            if hedef_ad_soyad == transfer.ad_soyad:
                                                yollanacak_para= int(input("Göndereceğiniz para miktarı: "))
                                                if yollanacak_para<=musteri.bakiye:
                                                    onay = input("{} adlı kişiye {} TL göndermeyi onaylıyor musunuz? (E/H) : ".format(transfer.ad_soyad,yollanacak_para))
                                                    if onay=="e" or onay=="E":
                                                        musteri.bakiye -= yollanacak_para
                                                        transfer.bakiye += yollanacak_para
                                                        print("Transfer işlemi başarılı!")
                                                        input(menu)
                                                    elif onay=="h" or onay=="H":
                                                        print("İşleminiz iptal edildi")
                                                        input(menu)
                                                    else:
                                                        print("Hatalı seçim yaptınız")
                                                        input(menu)


                                                else:
                                                    print("Bakiyeniz yetersiz!")
                                else:
                                    print("Hatalı TC girişi yaptınız")
                                    input(menu)

                            elif secim2=="4":
                                cekilecek_miktar=int(input("Ne kadar para çekmek istiyorsunuz? :"))
                                if cekilecek_miktar<= musteri.bakiye:
                                    onay= input("Hesabınızdan {} TL çekmeyi onaylıyor musunuz? (E/H):  ".format(cekilecek_miktar))
                                    if onay=="e" or onay=="E":
                                        musteri.bakiye -= cekilecek_miktar
                                        print("Hesabınızdan başarıyla para çekilmiştir!")
                                        input(menu)
                                    elif onay=="h" or onay=="H":
                                        print("İşleminiz iptal edildi")
                                        input(menu)
                                    else:
                                        print("Hatalı seçim yaptınız")
                                        input(menu)
                                else:
                                    print("Bakiyeniz yetersiz!")

                            elif secim2=="q" or secim2=="Q":
                                print("Çıkış yapılıyor. Bizi tercih ettiğiniz için teşekkür ederiz!")
                                quit()

                            else:
                                print("Hatalı seçim yaptınız!")
                                input(menu)

    elif secim=="2":
        print("Hoş geldiniz! ")
        ad_soyad= input("Ad Soyad: ")
        tc= input("TC kimlik numaranız: ")
        sifre = input("Lütfen şifrenizi giriniz: ")

        banka.musteri_ol(ad_soyad,tc,sifre)
        print("Başarıyla kaydoldunuz. Bizi tercih ettiğiniz için teşekkürler")
        input(menu)

    elif secim=="q" or secim=="Q":
        print("Çıkış yapılıyor. Yine bekleriz!")
        quit()

    else:
        input(menu)


