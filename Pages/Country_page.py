class CountryPage()

    def __init__(self, driver):
        self.driver = driver

    self.agree_terms_checkbox_css = "input[class="chkAgree"]
    self.proceed_button_xpath = //*[@id="root"]/div/div/div/div/button'
    self.succes_message_xpath = "//*[contains(text(), 'Thank you, your order has been placed successfully')]"


    def checkagree(self):
        self.driver.find_element(By.CSS_SELECTOR, self.agree_terms_checkbox_css).click

    def proceed(self):
        self.driver.find_element(By.XPATH, self.proceed_button_xpath).click()

   def success():
       self.driver.find_element(By.XPATH, self.succes_message_xpath)













































