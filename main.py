""""

1.program baslayinca bize menü gelecek, bu menüde aşağıdaki şekilde liste olacak
    ürünleri listele
    ürünleri ekle
    ürünleri sil

2.ürünleri listelersem o ana kadar eklenen ürünleri kullanıcıya göster

3.ürün ekleyi seçersem program benden ürünün adı,fiyatı, kaç tane stokta bulunduğunu bana sormalı ve buraya kaydetmeli

4.ürün sil seçersem, program yine ürünleri listeleyecek ve yanında hangi sayı bulunan ürünü silmek istiyorsak o numarayı yazmamızı isteyecek

"""

#Program başlıyor...

#kalıcı değişkenler, burada tanımlama nedenim, programın her yerinden bu değişkenlere ulaşmam içindir.

urunAdilistesi = []
urunFiyatiListesi = []
urunStoguListesi = []

uygulamacalisiyor = True

print("******\nPython ile yazılmış basit stok programına hoşgeldiniz.\n******\n")

while(uygulamacalisiyor):

    print("***********\n")

    print("İşlem Listesi\n 1.Ürünleri listele.\n 2.Ürün ekle.\n 3.Ürün sil.\n 4. Programı kapatmak için q tuşuna basmanız yeterli.")

    islemno = input("İşlem numarasını giriniz:")

    """if içerisine sayılari çift tırnak içerisinde yazmamızın nedeni input içerisinden gelen değerlerin string olarak gelmesidir."""

    if islemno == "1":
        for urun in urunAdilistesi:
            print(" - ", urun)


    elif islemno == "2":
        urunadi = input("Ürünün adı: ")
        urunfiyati = input("Ürünün fiyatı: ")
        urunstogu = input("Ürün stok sayısı: ")

        urunAdilistesi.append(urunadi)
        urunFiyatiListesi.append(urunfiyati)
        urunStoguListesi.append(urunstogu)

        #  .append ekle demek, eklemesini sağladı.


        print(urunstogu, urunadi, "sisteme eklendi.")

    elif islemno == "3":

        if len(urunAdilistesi)==0: # len. lenght den yani uzunluktan geliyor, len in içine girdiğimiz array in kaç tane elemanı olduğunu bize verir.
            print("Herhangi bir ürün bulunmadığından silme işlemi gerçekleştirilemiyor.")

        else:
            i = 0
            for urun in urunAdilistesi:
                print(" - ", i, urun)
                i += 1

            urunkodu = input("silmek istediğiniz ürünün kodu: ")
            urunkodu = int(urunkodu)

            urunAdilistesi.pop(urunkodu)
            urunFiyatiListesi.pop(urunkodu)
            urunStoguListesi.pop(urunkodu)

            print("ürün silme işlemi gerçekleşti.")

    elif islemno=="q":
        print("programdan çıktın.")
        uygulamacalisiyor=False


    else:
        print("Hatalı işlem numarası girildi.")






















