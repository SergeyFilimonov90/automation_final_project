import time
import datetime
import allure
from datetime import date
import calendar
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import Home_page
from pages.smartphones_page import SmartphonesPage
from pages.cart_step_one import CartStepOne
from pages.cart_final_page import FinalCheckoutTest


@allure.description('Smoke test citilink')
def test_city_select(set_up): #set_up
     options = Options()
     options.add_experimental_option('excludeSwitches',['enable-logging'])
     driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)
     city = Home_page(driver)

     smartphone = SmartphonesPage(driver)
     cart_stage_one = CartStepOne(driver)
     final_checkout = FinalCheckoutTest(driver)

     city.city_select()
     smartphone.smartphone_select()
     cart_stage_one.chechout_first_stage()
     final_checkout.final_checkout_test()


     time.sleep(10)

     driver.quit()

