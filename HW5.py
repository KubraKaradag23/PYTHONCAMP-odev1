######################################################
#Python & Selenium Yazılım Geliştirici Yetiştirme Kampı 5. Gün HW5
#
# PYTEST
# 
# 
#
#####################################################
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date


class Test_HW5:
    
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) 
    
    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.skip()
    def test_userNameControl(self):
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,("//*[@id='login_button_container']/div/form/div[3]/h3"))
        testResults=errorMessage.text == "Epic sadface: Username is required"
        print(f"User name boş ise=Epic sadface: Username is required --> {testResults}")

    @pytest.mark.skip()
    def test_passwordControl(self):
        userName=self.driver.find_element(By.ID,("user-name"))
        userName.send_keys("1")
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResults=errorMessage.text == "Epic sadface: Password is required"
        print(f"Password boş ise hata: Epic sadface: Password is required--> {testResults}")

    @pytest.mark.skip()
    def test_userLogin(self):

        userName=self.driver.find_element(By.ID,("user-name"))
        password=self.driver.find_element(By.ID,("password"))
        userName.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResults=errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        #self.driver.save_screenshot(f"{self.folderPath}/test-locked-login.png")
        assert testResults==True
        
        
        

    @pytest.mark.parametrize("username,password",[(" "," "),("1"," "),("locked_out_user","secret_sauce")])
    def test_inputControl(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userName=self.driver.find_element(By.ID,("user-name"))
        self.waitForElementVisible((By.ID,"password"))
        passWord=self.driver.find_element(By.ID,("password"))
        userName.send_keys(username)
        passWord.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-login-{username}-{password}.png")
        errorMessageBtn=self.driver.find_element(By.CLASS_NAME,("error-button"))
        errorMessageBtn.click()
        

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_standart_user(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userName=self.driver.find_element(By.ID,("user-name"))
        self.waitForElementVisible((By.ID,"password"))
        passWord=self.driver.find_element(By.ID,("password"))
        userName.send_keys(username)
        passWord.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"//*[@id='item_3_title_link']/div"))
        product=self.driver.find_element(By.XPATH,("//*[@id='add-to-cart-sauce-labs-backpack']"))
        product.click()
        product_two=self.driver.find_element(By.XPATH,("//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"))
        product_two.click()
        shopping=self.driver.find_element(By.CLASS_NAME,("shopping_cart_link"))
        shopping.click()
        checkout=self.driver.find_element(By.ID,("checkout"))
        checkout.click()
        conti=self.driver.find_element(By.ID,("continue"))
        conti.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-cartInfoEmpty.png")

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_remove_cart(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userName=self.driver.find_element(By.ID,("user-name"))
        self.waitForElementVisible((By.ID,"password"))
        passWord=self.driver.find_element(By.ID,("password"))
        userName.send_keys(username)
        passWord.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"//*[@id='item_3_title_link']/div"))
        product=self.driver.find_element(By.XPATH,("//*[@id='add-to-cart-sauce-labs-backpack']"))
        product.click()
        shopping=self.driver.find_element(By.CLASS_NAME,("shopping_cart_link"))
        shopping.click()
        product_remove=self.driver.find_element(By.XPATH,("//*[@id='remove-sauce-labs-backpack']"))
        product_remove.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-cartEmpty.png")

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_logout(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        userName=self.driver.find_element(By.ID,("user-name"))
        self.waitForElementVisible((By.ID,"password"))
        passWord=self.driver.find_element(By.ID,("password"))
        userName.send_keys(username)
        passWord.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"//*[@id='item_3_title_link']/div"))
        menu=self.driver.find_element(By.XPATH,("//*[@id='react-burger-menu-btn']"))
        menu.click()
        logout=self.driver.find_element(By.ID,("logout_sidebar_link"))
        logout.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-logout.png")

    
    def test_urunKontrol(self):
        userName=self.driver.find_element(By.ID,("user-name"))
        password=self.driver.find_element(By.ID,("password"))
        userName.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn=self.driver.find_element(By.ID,("login-button"))
        loginBtn.click()
        sleep(2)
        urunSayisi=self.driver.find_elements(By.CLASS_NAME,("inventory_item_name"))
        print(f"Urun sayisi= {len(urunSayisi)}")
        self.driver.save_screenshot(f"{self.folderPath}/test-inventory_items.png")

    def waitForElementVisible(self,locater,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locater))


hw3=Test_HW5()


