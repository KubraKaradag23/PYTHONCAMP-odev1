from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec #bekleme fonksiyonlarına şart ekleyeceğiz
from selenium.webdriver.common.action_chains import ActionChains

class Sauce:
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
    
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        #driver 5 saniye beklesin user-name alanı visibile olana kadar
        # loginBtn=driver.find_element(By.XPATH("/html/body/header/div/div/div/div/ul/li[3]/a"))
        #loginBtn.click()
        usernameInput=self.driver.find_element(By.ID,("user-name"))
        passwordInput=self.driver.find_element(By.ID,("password"))
      
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,("//*[@id='login_button_container']/div/form/div[3]/h3"))
        testResults=errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {testResults}")
        

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput=self.driver.find_element(By.ID,("user-name"))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,("password"))
        
        #ActionChains
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() #acion classının çalıştığı alan
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)") #sayfayı en aşağı kaydırır
        sleep(20)
           

testClass=Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()


-----------------------
pytest
-----------------------

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec #bekleme fonksiyonlarına şart ekleyeceğiz
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_DemoClass:
    #pytestte init fonksiyon kullanılmaz.
    #her testten önce çağrılır.
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    #günün tarihini al bu tarih ile bir klasör var mı kontrol et yolsa oluştur.
        self.folderPath=str(date.today()) #testler çalıştırıldığı her an o günün tarihini alıp o tarihle klasörde tuttar
        Path(self.folderPath).mkdir(exist_ok=True) #o tarihte klasör var mı diye kontrol edr
    #her testten sonra çağırılır.
    def teardown_method(self):
        self.driver.quit()
        
    
    #setup --> test_demofunc --> teardown
    def test_demoFunc(self):
        #3a act arrange assert
        text="Hello"
        assert text=="Hello"

    def demoFunc(self):   #önünde test olan prefixler çalıştırılır 
        print("demoFunc")

    #setup --> test_demo2 --> teardown
    def test_demo2(self):
        assert True

    #@pytest.mark.skip() #ilgili fonksiyonu atlamasını istiyoruz
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,("user-name"))
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput=self.driver.find_element(By.ID,("password"))
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,("//*[@id='login_button_container']/div/form/div[3]/h3"))
        #self.driver.save_screenshot(self.folderPath+"/test-invalid-login.png")
        #bu şekilde sürekli aynı isimde ekran görüntüsü alır.

        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")

        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        #assert testin sonuçlanmasını sağlıyor.Eğer eşitlik sağlanırsa test başarılıdır.
    
    def waitForElementVisible(self,locater,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locater))
                                        
