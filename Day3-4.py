####################################################################################################
#mathematic.py

def topla(a,b):
    return a + b
    
def bol(a,b):
    return a / b
    
####################################################################################################    
#module.py

#alias -> mathematic'i dosya içinde kullanırken m olarak isimlendiriyoruz
#import mathematic as m 
from mathematic import topla as toplamaIslemi #tüm modulu değil belirli fonksiyonun import edilmedisi
from day3 import Human
from seleniumExample import webdriver
#built-in modules
import random
#packages

#print(m.bol(90,3))
print(toplamaIslemi(10,20)) #direk fonksiyon import edildiğinde fonksiyon adı ile çağırabiliriz.

print(random.randint(0,100))

human1=Human("Halo")
human1.Talk("Merhaba")

chromeDriver = webdriver.Chrome()

#####################################################################################################
#seleniumExample.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(ChromeDriverManager().install()) #web driver oluşturuyoruz.

driver.maximize_window() #ekranın büyüklüğüü ayarlar genelde browser altına eklenmelidir.

driver.get("https://www.google.com.tr/") #gideceğimiz adresi yazıyoruz

input=driver.find_element(By.NAME,"q") #ilgili elementin adı bunu chromedan f12 ile bulduk
input.send_keys("kodlamaio") #inputun içine yazı yazmak için kullanılır.

searchButton=driver.find_element(By.NAME,"btnK") #butonu buluyoruz 
sleep(2) #kod direk çalıştığı zaman belirli nedenlerden dolayı(internet hızı, arama sonuçlar vb) input bulunamaz ve hata verilir.
#sleep kullanımı verimli bir çözüm değildir.
searchButton.click() #click fonksiynu ile arama yapıyoruz
sleep(2) #sonuçlar gelene kadar uygulamanın uyuması lazım
#arama sonucunda sayfaya giriş yaptırıyoruz
#Tıklanacak yeri f12 ile bulduktan sonra copy diyoruz.
#full Xpath -> /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a
#Xpath ->//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a ->input değerinden sonra bakar
firstResult=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCources=driver.find_elements(By.CLASS_NAME,"course-listing") #liste şeklinde dönüş yapar

#web scraping
#data scraping -> sitelerden veri kazıma
print(f"Kodlamaio sitesinde {len(listOfCources)} tane kurs bulunmaktadır")
#sleep(10)

while True:
    continue

#html locaters

###########################################################################################################################

#TestSauce.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(ChromeDriverManager().install()) #web driver oluşturuyoruz.

driver.maximize_window() #ekranın büyüklüğüü ayarlar genelde browser altına eklenmelidir.

driver.get("https://www.google.com.tr/") #gideceğimiz adresi yazıyoruz

input=driver.find_element(By.NAME,"q") #ilgili elementin adı bunu chromedan f12 ile bulduk
input.send_keys("kodlamaio") #inputun içine yazı yazmak için kullanılır.

searchButton=driver.find_element(By.NAME,"btnK") #butonu buluyoruz 
sleep(2) #kod direk çalıştığı zaman belirli nedenlerden dolayı(internet hızı, arama sonuçlar vb) input bulunamaz ve hata verilir.
#sleep kullanımı verimli bir çözüm değildir.
searchButton.click() #click fonksiynu ile arama yapıyoruz
sleep(2) #sonuçlar gelene kadar uygulamanın uyuması lazım
#arama sonucunda sayfaya giriş yaptırıyoruz
#Tıklanacak yeri f12 ile bulduktan sonra copy diyoruz.
#full Xpath -> /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a
#Xpath ->//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a ->input değerinden sonra bakar
firstResult=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCources=driver.find_elements(By.CLASS_NAME,"course-listing") #liste şeklinde dönüş yapar

#web scraping
#data scraping -> sitelerden veri kazıma
print(f"Kodlamaio sitesinde {len(listOfCources)} tane kurs bulunmaktadır")
#sleep(10)

while True:
    continue

#html locaters
