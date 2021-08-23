import sqlite3

import time

class Ürün():

    def __init__(self,adı,bölüm,marka,fiyat,gr,stt):

        self.adı = adı
        self.bölüm = bölüm
        self.marka = marka
        self.fiyat = fiyat
        self.gr = gr
        self.stt = stt

    def __str__(self):

        return "Ürünün Adı: {}\nBölüm: {}\nMarka: {}\nFiyat: {}\nGr: {}\nSon Tüketim Tarihi: {}\n".format(self.adı,self.bölüm,self.marka,self.fiyat,self.gr,self.stt)

class Ürünler():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("supermarket.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists ürünler (adı TEXT,bölüm TEXT,marka TEXT,fiyat INT,gr INT,stt INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def urunleri_goster(self):

        sorgu = "Select * From ürünler"

        self.cursor.execute(sorgu)

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print("Ürün bulunmuyor...")

        else:
            for i in ürünler:
                ürün = Ürün(i[0],i[1],i[2],i[3],i[4],i[5])
                print(ürün)

    def ürün_sorgula(self,adı):

        sorgu = "Select * From ürünler where adı = ? "

        self.cursor.execute(sorgu(adı,))

        ürünler = self.cursor.fetchall()

        if(len(ürünler) == 0):
            print("Sepetinizde böyle bir ürün bulunmamaktadır......")

        else:
            ürün = Ürün(ürünler[0][0],ürünler[0][1],ürünler[0][2],ürünler[0][3],ürünler[0][4],ürünler[0][5])

            print(ürün)

    def sepeteürün_ekle(self,ürün):

        sorgu = "Insert into ürünler Values(?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(ürün.adı,ürün.bölüm,ürün.marka,ürün.fiyat,ürün.gr,ürün.stt))
        self.baglanti.commit()

    def sepettekiürünü_sil(self,adı):

        sorgu = "Delete From ürünler where adı = ? "

        self.cursor.execute(sorgu(adı,))
        self.baglanti.commit()





































