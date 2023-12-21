örgen ok vs çizme
#Chekbutton: Kullanıcıdan birden fazla şey seçmesini istersek
#Entry: Tek satırlık veri girişi
#Frame: Windowları bölme,konumlandırma
#Label: Kullanıcının bilgilendirilmesi için kullanılınır.Tek satırdır.
#Listbox: Seçilebilir içerikler olan ve bunların alt alta yazdığı.
#Menu: Windowa katagorileri ve alt butonu yerleştiriyoruz.
#Message: Birden fazla satır metin göstermek istiyorsak.
#Radiobutton: Kullanıcın bir seçenek seçmesini istersek.
#Text: Birden fazla satır veri girişi

#GEÇMİŞ SINAV SORUSU:
#bir liste kutusunda kıtalar var.
#birine tıklayınca ilgili ülkeler ona tıkladığında
#ülkenin adı para birimi vs çıkıyormuş

"""
#BOŞ PENCERE OLUŞTURMA:
import tkinter
def main():
    anapencere = tkinter.Tk()
    tkinter.mainloop()
    #kinterın altındaki pencerenin eknranda kalmasını sağlıyoruz.

main()"""
"""
#SINIF KULLANARAK PENCERE OLUŞTURMA:
import tkinter
class Sınıfım:
    def _init__(öz):
        öz.pencerem= tkinter.Tk()
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#PENCEREYE İSİM VERME:
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem=tkinter.Tk()
        öz.pencerem.title("BenimSınıf")
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#PENCERE İÇİNDE TEK SATIRLIK METİN GÖSTERME:
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem, text= "Nesne çok zor")
        öz.yazı.pack()
        tkinter.mainloop()
        sınıf = Sınıfım()
"""

#Sınıf oluşturuyoruz
#Pencere açıyoruz
#İçine ne yazacagımızı belirliyoruz
#Paketliyoruz sola saga dayalı yazıyoruz.
#YAZININ KONUMUNU AYARLAMAK
"""
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem, text = "Selam")
        öz.yazı.pack(side="left")
        tkinter.mainloop()
        sınıf = Sınıfım()
"""

#SINIR ÇİZGİSİ ÇİZME:
#self.yazı = tkinter.yazı(öz.pencerem , text= "merhaba",borderwidth = 1, relief = "solid")
#relief='flat' | relief='raised' | relief='sunken' | relief='ridge' | relief='solid' | relief='groove'
#INTERNAL PADDİNG: border çizgisi ve metin arasındaki boşluk
#ipadx = n , ipady = n (Yatay boşluklar)
#padx = n, pady=n (Dikey boşluklar)
"""
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem , text = "merhaba" ,borderwith = 1, relief = "solid")
        öz.yazı.pack(ipadx = 5 , ipady=5)
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#SINIF OLUŞTURURKEN PARANTEZ KULLANMA!
#PENCEREYİ BÖLME(Frame):
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.üstkısım = tkinter.Frame(öz.pencerem)
        öz.altkısım = tkinter.Frame(öz.pencerem)
        öz.yazı1 = tkinter.Label(öz.üstkısım , text = "Selam")
        öz.yazı2 = tkinter.Label(öz.üstkısım , text = "Merhaba")
        öz.yazı1.pack(side = "top")
        öz.yazı2.pack(side = "top")
        öz.yazı3 = tkinter.Label(öz.altkısım , text = "Selam")
        öz.yazı4 = tkinter.Label(öz.altkısım , text= "arkadaşlar")
        öz.yazı3.pack(side = "left")
        öz.yazı4.pack(side = "left")
        öz.üstkısım.pack()
        öz.altkısım.pack()
        tkinter.mainloop()
        sınıfım = Sınıfım()
        #Selam ve Merhaba yı alt alta yazdırır. Onun altına Selam arkadaşlar yazdırır.
"""
"""
#BUTTON DEMO
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum = tkinter.Button(öz.pencerem , text = "Bana tıkla", command = öz.butona_tıkladın)
        öz.butonum.pack()
        tkinter.mainloop()
    def butona_tıkladın(öz):
        tkinter.messagebox.showinfo("Uyarı" , "Tıkladığınız için teşekkürler")
        sınıfım = Sınıfım()

#sınıfım = Sınıfım() : NEREYE YAZILACAK BAK!
"""
#ÖNCE PENCEREYİ OLUŞTURUYORUZ.
#SONRA BUTONLARI OLUŞTURUYORUZ.
#SONRA QUİT BUTONU DIŞINDAKİ BUTONA BASTIĞIMIZDA NE YAPACAĞINI YAZIYORUZ.
#QUİT BUTONU İÇİN TANIMLARKEN ZATEN DESTROY KULLANIYORUZ.

#PENCEREYİ KAPATMA:
#destroy: Butona bastığımızda sayfayı kapatması için kullanıyoruz.
"""
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum1 = tkinter.Button(öz.pencerem , text = "TIKLA" , command = öz.butona_tıkladın)
        öz.butonum2 = tkinter.Button(öz.pencerem , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.butonum1.pack()
        öz.butonum2.pack()
        tkinter.mainloop()
    def butona_tıkladın(öz):
        tkinter.messagebox.showinfo("UYARI" , "Tıkladığınız için teşekkürler")
        sınıfım = Sınıfım()
"""
#KULLANICIDAN VERİ ALMA:
#FRAMELER PENCEREYİ DÜZENLEMEK İÇİN KULLANILIR.
#ENTRY KULLANICIDAN GİRİŞ ALMAK İÇİN KULLANILIR.

#öNCE PENCERE OLUŞTUR.
#SONRA FRAMELERLE PENCEREYİ BÖL VE YAZI YAZ.(LABEL YANİ ETİKETLERLE).
#SONRA BU LABELLARLA KULLANICIDAN VERİ ALICAZ. ENTRY İLE YAPIYORUZ.
#SONRA BUTON OLUŞTURUYORUZ.
#PACKLEMEYİ UNUTMA.
"""
import tkinter
import tkinter.messagebox
class kmdönüstürücü:
    def __init__(öz):
        öz.pencerem =tkinter.Tk()
        öz.üstframe = tkinter.Frame(öz.pencerem)
        öz.altframe = tkinter.Frame(öz.pencerem)
        öz.etiketim = tkinter.Label(öz.üstframe , text = "Kilometreyi giriniz:")
        öz.kmgirisi = tkinter.Entry(öz.üstframe , width = 10)
        öz.etiketim.pack(side = "left")
        öz.kmgirisi.pack(side ="left")
        öz.hesapla = tkinter.Button(öz.altframe , text = "HESAPLA" , command = öz.hesaplama)
        öz.çıkış = tkinter.Button(öz.altframe , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.hesapla.pack(side = "left")
        öz.çıkış.pack(side = "left")
        öz.üstframe.pack()
        öz.altframe.pack()
        tkinter.mainloop()
    def hesaplama(öz):
        km = float(öz.kmgirisi.get())
        mil = km * 0.6214
        tkinter.messagebox.showinfo("SONUÇ" , str(km) + "km mil cinsinden =" + str(mil))
        Kmdönüstürücü = kmdönüstürücü()
"""

#KMDÖNÜSTÜRÜCÜ2
#BUNUN FARKI DÖNÜŞTÜRE TIKLADIĞIMIZDA YENİ BİR SAYFA AÇMAYIP EKRANDA OLAN LABELIN YANINA SONUCU YAZDIRIR.
#LABELIN DEĞERİNİ VALUEDAN ALIYORUZ.
# Etiket, StringVar nesnesiyle ilişkilendirilmiş ve bu nesnenin değeri etikette görüntülenmiştir.
#MESSAGEBOX I ÇAĞIRMADAN YAPIYORUZ.
"""
import tkinter
class kmcevirici:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.üstframe = tkinter.Frame()
        öz.ortaframe = tkinter.Frame()
        öz.altframe = tkinter.Frame()
        öz.kmetiketi = tkinter.Label(öz.üstframe , text = "Çevirmek istediğiniz km yi giriniz:")
        öz.kmgirisi = tkinter.Entry(öz.üstframe , width = 10)
        öz.kmetiketi.pack(side = "left")
        öz.kmgirisi.pack(side = "left")
        öz.dönüsüm = tkinter.Label(öz.ortaframe , text = "Mil e dönüşmüş hali:")
        öz.deger = tkinter.StringVar()
        öz.miletiketi = tkinter.Label(öz.artaframe , textvariable=öz.deger)
        öz.dönüsüm.pack(side = "left")
        öz.miletiketi.pack(side = "left")
        öz.dönüstürbutonu = tkinter.Button(öz.altframe , text = "DÖNÜŞTÜR" , command = öz.dönüstür)
        öz.çıkışbutonu = tkinter.Button(öz.altframe , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.dönüstürbutonu.pack(side = "left")
        öz.çıkışnutonu.pack(side = "left")
        öz.üstframe.pack()
        öz.ortaframe.pack()
        öz.altframe.pack()
        tkinter.mainloop()
    def dönüstür(öz):
        km = float(öz.kmgirisi.get())
        mil = km * 0.6214
        öz.deger.set(mil)
        Kmcevirici = kmcevirici()
"""
#ORTALAMA HESAPLAMA:
#3 NOT ALIP ORTALAMAYI HESAPLIYORUZ.
#5 FRAME E BÖLÜCEZ
"""
import tkinter
class Ortalama:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.test1_frame = tkinter.Frame()
        öz.test2_frame = tkinter.Frame()
        öz.test3_frame = tkinter.Frame()
        öz.ort_frame = tkinter.Frame()
        öz.buton_frame = tkinter.Frame()
        öz.test1etiket = tkinter.Label(öz.test1_frame , text="Test1:")
        öz.test1giris = tkinter.Entry(öz.test1_frame , width = 10)
        öz.test1etiket.pack(side = "left")
        öz.test1giris.pack(side = "left")
        öz.test2etiket = tkinter.Label(öz.test2_frame, text = "Test2:")
        öz.test2giris = tkinter.Label(öz.test2_frame , width = 10)
        öz.test2etiket.pack(side = "left")
        öz.test2giris.pack(side = "left")
        öz.test3etiket = tkinter.Label(öz.test3_frame , text = "Test3:")
        öz.test3giris = tkinter.Entry(öz.test3_frame , width = 10)
        öz.test3etiket.pack(side = "left")
        öz.test3giris.pack(side = "left")
        öz.sonucetiketi = tkinter.Label(öz.ort_frame , text = "Ortalama:")
        öz.ort =tkinter.StringVar()
        öz.sonuc = tkinter.Label(öz.ort_frame , textvariable = öz.ort)
        öz.sonucetiketi.pack(side = "left")
        öz.sonuc.pack(side="left")
        öz.hesaplabutonu = tkinter.Button(öz.buton_frame , text = "Hesapla" , command = öz.hesaplama)
        öz.çıkışbutonu = tkinter.Button(öz.buton_frame , text = "Çıkış" , command = öz.pencerem.destroy)
        öz.hesaplabutonu.pack(side = "left")
        öz.çıkışbutonu.pack(side = "left")
        öz.test1_frame.pack()
        öz.test2_frame.pack()
        öz.test3_frame.pack()
        öz.ort_frame.pack()
        öz.buton_frame.pack()
        tkinter.mainloop()
    def hesaplama(öz):
        öz.test1 = float(öz.test1giris.get())
        öz.test2 = float(öz.test2giris.get())
        öz.test3 = float(öz.test3giris.get())
        öz.ort = (öz.test1+öz.test2+öz.test3) / 3.0
        öz.ortalama.set(öz.ort)
        ortalama =Ortalama()
"""
#Pencere içine tek satırlık metin yazma:
"""
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem , text ="Merhaba")
        öz.yazı.pack()
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#DİKDÖRTGEN İÇİNDE YAZI YAZMA:
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem, text ="Merhaba" , borderwidth = 1 , relied = "solid")
        öz.yazı.pack(ipadx=20 , ipady=20)
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#ipadx yazının etrafındaki çerçevenin boşluklarını belirliyor.
#padx pencerenin etrafındaki boşlukları belirliyor.(yazının çerçevesinin pencerenin çerçevesine oranını belirlemek için)
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı1 = tkinter.Label(öz.pencerem, text = " Merhaba" , borderwidth = 20 , relief = "solid")
        #borderwidth büyük ihtimal yazının bulunduğu çerçevenin kalınlığı
        öz.yazı2= tkinter.Label(öz.pencerem , text = "Dünya" , borderwidth = 15, relief = "solid")
        öz.yazı1.pack(padx=10 , pady=10)
        öz.yazı2.pack(padx=10, pady=10)
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#PENCEREYİ BÖLME:
#TOP YAZDIĞIMIZ İÇİN ALT ALTA YAZDIRACAK.
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.frame1 = tkinter.Frame(öz.pencerem)
        öz.frame2 = tkinter.Frame(öz.pencerem)
        öz.yazı1 = tkinter.Label(öz.frame1 , text = "Halil")
        öz.yazı2 = tkinter.Label(öz.frame2 , text="Murat")
        öz.yazı1.pack(side = "top")
        öz.yazı2.pack(side = "top")
        öz.frame1.pack()
        öz.frame2.pack()
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#BUTON
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum = tkinter.Button(öz.pencerem , text = "TIKLA" , command = öz.tıkladım)
        öz.butonum.pack()
        tkinter.mainloop()
    def tıkladım(öz):
        tkinter.messagbox.showinfo("Uyarı" , "Tıkladığınız için teşekkürler.")
        sınıfım = Sınıfım()
"""
"""
#PENCEREYİ KAPATMA
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum = tkinter.Button(öz.pencerem, text ="TIKLA" , command = öz.tıkladım)
        öz.çıkışbutonu = tkinter.Button(öz.pencerem , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.butonum.pack()
        öz.çıkışbutonu.pack()
        tkinter.mainloop()
    def tıkladım(öz):
        tkinter.messagebox.showinfo("Uyarı" , "Tıkladığınız için teşekkürler.")
        sınıfım =Sınıfım()
"""
"""
#PARA ATMA
import random
class para:
    def __init__(öz):
        öz.parayüzü = "yazı"
    def çarpıştır(öz):
        if random.randint(0,1) == 0:
            öz.parayüzü = "yazı"
        else:
            öz.parayüzü="tura"
    def yüzüal(öz):
        return öz.parayüzü

def main():
    param = para() #nesnenin adı = sınıfın adı
    print("Paranın yüzü şuan:" + param.yüzüal())
    print("Parayı atıyorum:")
    param.çarpıştır()
    print("Şimdi paranın yüzü:" + param.yüzüal() )
main()"""

# Bu bölümde daha önce belirttiğimiz gibi, bir nesnenin veri özellikleri özel olmalıdır,
# böylece yalnızca nesnenin yöntemleri doğrudan erişebilir. Bu, nesnenin veri
# özelliklerini kazara bozulmaya karşı korur. Ancak, önceki örnekte gösterilen Coin
#sınıfında sideup özelliği özel değildir. Ona, Coin sınıfı yöntemleri içinde olmayan ifadeler doğrudan erişebilir.
# bunuda " __ "koyarak yapıyoruz.

"""
#PARA ATMA2 ("DOSYAYA KAYDETMELİ")
import random
class Para:
    def __init__(öz):
        öz.__parayüzü = "yazı"
    def çarpıştır(öz):
        if random.randint(0,1) == 0:
            öz.__parayüzü = "yazı"
        else:
            öz.__parayüzü = "tura"
    def paranınyüzünüal(öz):
        return öz.__parayüzü
"""
"""
#ÜSTTE SINIIFIN YAZILI OLDUĞU KOD AÇIK DEĞİLSE SINIFIN İÇİNDE BULUNDUĞU DOSYAYI İMPORTLAYABİLİRİZ.
import c13 #import ettiğimiz şey kodun kayıtlı olduğu dosya
def main():
    param = c13.Para()

    print("Parayı 10 kere atacağım.")
    for a in range(10):
        param.çarpıştır()
        print(param.paranınyüzünüal())
main()"""

"""
#bankaccount  #KOD ÇALIŞMIYOR
class BankaHesabı:
    def __init__(öz,para):
        öz.__paramik = para
    def yükle(öz,miktar):
        öz.__paramik += miktar
    def çek(öz,miktar):
        if öz.__paramik>= miktar:
            öz.__paramik -= miktar
        else:
            print("Bu miktar çekilemez.")
    def bankadakimiktar(öz):
        return öz.__paramik

import c13
def main():
    param = float(input("Bankada ne kadar paranız var."))
    bankam = c13.BankaHesabı(param) #sınıfa bir değer atadık.
    ekle = float(input("ne kadar yüklemek istiyorsun:"))
    bankam.yükle(ekle)
    çekme = float(input("ne kadar para çekmek istiyorsun:"))
    bankam.çek(çekme)
    print(f"Banka hesabındaki son miktar: {param.bankadakimiktar()}")
main()
"""
"""
#BOZUK PARA ATMA ; 3 FARKLI NESNE TANIMLIYORUZ ; 3 FARKLI BOZUK PARANIN ATILMASI GİBİ OLUYOR
import c13
def main():
    coin1 = c13.Para()
    coin2 = c13.Para()
    coin3 = c13.Para()
    print(coin1.paranınyüzünüal())
    print(coin2.paranınyüzünüal())
    print(coin3.paranınyüzünüal())
    print()

    coin1.çarpıştır()
    coin2.çarpıştır()
    coin3.çarpıştır()

    print(coin1.paranınyüzünüal())
    print(coin2.paranınyüzünüal())
    print(coin3.paranınyüzünüal())
    print()
main()"""

"""
#TELEFON PY
class Telefon:
    def __init__(öz,üretici,model,fiyat):
        öz.__üretici=üretici
        öz.__model=model
        öz.__fiyat=fiyat
    def set_üretici(öz,üretici):
        öz.__üretici = üretici
    def set_model(öz,model):
        öz.__model=model
    def set_fiyat(öz,fiyat):
        öz.__fiyat = fiyat
    def get_üretici(öz,üretici):
        return öz.__üretici
    def get_model(öz,model):
        return öz.__model
    def get_fiyat(öz,fiyat):
        return öz.__fiyat

import c13
def main():
    üretici = input("Üreticiyi giriniz:")
    model = input("Modeli giriniz:")
    fiyat = float("Fiyatı giriniz:")
    telefon = c13.Telefon(üretici,model,fiyat)
    print("Girdiğin bilgiler:")
    print(f"{telefon.get_üretici()}")
    print(f"{telefon.get_model()}")
    print(f"{telefon.get_fiyat()}")
main()

#Bir Listede Nesneler Saklama
import c13
def main():
    telefonlar = liste_yap()
    print(f"Girdiğiniz bilgiler {listeyi_oynat(telefon_listesi)}")
def liste_yap():
    telefon_listesi = []
    print("5 tane telefon için bilgileri giriniz:")
    for a in range(1,6): #1 den başlayıp 5 e kadar yazdırır.
        print("Telefon numarası:" + str(a))
        üretici = input("Üreticiyi giriniz:")
        model = input("Modeli giriniz:")
        fiyat = input("Fiyatı giriniz:")
        print()
        telefon = c13.Telefon(üretici,model,fiyat)
        telefon_listesi.append(telefon)
        return telefon_listesi #LİSTEYİ DÖNDÜRMEYİ UNUTMA!
def listeyi_oynat(telefon_listesi):
    for item in telefon_listesi:
        print(item.get_üretici())
        print(item.get_model())
        print(item.get_fiyat())

main()"""
"""
#Sonuç olarak, nesneyi argüman olarak alan fonksiyon veya metod, gerçek nesneye erişim sağlar.
import c13
def main():
    param = c13.Para()
    print(param.paranınyüzünüal())
    flip(param) #FONKSİYONUN İÇİNE NESNEYİ KOYDUK
    print(param.paranınyüzünüal())
def flip(coin_obj):
    coin_obj.çarpıştır()
main()"""
"""
#NESNEYİ PİCKLELAMA:
import pickle
import c13
dosyaadı = "telefonum.dat" #dosya adını mainin dışına yazdık.
def main():
    again = "y"
    dosyayayaz = open(dosyaadı , "wb")
    while again =="y" or again=="Y":
        üretici = input("Üreticiyi giriniz")
        model = input("Modeli giriniz:")
        fiyat = input("Fiyatı giriniz:")
        telefon = c13.Telefon(üretici,model,fiyat)
        pickle.dump(telefon, dosyayayaz)
        again = input("Devam etmek için y ye basınız.")
    dosyayayaz.close()
    print("Bilgiler telefonum.dat dosyasına yazıldı.")
main()"""
"""
#UNPİCKLE TELEFON.py
import pickle
import c13
dosyaadı = "telfonum.dat"
def main():
    dosya_sonu = False
    dosyaya_gir = open(dosyaadı, "rb")
    while not dosya_sonu:
        try:
            telefon = pickle.load(dosya_gir)
            oynat(telefon)
        except EOFError:
        dosya_sonu = True
    dosyaya_gir.close()
def oynat(telefon):
    print(telefon.get_üretici())
    print(telefon.get_model())
    print(telefon.get_fiyat())
    print()
main()"""
"""
#İLETİŞİM
class İletişim:
    def __init__(öz,isim,telefon,mail):
        öz.__isim = isim
        öz.__telefon = telefon
        öz.__mail = mail
    def set_isim(öz,isim):
        öz.__isim =isim
    def set_telefon(öz,telefon):
        öz.__telefon = telefon
    def set_mail(öz,mail):
        öz.__mail = mail
    def get_isim(öz):
        return öz.__isim
    def get_telefon(öz)
        return öz.__telefon
    def get_mail(öz):
        return öz.__mail
"""
#__STR__ NE İŞE YARIYOR ANLAMADIM.
"""
#İLETİŞİM MANAGER:
import c13
import pickle
BAK = 1
EKLE = 2
DEĞİŞTİR = 3
SİL = 4
ÇIK = 5

dosyaadı = "iletişim.dat"
def main():
    iletişimlerim = yükleiletişim()
    choice = 0
    while choice != ÇIK:
        choice = seçimyap()
        if choice == BAK:
            bak(iletişimlerim)
        elif choice == EKLE:
            ekle(iletişimlerim)
        elif choice == DEĞİŞTİR:
            değiştir(iletişimlerim)
        elif choice == SİL:
            sil(iletişimlerim)
    iletişimleri_kaydet(iletişimlerim)
def yükleiletişim():
    try:
        dosyayagir = open(dosyaadı ,"rb")
        iletişim_sözlüğü = pickle.load(dosyayagir)
        dosyayagir.close()
    except IOError:
        iletişim_sözlüğü = {}
    return iletişim_sözlüğü
def seçimyap():
    print("Menü")
    print("1: BAK")
    print("2: EKLE")
    print("3: DEĞİŞTİR")
    print("4:SİL")
    print("5:ÇIK")
    choice = int(input("Yapmak istediğiniz işlemi seçiniz:"))
    while choice< BAK or choice>ÇIK:
        print("Geçerli bir sayı giriniz.")
        choice = int(input("Yapmak istediğiniz işlemi giriniz:"))
    return choice
def bak(iletişimlerim):
    name = input("İsim giriniz")
    print(iletişimlerim.get(name , "İsim bulunamadı"))
def ekle(iletişimlerim):
    name = input("İsim giriniz:")
    telefon = input("Telefon numarası giriniz:")
    mail = input("Eposta adresini giriniz:")
    gir = c13.İletişim(name,telefon,mail)
    if name not in iletişimlerim:
        iletişimlerim[name] = ekle
    else:
        print("İsim zaten mevcut")
def değiştir(iletişimlerim):
    name = input("İsim giriniz:")
    if name in iletişimlerim:
        telefon = input("Telefon numarası giriniz:")
        mail = input("Eposta adresini giriniz:")
        gir = c13.İletişim(name,telefon,mail)
        iletişimlerim[name] = gir
    else:
        print("İsim bulunamadı.")
def sil(iletişimlerim):
    name = input("İsim giriniz:")
    if name in iletişimlerim:
        del iletişimlerim[name]
    else:
        print("İsim bulunamadı.")
def iletişimleri_kaydet(iletişimlerim):
    dosyayagir = open(dosyaadı , "wb")
    pickle.dump(iletişimlerim , dosyayagir)
    dosyayagir.close()
main()"""

#OPTİON 11
#Miras, bir yeni sınıfın mevcut bir sınıfı genişletmesine olanak tanır.
#Yeni sınıf, genişlettiği sınıfın üyelerini miras alır.

#Bir nesne diğer bir nesnenin uzmanlaşmış bir versiyonu ise, aralarında bir "bir" ilişkisi bulunur.
#Örneğin, bir çekirge bir böcektir. İşte "bir" ilişkisinin birkaç örneği:
#Bir çiçek bir bitkidir.
#Bir dikdörtgen bir şekildir.
#Nesneler arasında bir "bir" ilişkisi varsa, bu, uzmanlaşmış nesnenin genel nesnenin
#tüm özelliklerine sahip olduğu ve onu özel kılan ek özelliklere sahip olduğu anlamına gelir.
#Nesne tabanlı programlamada, miras kullanılarak sınıflar arasında bir "bir" ilişkisi oluşturulur.
#Bu, bir sınıfın yeteneklerini başka bir sınıfın uzmanlaşmış bir versiyonunu oluşturarak genişletmenizi sağlar.
#Miras, bir üst sınıf (superclass) ve bir alt sınıf (subclass) içerir.
# Üst sınıf genel bir sınıftır ve alt sınıf uzmanlaşmış bir sınıftır.
# Alt sınıfı, üst sınıfın genişletilmiş bir versiyonu olarak düşünebilirsiniz.
# Alt sınıf, üst sınıftan özellikler ve yöntemler miras alır, bunların hiçbiri yeniden yazılmadan.
#Ayrıca, alt sınıfa yeni özellikler ve yöntemler eklenerek, onu üst sınıfın uzmanlaşmış bir versiyonu yapar.

"""
#YANİ İKİ CLASSI İÇ İÇE ŞEKİLDE YAZIYORUZ.
class otomobil:
    def __init__(öz,marka,model,km,fiyat):
        öz.__marka = marka
        öz.__model = model
        öz.__km = km
        öz.__fiyat = fiyat
    def set_marka(öz,marka):
        öz.__marka = marka
    def set_model(öz,model):
        öz.__model = model
    def set_km(öz,km): #sette yanına özden başka bir şey daha yazıyoruz. get de yazmıyoruz.
        öz.__km = km
    def set_fiyat(öz,fiyat):
        öz.__fiyat = fiyat
    def get_marka(öz):
        return öz.__marka
    def get_model(öz):
        return öz.__model
    def get_km(öz)
        return öz.__km
    def get_fiyat(öz):
        return öz.__fiyat
class araba(otomobil):
    def __init__(öz,marka,model,km,fiyat,kapı):
        otomobil.__init__(öz,marka,model,km,fiyat)
        öz.__kapı = kapı
    def set_kapı(öz,kapı):
        öz.__kapı=kapı
    def get_kapı(öz):
        return öz.__kapı
"""

#import vehicles(araçlar):Otomobil ve Araba sınıflarına ilişkin sınıf tanımlarını içeren araçlar modülünü içe aktarır.
#import vehicles#Grafical User Interfaces
#Button: Tıklandığında atandığı metodu icra ediyor.
#Canvas: Diktörgen ok vs çizme
#Chekbutton: Kullanıcıdan birden fazla şey seçmesini istersek
#Entry: Tek satırlık veri girişi
#Frame: Windowları bölme,konumlandırma
#Label: Kullanıcının bilgilendirilmesi için kullanılınır.Tek satırdır.
#Listbox: Seçilebilir içerikler olan ve bunların alt alta yazdığı.
#Menu: Windowa katagorileri ve alt butonu yerleştiriyoruz.
#Message: Birden fazla satır metin göstermek istiyorsak.
#Radiobutton: Kullanıcın bir seçenek seçmesini istersek.
#Text: Birden fazla satır veri girişi

#GEÇMİŞ SINAV SORUSU:
#bir liste kutusunda kıtalar var.
#birine tıklayınca ilgili ülkeler ona tıkladığında
#ülkenin adı para birimi vs çıkıyormuş

"""
#BOŞ PENCERE OLUŞTURMA:
import tkinter
def main():
    anapencere = tkinter.Tk()
    tkinter.mainloop()
    #kinterın altındaki pencerenin eknranda kalmasını sağlıyoruz.

main()"""
"""
#SINIF KULLANARAK PENCERE OLUŞTURMA:
import tkinter
class Sınıfım:
    def _init__(öz):
        öz.pencerem= tkinter.Tk()
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#PENCEREYE İSİM VERME:
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem=tkinter.Tk()
        öz.pencerem.title("BenimSınıf")
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#PENCERE İÇİNDE TEK SATIRLIK METİN GÖSTERME:
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem, text= "Nesne çok zor")
        öz.yazı.pack()
        tkinter.mainloop()
        sınıf = Sınıfım()
"""

#Sınıf oluşturuyoruz
#Pencere açıyoruz
#İçine ne yazacagımızı belirliyoruz
#Paketliyoruz sola saga dayalı yazıyoruz.
#YAZININ KONUMUNU AYARLAMAK
"""
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem, text = "Selam")
        öz.yazı.pack(side="left")
        tkinter.mainloop()
        sınıf = Sınıfım()
"""

#SINIR ÇİZGİSİ ÇİZME:
#self.yazı = tkinter.yazı(öz.pencerem , text= "merhaba",borderwidth = 1, relief = "solid")
#relief='flat' | relief='raised' | relief='sunken' | relief='ridge' | relief='solid' | relief='groove'
#INTERNAL PADDİNG: border çizgisi ve metin arasındaki boşluk
#ipadx = n , ipady = n (Yatay boşluklar)
#padx = n, pady=n (Dikey boşluklar)
"""
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem , text = "merhaba" ,borderwith = 1, relief = "solid")
        öz.yazı.pack(ipadx = 5 , ipady=5)
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#SINIF OLUŞTURURKEN PARANTEZ KULLANMA!
#PENCEREYİ BÖLME(Frame):
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.üstkısım = tkinter.Frame(öz.pencerem)
        öz.altkısım = tkinter.Frame(öz.pencerem)
        öz.yazı1 = tkinter.Label(öz.üstkısım , text = "Selam")
        öz.yazı2 = tkinter.Label(öz.üstkısım , text = "Merhaba")
        öz.yazı1.pack(side = "top")
        öz.yazı2.pack(side = "top")
        öz.yazı3 = tkinter.Label(öz.altkısım , text = "Selam")
        öz.yazı4 = tkinter.Label(öz.altkısım , text= "arkadaşlar")
        öz.yazı3.pack(side = "left")
        öz.yazı4.pack(side = "left")
        öz.üstkısım.pack()
        öz.altkısım.pack()
        tkinter.mainloop()
        sınıfım = Sınıfım()
        #Selam ve Merhaba yı alt alta yazdırır. Onun altına Selam arkadaşlar yazdırır.
"""
"""
#BUTTON DEMO
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum = tkinter.Button(öz.pencerem , text = "Bana tıkla", command = öz.butona_tıkladın)
        öz.butonum.pack()
        tkinter.mainloop()
    def butona_tıkladın(öz):
        tkinter.messagebox.showinfo("Uyarı" , "Tıkladığınız için teşekkürler")
        sınıfım = Sınıfım()

#sınıfım = Sınıfım() : NEREYE YAZILACAK BAK!
"""
#ÖNCE PENCEREYİ OLUŞTURUYORUZ.
#SONRA BUTONLARI OLUŞTURUYORUZ.
#SONRA QUİT BUTONU DIŞINDAKİ BUTONA BASTIĞIMIZDA NE YAPACAĞINI YAZIYORUZ.
#QUİT BUTONU İÇİN TANIMLARKEN ZATEN DESTROY KULLANIYORUZ.

#PENCEREYİ KAPATMA:
#destroy: Butona bastığımızda sayfayı kapatması için kullanıyoruz.
"""
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum1 = tkinter.Button(öz.pencerem , text = "TIKLA" , command = öz.butona_tıkladın)
        öz.butonum2 = tkinter.Button(öz.pencerem , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.butonum1.pack()
        öz.butonum2.pack()
        tkinter.mainloop()
    def butona_tıkladın(öz):
        tkinter.messagebox.showinfo("UYARI" , "Tıkladığınız için teşekkürler")
        sınıfım = Sınıfım()
"""
#KULLANICIDAN VERİ ALMA:
#FRAMELER PENCEREYİ DÜZENLEMEK İÇİN KULLANILIR.
#ENTRY KULLANICIDAN GİRİŞ ALMAK İÇİN KULLANILIR.

#öNCE PENCERE OLUŞTUR.
#SONRA FRAMELERLE PENCEREYİ BÖL VE YAZI YAZ.(LABEL YANİ ETİKETLERLE).
#SONRA BU LABELLARLA KULLANICIDAN VERİ ALICAZ. ENTRY İLE YAPIYORUZ.
#SONRA BUTON OLUŞTURUYORUZ.
#PACKLEMEYİ UNUTMA.
"""
import tkinter
import tkinter.messagebox
class kmdönüstürücü:
    def __init__(öz):
        öz.pencerem =tkinter.Tk()
        öz.üstframe = tkinter.Frame(öz.pencerem)
        öz.altframe = tkinter.Frame(öz.pencerem)
        öz.etiketim = tkinter.Label(öz.üstframe , text = "Kilometreyi giriniz:")
        öz.kmgirisi = tkinter.Entry(öz.üstframe , width = 10)
        öz.etiketim.pack(side = "left")
        öz.kmgirisi.pack(side ="left")
        öz.hesapla = tkinter.Button(öz.altframe , text = "HESAPLA" , command = öz.hesaplama)
        öz.çıkış = tkinter.Button(öz.altframe , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.hesapla.pack(side = "left")
        öz.çıkış.pack(side = "left")
        öz.üstframe.pack()
        öz.altframe.pack()
        tkinter.mainloop()
    def hesaplama(öz):
        km = float(öz.kmgirisi.get())
        mil = km * 0.6214
        tkinter.messagebox.showinfo("SONUÇ" , str(km) + "km mil cinsinden =" + str(mil))
        Kmdönüstürücü = kmdönüstürücü()
"""

#KMDÖNÜSTÜRÜCÜ2
#BUNUN FARKI DÖNÜŞTÜRE TIKLADIĞIMIZDA YENİ BİR SAYFA AÇMAYIP EKRANDA OLAN LABELIN YANINA SONUCU YAZDIRIR.
#LABELIN DEĞERİNİ VALUEDAN ALIYORUZ.
# Etiket, StringVar nesnesiyle ilişkilendirilmiş ve bu nesnenin değeri etikette görüntülenmiştir.
#MESSAGEBOX I ÇAĞIRMADAN YAPIYORUZ.
"""
import tkinter
class kmcevirici:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.üstframe = tkinter.Frame()
        öz.ortaframe = tkinter.Frame()
        öz.altframe = tkinter.Frame()
        öz.kmetiketi = tkinter.Label(öz.üstframe , text = "Çevirmek istediğiniz km yi giriniz:")
        öz.kmgirisi = tkinter.Entry(öz.üstframe , width = 10)
        öz.kmetiketi.pack(side = "left")
        öz.kmgirisi.pack(side = "left")
        öz.dönüsüm = tkinter.Label(öz.ortaframe , text = "Mil e dönüşmüş hali:")
        öz.deger = tkinter.StringVar()
        öz.miletiketi = tkinter.Label(öz.artaframe , textvariable=öz.deger)
        öz.dönüsüm.pack(side = "left")
        öz.miletiketi.pack(side = "left")
        öz.dönüstürbutonu = tkinter.Button(öz.altframe , text = "DÖNÜŞTÜR" , command = öz.dönüstür)
        öz.çıkışbutonu = tkinter.Button(öz.altframe , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.dönüstürbutonu.pack(side = "left")
        öz.çıkışnutonu.pack(side = "left")
        öz.üstframe.pack()
        öz.ortaframe.pack()
        öz.altframe.pack()
        tkinter.mainloop()
    def dönüstür(öz):
        km = float(öz.kmgirisi.get())
        mil = km * 0.6214
        öz.deger.set(mil)
        Kmcevirici = kmcevirici()
"""
#ORTALAMA HESAPLAMA:
#3 NOT ALIP ORTALAMAYI HESAPLIYORUZ.
#5 FRAME E BÖLÜCEZ
"""
import tkinter
class Ortalama:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.test1_frame = tkinter.Frame()
        öz.test2_frame = tkinter.Frame()
        öz.test3_frame = tkinter.Frame()
        öz.ort_frame = tkinter.Frame()
        öz.buton_frame = tkinter.Frame()
        öz.test1etiket = tkinter.Label(öz.test1_frame , text="Test1:")
        öz.test1giris = tkinter.Entry(öz.test1_frame , width = 10)
        öz.test1etiket.pack(side = "left")
        öz.test1giris.pack(side = "left")
        öz.test2etiket = tkinter.Label(öz.test2_frame, text = "Test2:")
        öz.test2giris = tkinter.Label(öz.test2_frame , width = 10)
        öz.test2etiket.pack(side = "left")
        öz.test2giris.pack(side = "left")
        öz.test3etiket = tkinter.Label(öz.test3_frame , text = "Test3:")
        öz.test3giris = tkinter.Entry(öz.test3_frame , width = 10)
        öz.test3etiket.pack(side = "left")
        öz.test3giris.pack(side = "left")
        öz.sonucetiketi = tkinter.Label(öz.ort_frame , text = "Ortalama:")
        öz.ort =tkinter.StringVar()
        öz.sonuc = tkinter.Label(öz.ort_frame , textvariable = öz.ort)
        öz.sonucetiketi.pack(side = "left")
        öz.sonuc.pack(side="left")
        öz.hesaplabutonu = tkinter.Button(öz.buton_frame , text = "Hesapla" , command = öz.hesaplama)
        öz.çıkışbutonu = tkinter.Button(öz.buton_frame , text = "Çıkış" , command = öz.pencerem.destroy)
        öz.hesaplabutonu.pack(side = "left")
        öz.çıkışbutonu.pack(side = "left")
        öz.test1_frame.pack()
        öz.test2_frame.pack()
        öz.test3_frame.pack()
        öz.ort_frame.pack()
        öz.buton_frame.pack()
        tkinter.mainloop()
    def hesaplama(öz):
        öz.test1 = float(öz.test1giris.get())
        öz.test2 = float(öz.test2giris.get())
        öz.test3 = float(öz.test3giris.get())
        öz.ort = (öz.test1+öz.test2+öz.test3) / 3.0
        öz.ortalama.set(öz.ort)
        ortalama =Ortalama()
"""
#Pencere içine tek satırlık metin yazma:
"""
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem , text ="Merhaba")
        öz.yazı.pack()
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#DİKDÖRTGEN İÇİNDE YAZI YAZMA:
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı = tkinter.Label(öz.pencerem, text ="Merhaba" , borderwidth = 1 , relied = "solid")
        öz.yazı.pack(ipadx=20 , ipady=20)
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#ipadx yazının etrafındaki çerçevenin boşluklarını belirliyor.
#padx pencerenin etrafındaki boşlukları belirliyor.(yazının çerçevesinin pencerenin çerçevesine oranını belirlemek için)
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.yazı1 = tkinter.Label(öz.pencerem, text = " Merhaba" , borderwidth = 20 , relief = "solid")
        #borderwidth büyük ihtimal yazının bulunduğu çerçevenin kalınlığı
        öz.yazı2= tkinter.Label(öz.pencerem , text = "Dünya" , borderwidth = 15, relief = "solid")
        öz.yazı1.pack(padx=10 , pady=10)
        öz.yazı2.pack(padx=10, pady=10)
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#PENCEREYİ BÖLME:
#TOP YAZDIĞIMIZ İÇİN ALT ALTA YAZDIRACAK.
import tkinter
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.frame1 = tkinter.Frame(öz.pencerem)
        öz.frame2 = tkinter.Frame(öz.pencerem)
        öz.yazı1 = tkinter.Label(öz.frame1 , text = "Halil")
        öz.yazı2 = tkinter.Label(öz.frame2 , text="Murat")
        öz.yazı1.pack(side = "top")
        öz.yazı2.pack(side = "top")
        öz.frame1.pack()
        öz.frame2.pack()
        tkinter.mainloop()
        sınıfım = Sınıfım()
"""
"""
#BUTON
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum = tkinter.Button(öz.pencerem , text = "TIKLA" , command = öz.tıkladım)
        öz.butonum.pack()
        tkinter.mainloop()
    def tıkladım(öz):
        tkinter.messagbox.showinfo("Uyarı" , "Tıkladığınız için teşekkürler.")
        sınıfım = Sınıfım()
"""
"""
#PENCEREYİ KAPATMA
import tkinter
import tkinter.messagebox
class Sınıfım:
    def __init__(öz):
        öz.pencerem = tkinter.Tk()
        öz.butonum = tkinter.Button(öz.pencerem, text ="TIKLA" , command = öz.tıkladım)
        öz.çıkışbutonu = tkinter.Button(öz.pencerem , text = "ÇIKIŞ" , command = öz.pencerem.destroy)
        öz.butonum.pack()
        öz.çıkışbutonu.pack()
        tkinter.mainloop()
    def tıkladım(öz):
        tkinter.messagebox.showinfo("Uyarı" , "Tıkladığınız için teşekkürler.")
        sınıfım =Sınıfım()
"""
"""
#PARA ATMA
import random
class para:
    def __init__(öz):
        öz.parayüzü = "yazı"
    def çarpıştır(öz):
        if random.randint(0,1) == 0:
            öz.parayüzü = "yazı"
        else:
            öz.parayüzü="tura"
    def yüzüal(öz):
        return öz.parayüzü

def main():
    param = para() #nesnenin adı = sınıfın adı
    print("Paranın yüzü şuan:" + param.yüzüal())
    print("Parayı atıyorum:")
    param.çarpıştır()
    print("Şimdi paranın yüzü:" + param.yüzüal() )
main()"""

# Bu bölümde daha önce belirttiğimiz gibi, bir nesnenin veri özellikleri özel olmalıdır,
# böylece yalnızca nesnenin yöntemleri doğrudan erişebilir. Bu, nesnenin veri
# özelliklerini kazara bozulmaya karşı korur. Ancak, önceki örnekte gösterilen Coin
#sınıfında sideup özelliği özel değildir. Ona, Coin sınıfı yöntemleri içinde olmayan ifadeler doğrudan erişebilir.
# bunuda " __ "koyarak yapıyoruz.

"""
#PARA ATMA2 ("DOSYAYA KAYDETMELİ")
import random
class Para:
    def __init__(öz):
        öz.__parayüzü = "yazı"
    def çarpıştır(öz):
        if random.randint(0,1) == 0:
            öz.__parayüzü = "yazı"
        else:
            öz.__parayüzü = "tura"
    def paranınyüzünüal(öz):
        return öz.__parayüzü
"""
"""
#ÜSTTE SINIIFIN YAZILI OLDUĞU KOD AÇIK DEĞİLSE SINIFIN İÇİNDE BULUNDUĞU DOSYAYI İMPORTLAYABİLİRİZ.
import c13 #import ettiğimiz şey kodun kayıtlı olduğu dosya
def main():
    param = c13.Para()

    print("Parayı 10 kere atacağım.")
    for a in range(10):
        param.çarpıştır()
        print(param.paranınyüzünüal())
main()"""

"""
#bankaccount  #KOD ÇALIŞMIYOR
class BankaHesabı:
    def __init__(öz,para):
        öz.__paramik = para
    def yükle(öz,miktar):
        öz.__paramik += miktar
    def çek(öz,miktar):
        if öz.__paramik>= miktar:
            öz.__paramik -= miktar
        else:
            print("Bu miktar çekilemez.")
    def bankadakimiktar(öz):
        return öz.__paramik

import c13
def main():
    param = float(input("Bankada ne kadar paranız var."))
    bankam = c13.BankaHesabı(param) #sınıfa bir değer atadık.
    ekle = float(input("ne kadar yüklemek istiyorsun:"))
    bankam.yükle(ekle)
    çekme = float(input("ne kadar para çekmek istiyorsun:"))
    bankam.çek(çekme)
    print(f"Banka hesabındaki son miktar: {param.bankadakimiktar()}")
main()
"""
"""
#BOZUK PARA ATMA ; 3 FARKLI NESNE TANIMLIYORUZ ; 3 FARKLI BOZUK PARANIN ATILMASI GİBİ OLUYOR
import c13
def main():
    coin1 = c13.Para()
    coin2 = c13.Para()
    coin3 = c13.Para()
    print(coin1.paranınyüzünüal())
    print(coin2.paranınyüzünüal())
    print(coin3.paranınyüzünüal())
    print()

    coin1.çarpıştır()
    coin2.çarpıştır()
    coin3.çarpıştır()

    print(coin1.paranınyüzünüal())
    print(coin2.paranınyüzünüal())
    print(coin3.paranınyüzünüal())
    print()
main()"""

"""
#TELEFON PY
class Telefon:
    def __init__(öz,üretici,model,fiyat):
        öz.__üretici=üretici
        öz.__model=model
        öz.__fiyat=fiyat
    def set_üretici(öz,üretici):
        öz.__üretici = üretici
    def set_model(öz,model):
        öz.__model=model
    def set_fiyat(öz,fiyat):
        öz.__fiyat = fiyat
    def get_üretici(öz,üretici):
        return öz.__üretici
    def get_model(öz,model):
        return öz.__model
    def get_fiyat(öz,fiyat):
        return öz.__fiyat

import c13
def main():
    üretici = input("Üreticiyi giriniz:")
    model = input("Modeli giriniz:")
    fiyat = float("Fiyatı giriniz:")
    telefon = c13.Telefon(üretici,model,fiyat)
    print("Girdiğin bilgiler:")
    print(f"{telefon.get_üretici()}")
    print(f"{telefon.get_model()}")
    print(f"{telefon.get_fiyat()}")
main()

#Bir Listede Nesneler Saklama
import c13
def main():
    telefonlar = liste_yap()
    print(f"Girdiğiniz bilgiler {listeyi_oynat(telefon_listesi)}")
def liste_yap():
    telefon_listesi = []
    print("5 tane telefon için bilgileri giriniz:")
    for a in range(1,6): #1 den başlayıp 5 e kadar yazdırır.
        print("Telefon numarası:" + str(a))
        üretici = input("Üreticiyi giriniz:")
        model = input("Modeli giriniz:")
        fiyat = input("Fiyatı giriniz:")
        print()
        telefon = c13.Telefon(üretici,model,fiyat)
        telefon_listesi.append(telefon)
        return telefon_listesi #LİSTEYİ DÖNDÜRMEYİ UNUTMA!
def listeyi_oynat(telefon_listesi):
    for item in telefon_listesi:
        print(item.get_üretici())
        print(item.get_model())
        print(item.get_fiyat())

main()"""
"""
#Sonuç olarak, nesneyi argüman olarak alan fonksiyon veya metod, gerçek nesneye erişim sağlar.
import c13
def main():
    param = c13.Para()
    print(param.paranınyüzünüal())
    flip(param) #FONKSİYONUN İÇİNE NESNEYİ KOYDUK
    print(param.paranınyüzünüal())
def flip(coin_obj):
    coin_obj.çarpıştır()
main()"""
"""
#NESNEYİ PİCKLELAMA:
import pickle
import c13
dosyaadı = "telefonum.dat" #dosya adını mainin dışına yazdık.
def main():
    again = "y"
    dosyayayaz = open(dosyaadı , "wb")
    while again =="y" or again=="Y":
        üretici = input("Üreticiyi giriniz")
        model = input("Modeli giriniz:")
        fiyat = input("Fiyatı giriniz:")
        telefon = c13.Telefon(üretici,model,fiyat)
        pickle.dump(telefon, dosyayayaz)
        again = input("Devam etmek için y ye basınız.")
    dosyayayaz.close()
    print("Bilgiler telefonum.dat dosyasına yazıldı.")
main()"""
"""
#UNPİCKLE TELEFON.py
import pickle
import c13
dosyaadı = "telfonum.dat"
def main():
    dosya_sonu = False
    dosyaya_gir = open(dosyaadı, "rb")
    while not dosya_sonu:
        try:
            telefon = pickle.load(dosya_gir)
            oynat(telefon)
        except EOFError:
        dosya_sonu = True
    dosyaya_gir.close()
def oynat(telefon):
    print(telefon.get_üretici())
    print(telefon.get_model())
    print(telefon.get_fiyat())
    print()
main()"""
"""
#İLETİŞİM
class İletişim:
    def __init__(öz,isim,telefon,mail):
        öz.__isim = isim
        öz.__telefon = telefon
        öz.__mail = mail
    def set_isim(öz,isim):
        öz.__isim =isim
    def set_telefon(öz,telefon):
        öz.__telefon = telefon
    def set_mail(öz,mail):
        öz.__mail = mail
    def get_isim(öz):
        return öz.__isim
    def get_telefon(öz)
        return öz.__telefon
    def get_mail(öz):
        return öz.__mail
"""
#__STR__ NE İŞE YARIYOR ANLAMADIM.
"""
#İLETİŞİM MANAGER:
import c13
import pickle
BAK = 1
EKLE = 2
DEĞİŞTİR = 3
SİL = 4
ÇIK = 5

dosyaadı = "iletişim.dat"
def main():
    iletişimlerim = yükleiletişim()
    choice = 0
    while choice != ÇIK:
        choice = seçimyap()
        if choice == BAK:
            bak(iletişimlerim)
        elif choice == EKLE:
            ekle(iletişimlerim)
        elif choice == DEĞİŞTİR:
            değiştir(iletişimlerim)
        elif choice == SİL:
            sil(iletişimlerim)
    iletişimleri_kaydet(iletişimlerim)
def yükleiletişim():
    try:
        dosyayagir = open(dosyaadı ,"rb")
        iletişim_sözlüğü = pickle.load(dosyayagir)
        dosyayagir.close()
    except IOError:
        iletişim_sözlüğü = {}
    return iletişim_sözlüğü
def seçimyap():
    print("Menü")
    print("1: BAK")
    print("2: EKLE")
    print("3: DEĞİŞTİR")
    print("4:SİL")
    print("5:ÇIK")
    choice = int(input("Yapmak istediğiniz işlemi seçiniz:"))
    while choice< BAK or choice>ÇIK:
        print("Geçerli bir sayı giriniz.")
        choice = int(input("Yapmak istediğiniz işlemi giriniz:"))
    return choice
def bak(iletişimlerim):
    name = input("İsim giriniz")
    print(iletişimlerim.get(name , "İsim bulunamadı"))
def ekle(iletişimlerim):
    name = input("İsim giriniz:")
    telefon = input("Telefon numarası giriniz:")
    mail = input("Eposta adresini giriniz:")
    gir = c13.İletişim(name,telefon,mail)
    if name not in iletişimlerim:
        iletişimlerim[name] = ekle
    else:
        print("İsim zaten mevcut")
def değiştir(iletişimlerim):
    name = input("İsim giriniz:")
    if name in iletişimlerim:
        telefon = input("Telefon numarası giriniz:")
        mail = input("Eposta adresini giriniz:")
        gir = c13.İletişim(name,telefon,mail)
        iletişimlerim[name] = gir
    else:
        print("İsim bulunamadı.")
def sil(iletişimlerim):
    name = input("İsim giriniz:")
    if name in iletişimlerim:
        del iletişimlerim[name]
    else:
        print("İsim bulunamadı.")
def iletişimleri_kaydet(iletişimlerim):
    dosyayagir = open(dosyaadı , "wb")
    pickle.dump(iletişimlerim , dosyayagir)
    dosyayagir.close()
main()"""

#OPTİON 11
#Miras, bir yeni sınıfın mevcut bir sınıfı genişletmesine olanak tanır.
#Yeni sınıf, genişlettiği sınıfın üyelerini miras alır.

#Bir nesne diğer bir nesnenin uzmanlaşmış bir versiyonu ise, aralarında bir "bir" ilişkisi bulunur.
#Örneğin, bir çekirge bir böcektir. İşte "bir" ilişkisinin birkaç örneği:
#Bir çiçek bir bitkidir.
#Bir dikdörtgen bir şekildir.
#Nesneler arasında bir "bir" ilişkisi varsa, bu, uzmanlaşmış nesnenin genel nesnenin
#tüm özelliklerine sahip olduğu ve onu özel kılan ek özelliklere sahip olduğu anlamına gelir.
#Nesne tabanlı programlamada, miras kullanılarak sınıflar arasında bir "bir" ilişkisi oluşturulur.
#Bu, bir sınıfın yeteneklerini başka bir sınıfın uzmanlaşmış bir versiyonunu oluşturarak genişletmenizi sağlar.
#Miras, bir üst sınıf (superclass) ve bir alt sınıf (subclass) içerir.
# Üst sınıf genel bir sınıftır ve alt sınıf uzmanlaşmış bir sınıftır.
# Alt sınıfı, üst sınıfın genişletilmiş bir versiyonu olarak düşünebilirsiniz.
# Alt sınıf, üst sınıftan özellikler ve yöntemler miras alır, bunların hiçbiri yeniden yazılmadan.
#Ayrıca, alt sınıfa yeni özellikler ve yöntemler eklenerek, onu üst sınıfın uzmanlaşmış bir versiyonu yapar.

"""
#YANİ İKİ CLASSI İÇ İÇE ŞEKİLDE YAZIYORUZ.
class otomobil:
    def __init__(öz,marka,model,km,fiyat):
        öz.__marka = marka
        öz.__model = model
        öz.__km = km
        öz.__fiyat = fiyat
    def set_marka(öz,marka):
        öz.__marka = marka
    def set_model(öz,model):
        öz.__model = model
    def set_km(öz,km): #sette yanına özden başka bir şey daha yazıyoruz. get de yazmıyoruz.
        öz.__km = km
    def set_fiyat(öz,fiyat):
        öz.__fiyat = fiyat
    def get_marka(öz):
        return öz.__marka
    def get_model(öz):
        return öz.__model
    def get_km(öz)
        return öz.__km
    def get_fiyat(öz):
        return öz.__fiyat
class araba(otomobil):
    def __init__(öz,marka,model,km,fiyat,kapı):
        otomobil.__init__(öz,marka,model,km,fiyat)
        öz.__kapı = kapı
    def set_kapı(öz,kapı):
        öz.__kapı=kapı
    def get_kapı(öz):
        return öz.__kapı
"""
"""
import c13
def main():
    ikinci_el =c13.araba("audi" ,2007, 12500,21500.0 , 4)
    print(ikinci_el.get_marka())
    print(ikinci_el.get_model())
    print(ikinci_el.get_km)
    print(ikinci_el.get_fiyat())
    print(ikinci_el.get_kapı())
main()"""
#def main() açarken üste dosya ismini import ediyoruz.

"""
#Aslında, metod geçersiz kılma örneğini zaten gördünüz.
#Bu bölümde incelediğimiz her alt sınıfın, üst sınıfın _ init _ metodunu geçersiz kılan bir
#_ init _ metoduna sahip olduğunu gördük.
class Mammal:
    def __init__(öz,species):
        öz.__species = species
    def show_species(öz):
        print("Im a" , öz.__species)
    def makesound(öz):
        print("grrr")

class Dog(Mammal):
    def __init__(öz):
        Mammal.__init__(öz,"dog")
    def makesound(öz):
        print("wof wof")
"""
# Bir özyinelemeli fonksiyon, kendini çağıran bir fonksiyondur.
#Fonksiyonların birbirlerini çağırma örneklerini gördünüz.
#Bir programda, ana fonksiyon fonksiyon A'yı çağırabilir, bu fonksiyon da fonksiyon B'yi çağırabilir.
#Aynı zamanda bir fonksiyonun kendini çağırması da mümkündür.
#Kendini çağıran bir fonksiyona özyinelemeli fonksiyon denir.
#Örneğin, Program 12-1'de gösterilen message fonksiyonuna bir göz atın.
"""
def main():
    mesaj()
def mesaj():
    print("devam")
    mesaj()
main()"""
#sonsuza kadar devam yazdırır

"""
def main():
    mesaj(5)
def mesaj(sayı):
    if sayı>0:
        print("selam")
        mesaj(sayı-1)
main() #5 kere selam yazdırır."""

