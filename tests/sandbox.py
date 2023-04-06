import time
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)

url = 'https://www.citilink.ru/catalog/smartfony/'
driver.get(url)
driver.maximize_window()
time.sleep(3)

paragraph = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//h1[@class='e1e4gwta0 eml1k9j0 app-catalog-yhwyfr e1gjr6xo0']")))

button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[7]/div[2]/div/div[2]/button")))

button2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[7]/div[2]/div/div[2]/button")))

action = ActionChains(driver)
action.move_to_element(button).perform()
show_all = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[6]/div[2]/div/div[2]/button")))
show_all.click()
field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[6]/div[2]/div/div[1]/div/input")))
field.send_keys('Huawei')

huawei_button = driver.find_element(by=By.XPATH, value="//*[@id='huawei']").click()

time.sleep(20)

action.move_to_element(paragraph).perform()

button_2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[2]/button/span/span/span[2]")))
button_2.click()
time.sleep(10)
price = driver.find_element(by=By.CSS_SELECTOR, value="body > div.PopupScrollContainer > div > div > div > div > div.css-10n8sd6.e73syig0 > div > div > div > div.css-10hz06r.e1r8mzjd0 > div > div.css-19i70pr.e1e9kkl20 > div.css-qfdd9t.ezset5n0 > span > span > span > span.e1j9birj0.e106ikdt0.css-175fskm.e1gjr6xo0")

price_text= price.text

print(price_text)

time.sleep(20)




#actions = ActionChains(driver)
#a.move_to_element(huawei_button).click().perform()
#actions.click().perform()



time.sleep(30)



