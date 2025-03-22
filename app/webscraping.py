import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def web_scraping():
  options = webdriver.ChromeOptions()
  options.add_argument("--start-maximized")
  options.add_experimental_option("detach", True)
  
  driver = webdriver.Chrome(options=options)

  driver.get("https://www.livelo.com.br/")
  
  close_modal_home_cadastro = driver.find_element(By.CLASS_NAME, "close_modal_home_cadastro")
  time.sleep(2)
  close_modal_home_cadastro.click()


if __name__ == "__main__":
  web_scraping()