######################################################
#Python & Selenium Yazılım Geliştirici Yetiştirme Kampı 4. Gün HW3
#
# Username , password kontrolü
# Urun sayısı kontrolü
# Geçerli geçersiz login
#
#####################################################
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

class HW3:
    
    
    def userNameControl(self):

        loginBtn=driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        
        errorMessage=driver.find_element(By.XPATH,("//*[@id='login_button_container']/div/form/div[3]/h3"))
        testResults=errorMessage.text == "Epic sadface: Username is required"
        print(f"User name boş ise=Epic sadface: Username is required --> {testResults}")

    def passwordControl(self):

        userName=driver.find_element(By.ID,("user-name"))
        #passwordInput=driver.find_element(By.ID,("password"))
        userName.send_keys("1")
        #passwordInput.send_keys(" ")
        #sleep(2)
        loginBtn=driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResults=errorMessage.text == "Epic sadface: Password is required"
        print(f"Password boş ise hata: Epic sadface: Password is required--> {testResults}")

    def userLogin(self):

        userName=driver.find_element(By.ID,("user-name"))
        password=driver.find_element(By.ID,("password"))
        userName.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        
        loginBtn=driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResults=errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Uyarı mesajı: Epic sadface: Sorry, this user has been locked out.--> {testResults} ")
        


    def inputControl(self):

        userName=driver.find_element(By.ID,("user-name"))
        password=driver.find_element(By.ID,("password"))
        userName.send_keys(" ")
        password.send_keys(" ")
        sleep(2)
        loginBtn=driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        errorMessageBtn=driver.find_element(By.CLASS_NAME,("error-button"))
        errorMessageBtn.click()
        sleep(3)

    def standart_user(self):
        userName=driver.find_element(By.ID,("user-name"))
        password=driver.find_element(By.ID,("password"))
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(5)

    def urunKontrol(self):
        userName=driver.find_element(By.ID,("user-name"))
        password=driver.find_element(By.ID,("password"))
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        urunSayisi=driver.find_elements(By.CLASS_NAME,("inventory_item_name"))
        print(f"Urun sayisi= {len(urunSayisi)}")


hw3=HW3()
hw3.userNameControl()
hw3.passwordControl()
hw3.userLogin()
hw3.inputControl()
hw3.standart_user()
hw3.urunKontrol()

