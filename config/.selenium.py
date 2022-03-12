import os
import math
import sys
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

class Circle:

  def __init__(self, size: dict, loc:dict):
    self.w = size["width"]
    self.h = size["height"]

    self.radius = self.w // 2

    self.x = loc["x"] + self.radius
    self.y = loc["y"] + self.radius

def evaluate(
    target:WebElement,
    ball:WebElement
  ) -> bool:

  t_circ = Circle(target.size, target.location)
  b_circ = Circle(ball.size, ball.location)

  distance = math.sqrt(
    (t_circ.x - b_circ.x) ** 2 +
    (t_circ.y - b_circ.y) ** 2
  )

  if distance + b_circ.radius <= t_circ.radius:
    return True
  return False

def main():

  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)
  driver.maximize_window()

  pages_api = os.getenv("PAGES_URL")
  data = json.loads(pages_api)
  endpoint = data["html_url"]

  page = sys.argv[1]

  # Local Testing
  #driver.get(f"https://allegheny-college-sandbox.github.io/selenuim-testing/{page}")
  driver.get(f"{endpoint}{page}")

  target = driver.find_element(by=By.CSS_SELECTOR, value="#target")
  ball = driver.find_element(by=By.CSS_SELECTOR, value="#ball")

  try:
    trap = driver.find_element(by=By.CSS_SELECTOR, value="#traps")
    if not evaluate(trap, ball): sys.exit(1)
  except:
    pass

  try:
    water = driver.find_element(by=By.CSS_SELECTOR, value="#water")
    if not evaluate(water, ball): sys.exit(1)
  except:
    pass

  if not evaluate(target, ball):
    sys.exit(1)
  print("IN!")

if __name__=="__main__":
  main()
