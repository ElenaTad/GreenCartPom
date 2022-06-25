from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import unittest

class Mango_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Service("C:\\webdriver\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls. driver.implicitly_wait(10)
        cls.river.maximize_window()


    def test_Mango(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[18]/div[3]/button').click()
        self.driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
        self.driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[text()='PROCEED TO CHECKOUT']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click
        self.driver.find_element(By.CSS_SELECTOR, "div.container div.products-wrapper:nth-child(2) div.products div:nth-child(4) > button:nth-child(14)").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class="chkAgree"]).click()
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/button').click()
        self.driver.find_element(By.XPATH,"//*[contains(text(), 'Thank you, your order has been placed successfully')]")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")