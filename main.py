from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
import os


def clean():
    if os.path.exists('./out'):
        for f in os.listdir('./out'):
            os.remove(os.path.join('./out', f))


def scrape(category, scrolls=5):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(f'https://unsplash.com/s/photos/{category}')

    for i in range(scrolls):
        images = driver.find_elements_by_tag_name('img')

        for i, img in enumerate(images):
            source = img.get_attribute("src")

            if "profile" in source:
                continue

            img_data = requests.get(source).content
            with open(f'./out/{category}-{i}.jpg', 'wb') as handler:
                handler.write(img_data)

        print(f"Download batch {i}")

        driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight-2000)")

        try:
            loadMoreButton = driver.find_element_by_xpath(
                "//button[text()='Load more photos']")
            loadMoreButton.click()
        except:
            print("No button to press")

        print('Loaded more photos')
        time.sleep(10)


clean()
scrape('cars')
