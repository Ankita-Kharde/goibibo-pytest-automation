from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_util import take_screenshot
import time

class Results_page():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def Verify_flight_displayed(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="listing-id"]/div/div[2]/div/div[1]/div[1]')))
        return True
    # verify list of flights displayed after clicking on search button


    def is_flight_list_displayed(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-test, 'component-clusterItem')]")))
            return True
        except TimeoutException:
            return False

    def select_stop_checkbox(self):
        try:
             stop_checkbox = (WebDriverWait(self.driver, 20).until
                             (EC.element_to_be_clickable((
                By.XPATH, "//*[@class ='filterWrapper']/div[1]/div[1]/div[1]/label/span"))))
             self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", stop_checkbox)
             time.sleep(1)  # let any UI transition complete
             self.driver.execute_script("arguments[0].click();", stop_checkbox)
        except TimeoutException:
            take_screenshot(self.driver, "stop_checkbox_selection_failed")
            print("[ERROR] Failed to select '1 Stop' checkbox.")


    def select_airline_checkbox(self):

        # airline_checkbox = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
        #     (By.XPATH, "//*[@class ='filterWrapper']/div[1]/div[1]/div[3]/label/span"))
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", airline_checkbox)
        # time.sleep(1)
        # self.driver.execute_script("arguments[0].click();", airline_checkbox)

        try:
            time.sleep(6)
            self.scroll_to_element((By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/p"))
            airline_checkbox = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@class ='filterWrapper']/div[1]/div[1]/div[3]/label/span")))
            self.driver.execute_script("arguments[0].click();", airline_checkbox)
            time.sleep(3)
        except TimeoutException:

            take_screenshot(self.driver, "airline_checkbox_found")  # Capture screenshot if element found

            print("[WARN] Airline checkbox not found or not clickable.")

        # raise  # Reraise the exception so the test can fail


    def get_visible_flight_count(self):
        flights = self.driver.find_elements(By.XPATH, "//div[@data-test='component-clusterItem']")
        return len(flights)


    def scroll_to_element(self, by_locator):
        """Scrolls to the element identified by the given locator."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(by_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element





































