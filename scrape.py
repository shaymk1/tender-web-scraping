import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import service
import time


def scrape_website(website):
    print("launching a website")

    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.ChromeService(service=service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("website loaded..")
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()