from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests


def scrape(category):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(f'https://unsplash.com/s/photos/{category}')

    images = driver.find_elements_by_tag_name('img')

    for i, img in enumerate(images):
        source = img.get_attribute("src")
        print(source)

        if "profile" in source:
            continue

        img_data = requests.get(source).content
        with open(f'./out/{category}-{i}.jpg', 'wb') as handler:
            handler.write(img_data)


scrape('cars')
