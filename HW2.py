#**********************************
#ÖĞRENCİ KAYIT SİSTEMİ
#HOMEWORK2
#
#**********************************

ogrenciListesi=["kadir kat", "orçun ok"]

#OGRENCI KAYIT
def ogrenciKayit(x):
    
    ogrenciListesi.append(ogrenci)
    
    return ogrenciListesi
 

#ÖĞRENCİ KAYIT KONTROLÜ
def ogrenciKontrol(ogrenci):
    i = 0
    while i <= len(ogrenciListesi):
        if ogrenciListesi[i] == ogrenci :
            print("Öğrenci sistemde mevcuttur")
            
        else:
            ogrenciKayit(ogrenci)
            print("Öğrenci kaydı alınmıştır.")
        i+=1
        break
        
    return ogrenciListesi

#ÖĞRENCİ NUMARASI ÖĞRENME
def ogrenciNo():
    ogrenci=(input("Öğrenmek istediğiniz öğrenci ad ve soyadını giriniz= "))
    
    if ogrenci in ogrenciListesi :
        no=ogrenciListesi.index(ogrenci)
        print(f"Öğrencinin numarası: {no+1}")
            
    else:
        print("Öğrenci bulunamadı.")
    
    return ogrenciListesi 

#ÖĞRENCİ LİSTESİ
def ogrenciListele():
    
    print(ogrenciListesi)
    
    return


#OGRENCİ SİLME
def ogrenciSil():
    sayi=int(input("Silinecek öğrenci sayısını giriniz: "))
    i=1
    while i <= sayi:
        ogrenciSilinecek=input("Lütfen silinecek öğrencinin ad ve soyadını giriniz: ")
        if ogrenciSilinecek in ogrenciListesi:
            ogrenciListesi.remove(ogrenciSilinecek)
            print("1 kayıt silinmiştir.")
            print(ogrenciListesi)
        else:
            print("öğrenci kaydı bulunamadı")
        i+=1
        break
        
    return
       

#Kayıt edilecek öğrenci adı kullanıcıdan istenir.
ogrenciEklenecek=int(input("Eklenemek istediğiniz öğrenci sayısını giriniz: "))
for i in range(ogrenciEklenecek):
    ogrenci=(input("Lütfen öğrenci adı giriniz "))
    ogrenciKontrol(ogrenci)
    
    
ogrenciListele()
ogrenciNo()   
ogrenciSil()




