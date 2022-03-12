import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

pages_api = os.getenv("PAGES_URL")
data = json.loads(pages_api)
endpoint = data["html_url"]

driver.get(endpoint + "hole-1.html")

ball = driver.find_element_by_css_selector("#ball")

print(ball)
