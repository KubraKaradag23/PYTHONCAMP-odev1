# Generated by Selenium IDE
import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

class TestSaucedemo():
  def setup_method(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.maximize_window()
    self.driver.get("https://www.saucedemo.com/")
    #self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()

  @pytest.mark.parametrize("username,password",[(" "," "),("1"," "),(" ","1"),("1","1"),("standard_user","secret_sauce")])
  def test_saucedemo(self,username,password):
    userName=self.driver.find_element(By.ID,("user-name"))
    passWord=self.driver.find_element(By.ID,("password"))
    userName.send_keys(username)
    passWord.send_keys(password)
    loginBtn=self.driver.find_element(By.ID,("login-button"))
    loginBtn.click()
    product=self.driver.find_element(By.XPATH,("//*[@id='add-to-cart-sauce-labs-backpack']"))
    product.click()
    product_two=self.driver.find_element(By.XPATH,("//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"))
    product_two.click()
    product_two=self.driver.find_element(By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")
    product_two.click()
    shopping=self.driver.find_element(By.CLASS_NAME,("shopping_cart_link"))
    shopping.click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("1")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    self.driver.find_element(By.ID, "logout_sidebar_link").click()

  def waitForElementVisible(self,locater,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locater))
  
