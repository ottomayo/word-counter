from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def get_wikipedia(num_of_pages):
    driver_path = r'C:\Program Files (x86)\chromedriver.exe'

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("–-disable-notifications")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.set_window_size(1050, 708)
    wait = WebDriverWait(driver, 600)

    text = []
    for i in range(num_of_pages):
        driver.get('https://en.wikipedia.org/wiki/Special:Random')
        text.append(wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'body'))).text)
        print(i)

    driver.quit()

    return ' '.join(text).split()
