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
from pages.locators import FinalCheckout
from pages.smartphones_page import SmartphonesPage
from utilities.logger import Logger


class FinalCheckoutTest(SmartphonesPage,Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    item_name = ''
    item_price = ''
    item_price_mini = ''
    item_price_total = ''

    price_mini_text = '₽ - 1 шт.'


    #Getters

    def get_final_cart_paragraph(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.FINAL_CHECKOUT_TEXT)))

    def get_item_text_final(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_TEXT)))

    def get_item_price_tag_mini(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_PRICE_MINI)))

    def get_item_price_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_PRICE)))

    def get_item_price_tag_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_PRICE_TOTAL)))


    def get_item_name(self):
        global item_name
        item_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_TEXT)))
        item_name = item_name.text
        print(item_name)
        return item_name


    def get_item_price(self):
        global item_price
        item_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_PRICE)))
        item_price = item_price.text
        print(item_price)
        return item_price

    def get_item_price_mini(self):
        global item_price_mini
        item_price_mini = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_PRICE_MINI)))
        item_price_mini = item_price_mini.text[:-10]
        print(item_price_mini)
        return item_price_mini

    def get_item_price_total(self):
        global item_price_total
        item_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinalCheckout.ITEM_PRICE_TOTAL)))
        item_price_total = item_price.text
        print(item_price_total)
        return item_price_total



    #Actions



    #Methods

    def final_checkout_test(self):
        with allure.step('Checkout final stage'):
            Logger.add_start_step(method='final_checkout_test')
            self.assert_url('https://www.citilink.ru/order/checkout/')
            self.get_item_name()
            self.get_item_price()
            self.get_item_price_mini()
            self.check_value(SmartphonesPage.item_name_value,self.item_name)
            self.check_value(SmartphonesPage.item_price_value,self.item_price)
            self.check_value(SmartphonesPage.item_price_value,self.item_price_mini)
            self.check_value(SmartphonesPage.item_price_value,self.item_price_total)
            Logger.add_end_step(url=self.driver.current_url, method='final_checkout_test')









