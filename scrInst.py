'''
pip install selenium

https://github.com/MariyaSha/WebscrapingInstagram/blob/main/ImageExtracting_bot.ipynb

En este caso tiene que estar en el resultado de la busque la palabra que se busco, porque hace click sobre esa palabra.
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

path = os.getcwd()

# driver = webdriver.Chrome('F:/GitHub/ScripyngInstagram/chromedriver.exe')
driver = webdriver.Chrome(path + '\chromedriver.exe')

driver.get('https://www.instagram.com')


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
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Ahora no")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Ahora no")]'))).click()


# target the search input field
searchbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Busca']")))
searchbox.clear()

# search for the hashtag cat
keyword = "#comida"
searchbox.send_keys(keyword)

# searchbox.send_keys(Keys.ENTER)

# FIXING THE DOUBLE ENTER
time.sleep(5)  # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

n_scrolls = 2
for j in range(0, n_scrolls):
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(5)

# target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
# narrow down all links to image links only
anchors = [a for a in anchors if str(
    a).startswith("https://www.instagram.com/p/")]

print('Found ' + str(len(anchors)) + ' links to images')
anchors[:5]

images = []

# follow each image link and extract only image at index=1
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])
    print(a)

images[:5]


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
