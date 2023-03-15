#değişkenler
faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

#Tip dönüşümleri
#type kullanımı ile değişkenin veri tipini öğrenebiliriz.

print(type(faiz)) #float
print(type(vade)) #int
print(type(krediAdi)) #str

#dönüşümler
#float olan değişken int olarak dönüştü ve değer tamsayılık kısım olarak alınır.
print(int(faiz)) 

print (int(vade)+12)

# NOT: string değerler int değelere dönüştürülemez.
#print(int(krediAdi))

#float değer tipi str ye dönüştürüldükten sonra type kontrolü
faiz=str(faiz)
print(type(faiz))

#Kullanıcı input değerinin istenmesi
#--> vade=input("Lütfen istediğiniz vade sayısını giriniz! : ")

#Kullanıcıdan alınan input değeri default olarak str değişkeninde tutulur.
print(type(vade))
#Yöntem 1 --> print(int(vade)+12)

#Yöntem 2
#vade=int(input("Lütfen istediğiniz vade sayısını giriniz! : "))
#vade=vade+12

#string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade
#Yöntem 1 --> print("sectiginiz vade sonucu ortaya cikan vade: "+str(vade))

#Yöntem 2 --> print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}" .format(vadeSayisi=vade))

isim="Kübra"
#Yöntem 3 --> .format
#name gördüğün yere format parantezleri içerisinde girilen değeri ver.
#metin="Merhaba {name}".format(name="SENEM")


#yöntem 4 --> f-string
#parantezler içerisinde kod yazıyormuşuz gibi düşünüyoruz. 1+1 gibi ifadeler de yazılabilir.
metin=f"merhaba {isim}"
print(metin)

#listeler -->verilerin liste grup olarak saklanmasını sağlar.
#dizilerde farklı data tipinde elemanlar tanımlanabilir.
dizi=["Kübra",10,5.5,True]

krediler=["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]

print(type(krediler))
print(krediler[0])

#krediler dizininn eleman sayısını len anahtar kelimesi ile görebiliriz.
print(len(krediler))

#listenin sonuna yeni bir index ekler
krediler.append("bireysel kredi")
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)

#listeden bir index çıkarma işlemii remove ile yapabiliriz.
#çıkarılmak istenilen indexten 2 adet var ise ilk değeri siler
krediler.remove("taşıt kredisi")
print(krediler)

#birden fazla index eklemek için extend
krediler.extend(["x kredisi","y kredisi"])
print(krediler)

#defaut olarak son elemanı siler
krediler.pop()
print(krediler)

#döngüler
#for

for i in range(10): #0 dan 10 kadar 10 dahil olmamak üzere çalıştırılır.
    print("xxx")
    print(i)

print("*******")

for i in range(5,10): #for döngümü başlatacağım sayıyı belirtme için kullanılan yöntem
    print(i) 

print("*******")

for i in range(5,51,10): #3. değer sayının kaçar kaçar arttırması gerektiğini götermek için 
    print(i)

print("*******")

for kredi in krediler:
    print(kredi)

print("*******")

for i in range(len(krediler)):
    print(krediler[i])

print("*******")

#döngüler

i=0
while i<10:
    print(i)
    i+=1

print("*******")

while True:
    print("X")
    break        #break ile sonsuz döngü sona erdirilir.

print("*******")

i=0
while i<len(krediler):
    if krediler[i] =="taşıt kredisi": #i. index taşıt kredisine eşit olduğunda döngüyü sonlandır
        break
    print(krediler[i])
    i+=1

print("*******")

i=0
while i<len(krediler):
    i+=1
    print(krediler[i])
    if krediler[i] =="taşıt kredisi": #i. index taşıt kredisine eşit olduğunda döngüyü sonlandır
        break

print("*******")

#fonksiyonlar

fiyat = 100
indirim= 20

#def define --> anaktar kelimesi ile fonksiyonlar tanımlanır.

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim): #parantez içerisinde yazılan değerler parametre aldığını gösterir.
    print(fiyat-indirim)

calculate() #fonksiyon çağırılır.
calculateWithParams(90,20)

print("*******")

def sayHello(name):
    print(f"merhaba {name}")

sayHello("Kübra")

print("*******")

#değer dönen fonsksiyon

def claculateAndReturn(price,discount):
    return price-discount #print yazılsa sadece değer basar return ile geriye bir değer döndürüp değişken olarak kullanabiliriz.

yeniFiyat=claculateAndReturn(70,10)
print(yeniFiyat)
