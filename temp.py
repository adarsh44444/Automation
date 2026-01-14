from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Uncomment below for headless execution (cron/servers)
# chrome_options.add_argument("--headless=new")

# Setup WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

try:
    url = "https://www.cricbuzz.com/"
    driver.get(url)

    # Wait for page to load
    time.sleep(5)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"cricbuzz_{timestamp}.png"

    # Take screenshot
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
