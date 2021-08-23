from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import os

path = "C:\Program Files (x86)\chromedriver.exe"

isExist = os.path.exists(path)
print(isExist) # Prints True if file is in right place, prints false if not

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://github.com/login")

start_time = time.time()

button = driver.find_element_by_id("login_field")

# PUT YOUR USERNAME HERE
button.send_keys("USERNAME")

button = driver.find_element_by_id("password")

# PUT YOUR PASSWORD HERE
button.send_keys("PASSWORD")

button = driver.find_element_by_name("commit")
button.click()

time.sleep(3)
# PUT YOUR PROFILE LINK HERE 
driver.get("https://github.com/ExTTT")


while True:
    text = driver.find_element_by_partial_link_text("following")
    text.click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/span/form[2]/input[2]  ')\
        .click()
    time.sleep(3)
    
    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/span/form[2]/input[2]')\
        .click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[3]/div[3]/span/form[2]/input[2]')\
        .click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[4]/div[3]/span/form[2]/input[2]')\
        .click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[5]/div[3]/span/form[2]/input[2]')\
        .click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[6]/div[3]/span/form[2]/input[2]')\
        .click()
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[4]/main/div[2]/div/div[2]/div[2]/div/div[7]/div[3]/span/form[2]/input[2]')\
        .click()
    time.sleep(3)
    
driver.quit()
