import time
import datetime
from datetime import date
import calendar
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import SmartphonesPageLocators
from pages.locators import CartLocators
from pages.smartphones_page import SmartphonesPage
from utilities.logger import Logger


class CartStepOne(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    item_name_value = ''
    item_price_value_1 = ''
    item_price_value_2 = ''


    #Getters

    def get_cart_paragraph(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartLocators.CART_PARAGRAPH)))





    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartLocators.CHECKOUT_BUTTON)))

    def get_item_name(self):
        global item_name_value
        item_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartLocators.ITEM_NAME)))
        item_name_value = item_name.text
        print(item_name_value)
        return item_name_value


    def get_item_price(self):
        global item_price_value_1
        item_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartLocators.ITEM_PRICE_TAG_1)))
        item_price_value_1 = item_price.text
        print(item_price_value_1)
        return item_price_value_1

    def get_item_price_2(self):
        global item_price_value_2
        item_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartLocators.ITEM_PRICE_TAG_2)))
        item_price_value_2 = item_price.text
        print(item_price_value_2)
        return item_price_value_2




    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Cliking checkout button')




    #Methods

    def chechout_first_stage(self):
        with allure.step('Checkout first stage'):
            Logger.add_start_step(method='chechout_first_stage')
            self.assert_url('https://www.citilink.ru/order/')
            self.check_value(SmartphonesPage.item_name_value,self.item_name_value)
            self.check_value(SmartphonesPage.item_price_value, self.item_price_value_1)
            self.check_value(SmartphonesPage.item_price_value, self.item_price_value_2)
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='chechout_first_stage')








