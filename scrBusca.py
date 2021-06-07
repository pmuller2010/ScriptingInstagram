'''

https://github.com/MariyaSha/WebscrapingInstagram/blob/main/WebscrapingInstagram_completeNotebook.ipynb

Aca busca aunque la palabra no este, porque hace dos enter en buscar.
'''

# imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time
import os
import wget


# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('F:/GitHub/ScrInstagram/chromedriver.exe')

# open the webpage
driver.get("http://www.instagram.com")

# target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# enter username and password
username.clear()
username.send_keys("")
password.clear()
password.send_keys("")

# target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

# We are logged in!

# nadle NOT NOW
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Ahora no")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Ahora no")]'))).click()


# target the search input field
searchbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Busca']")))
searchbox.clear()

# search for the hashtag cat
keyword = "#sex"
searchbox.send_keys(keyword)

# Wait for 5 seconds
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

# scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

# target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]

print('Number of scraped images: ', len(images))


path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

# create the directory
os.mkdir(path)

path

# download images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
