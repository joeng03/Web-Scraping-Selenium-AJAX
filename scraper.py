import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def download_checker():
    for i in os.listdir("C:\\Users\\user\\Downloads\\Songs")[:3]:
        if ".crdownload" in i:
            time.sleep(0.1)
            download_checker()
def scrape(path):
    prefs = {"download.default_directory":path}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=r'C:\STUFF\chromedriver_win32 (1)\chromedriver.exe',options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.mp3juices.cc/')
    songs=["bohemian rhapsody","castle on the hill","everything i wanted"]
    for song in songs:
        search_box = driver.find_element_by_name('query')
        search_box.clear()
        search_box.send_keys(song+' '+'lyrics')
        search_box.submit()
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        button=driver.find_element_by_link_text('Download')
        driver.execute_script("arguments[0].click();",button)
        wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        url = driver.find_element_by_class_name('url')
        driver.execute_script("arguments[0].click();", url)
        #Close popup tabs that might appear
        if(len(driver.window_handles)==2):
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w')
    download_checker()
    driver.quit()

if __name__ == "__main__":
    scrape("C:\\Users\\user\\Downloads\\Songs")
