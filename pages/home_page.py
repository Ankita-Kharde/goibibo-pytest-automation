from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def Open(self):
        self.driver.get("https://www.goibibo.com")
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='logSprite icClose']")))
            close_btn.click()
        except Exception as e:
            print("No popup to close:", e)


    def enter_trip_deatils(self, source, destination, travel_date):
        #one way selected by default
        # self.wait.until(EC.element_to_be_clickable((By.XPATH,"//p[text()='One-way']")))
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "sc-jlwm9r-6 sc-jlwm9r-7 jTFFXm fXSZVc")))
        except:
            pass


        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='From']")))
        from_input = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='sc-12foipm-22 kGtxGm']//p[@class='sc-12foipm-6 erPfRs'][normalize-space()='Enter city or airport']")))
        from_input.click()

        from_input_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        from_input_input.send_keys(source)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@id="autoSuggest-list"]/li[1]'))).click()


        # # Click and enter to city
        to_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        self.driver.execute_script("arguments[0].click();", to_input)
        to_input.clear()
        to_input.send_keys(destination)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text() = 'Mumbai, India']"))).click()


        # date pick
        self.driver.find_element(By.XPATH, "//*[text()='Departure']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@aria-label="{travel_date}"]'))).click()

        self.driver.find_element(By.XPATH, "//*[text()='SEARCH FLIGHTS']").click()

# validation
        try :
         WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Flights from ']" )))

        except :
            print("[ERROR] 'Flights from' text not found. Check if the page loaded properly or if the text changed.")



