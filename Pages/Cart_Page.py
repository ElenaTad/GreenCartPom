class Cart_Page

    def __init__(self, driver):
        self.driver = driver

        self.place_order_button_xpath="//button[contains(text(),'Place Order')]"

    def place_order
        self.driver.find_element(By.XPATH, self.place_order_button_xpath).click
 