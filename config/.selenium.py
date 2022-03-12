import os
import selenium
from selenium import webdriver

driver = webdriver.Chrome("/home/dluman/chromedriver")
driver.maximize_window()

#pages_api = os.getenv("PAGES_URL")
#data = json.loads(pages_api)
#endpoint = data["html_url"]

driver.get("https://allegheny-college-sandbox.github.io/selenuim-testing/" + "hole-1.html")

target = driver.find_element_by_css_selector("#target")
ball = driver.find_element_by_css_selector("#ball")

print(ball.location)
print(target.location)
