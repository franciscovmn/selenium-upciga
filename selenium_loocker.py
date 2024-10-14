from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys

browser = Chrome()

browser.get("https://lookerstudio.google.com/navigation/reporting?requirelogin=1")

sleep(2)

try:
    manifestacao_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="divServicosMaisAcessados"]/div[4]/a'))
    )
    manifestacao_link.click()
except:
    browser.quit()
    sys.exit() 