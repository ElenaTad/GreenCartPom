class HomePage():

    def __init__(self, driver):
        self.driver = driver

    self.mango_button_xpath = "//*[@id="root"]/div/div[1]/div/div[18]/div[3]/button"
    self.cart_button_css = "img[alt='Cart']"
    self.proceed_checkout_button_xpath="//button[contains(text(),'PROCEED TO CHECKOUT')]"

    def select_mango(self, mango):
        self.driver.find_element(By.XPATH, self.mango_button_xpath).click()

    def open_cart(self,cart):
        self.driver.find_element(By.CSS_SELECTOR, self.cart_button_css).click()

    def proceed_checkout(self):
        sself.driver.find_element(By.XPATH,self.proceed_checkout_button_xpath).click




