import time

from supermarket import *

print("""*****************************


Sepetinize Hoşgeldiniz

İşlemler;

1. Ürünleri Göster

2. Ürünleri Sorgula

3. Sepete Ürün Ekle

4. Sepetten Ürün Sil


Sepetinizden çıkmak için lütfen 'q' ya basınız... İyi alışerişler dileriz....




*****************************""")

supermarket = Ürünler()

while True:

    işlem = input("Yapacağınız İşlem:  ")

    if(işlem == "q"):
        print("Program Sonlandırılıyor......")
        print("İyi alışverişler dileriz")
        break

    elif(işlem == "1"):
        supermarket.urunleri_goster()

    elif(işlem == "2"):
        adı = input("Hangi ürünü arıyorsunuz ?")
        print("Ürünler arasından istediğinizi arıyoruz.... Bu biraz sürebilir....")
        time.sleep(2)

        supermarket.ürün_sorgula(adı)

    elif(işlem == "3"):
        adı = input(("Adı: "))
        bölüm = input("Bölüm: ")
        marka = input("Marka: ")
        fiyat = float(input("Fiyat: "))
        gr = float(input("Gr: "))
        stt = int(input("Son Tüketim Tarihi (GGAAYY): "))

        yeni_urun = Ürün(adı,bölüm,marka,fiyat,gr,stt)

        print("Ürününüz sepetinize ekleniyor.....")
        time.sleep(2)

        supermarket.sepeteürün_ekle(yeni_urun)

        print("Ürün sepetinize başarıyla eklendi")

    elif(işlem == "4"):
        adı = input("Hangi ürünü sepetinizden çıkarmak istiyorsunuz ? ")

        cevap = input("Emin misiniz ? E/H")

        if (cevap == "E"):
            print("Ürün sepetinizden siliniyor......")
            time.sleep(2)

            supermarket.sepettekiürünü_sil(adı)
            print("Ürün sepetinizden silindi.....")

        else:

            print("Geçersiz işlem.......")




























