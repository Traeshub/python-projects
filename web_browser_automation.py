from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
import time

#website desired to automate
driver.get("https://www.google.com/")
WebDriverWait(driver, 5.00).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Interacting w the website and searching via HTML

input_field = driver.find_element(By.CLASS_NAME, "gLFyf")
input_field.send_keys("NFL")
input_field.send_keys(Keys.ENTER)
# this allow you to press buttons on the browser (+ Keys.ENTER)

# clicking link & opening pages
link = driver.find_element(By.PARTIAL_LINK_TEXT, "NFL.com | Official Site")
link.click()


time.sleep(7.00)
driver.quit()