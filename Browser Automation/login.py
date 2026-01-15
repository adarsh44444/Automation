from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def get_driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys("automated")
    wait.until(EC.presence_of_element_located((By.ID, "id_password"))).send_keys(
        "automatedautomated" + Keys.RETURN
    )

    # Click Home after login
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/a"))).click()

    # Explicit wait of 5 seconds (as requested)
    time.sleep(5)

    # Save screenshot in current directory
    screenshot_path = os.path.join(os.getcwd(), "after_login.png")
    driver.save_screenshot(screenshot_path)

    print("Screenshot saved at:", screenshot_path)

    driver.quit()

if __name__ == "__main__":
    main()
