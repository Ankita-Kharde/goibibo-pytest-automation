import time
from selenium.common import TimeoutException
from utils.screenshot_util import take_screenshot
from pages.home_page import HomePage
from pages.results_page import Results_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_goibibo_flight_search(driver):
    # Initialize the Home Page and open the Goibibo website
    home = HomePage(driver)
    home.Open()

    # Enter trip details: source, destination, and travel date
    home.enter_trip_deatils('Pune', 'Mumbai', 'Sat May 10 2025')


    # Handle "Got it" popup if it appears
    try:
        popup_close_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'GOT IT')]"))
        )
        popup_close_btn.click()
    except TimeoutException:
        pass

    # Initialize the Results Page
    results = Results_page(driver)

    # Assert that flight results are displayed
    assert results.Verify_flight_displayed(), "[ERROR] No flights displayed after search"

    # Take screenshot of the initial flight count
    take_screenshot(driver, "initial_flight_count")


    # Handle coachmark popup if it appears
    try:
        coachmark = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='coachmark-overlay-button']"))
        )
        driver.execute_script("arguments[0].click();", coachmark)
    except TimeoutException:
        pass        # Coachmark not present, safe to continue

    # Scroll to the filter section on the results page
    results.scroll_to_element((By.XPATH, "//p[contains(text(),'Popular Filters')]"))

    # Select the stop checkbox filter (e.g. 1 Stop)
    results.select_stop_checkbox()
    time.sleep(2)
    take_screenshot(driver, "stop_checkbox_selection")

    # Select the airline checkbox filter (optional step)
    results.select_airline_checkbox()
    time.sleep(5)
    take_screenshot(driver,"Air india checkbox_selection")


# Get and print count of flights currently visible
    count = results.get_visible_flight_count()
    print(f"[INFO] Number of flights displayed: {count}")
