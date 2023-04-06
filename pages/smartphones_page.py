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
from utilities.logger import Logger


class SmartphonesPage(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    item_name_value = ''
    item_price_value = ''
    pop_up_item_name = ''
    pop_up_item_price = ''

    #Getters

    def get_smartphones_paragraph(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.SMARTPHONES_PARAGRAPH)))

    def get_show_all_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.SHOW_ALL_BUTTON)))

    def get_series_span(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.SERIES_SPAN)))

    def get_series_huawei(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.HUAWEI)))

    def get_show_all_series(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.SHOW_ALL_SERIES)))

    def get_smartphones_sub_menu_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.HUAWEI_CHECKBOX)))

    def get_huawei_checkbox(self):
        time.sleep(1)
        driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe')
        return driver.find_element(by=By.XPATH, value="//*[@id='huawei']")

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.ADD_TO_CART_BUTTON)))

    def get_item_name(self):
        global item_name_value
        item_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.ITEM_NAME)))
        item_name_value = item_name.text
        print(item_name_value)
        return item_name_value


    def get_item_price(self):
        global item_price_value
        item_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.ITEM_PRICE)))
        item_price_value = item_price.text
        print(item_price_value)
        return item_price_value


    def get_pop_up_item_name(self):
        global pop_up_item_name
        pop_up_item = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.POP_UP_ITEM_NAME)))
        pop_up_item_name = pop_up_item.text
        print(pop_up_item_name)
        return pop_up_item_name


    def get_pop_up_item_price(self):
        global pop_up_item_price
        pop_up_price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.POP_UP_ITEM_PRICE_CCS )))
        pop_up_item_price = pop_up_price.text
        print(pop_up_item_price)
        return pop_up_item_price

    def get_pop_up_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((SmartphonesPageLocators.POP_UP_ADD_TO_CART )))




    # def get_selected_city(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(()))
    #
    # def get_h3_word_text(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(())
    #
    # def get_smartphones(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(()))


    #Actions

    def click_huawei_checkbox(self):
        self.get_huawei_checkbox().click()
        print('Cliking show all button')

    def click_sub_menu(self):
        self.get_show_all_button().click()
        print('Clicking smarthphones  sub menuserach field')

    def sub_menu_sent_keys(self,keys):
        self.get_smartphones_sub_menu_field().send_keys(keys)

    def add_to_cart(self):
        self.get_add_to_cart_button().click()

    def pop_up_add_to_cart(self):
        self.get_pop_up_add_to_cart().click()



    #def input_city(self, city):
        #self.get_city_search().send_keys(city)
        #print('Input password')

    #def click_selected_city(self):
        #self.get_selected_city().click()
        #print('clicking selected city')

    #def click_smartphones(self):
        #self.get_smartphones().click()

    #Methods

    def smartphone_select(self):
        with allure.step('Smartphone select'):
            Logger.add_start_step(method='smartphone_select')
            self.assert_url('https://www.citilink.ru/catalog/smartfony/')
            self.get_item_name()
            self.get_item_price()
            self.add_to_cart()
            self.get_pop_up_item_name()
            self.get_pop_up_item_price()
            self.check_value(self.item_name_value,self.pop_up_item_name)
            self.check_value(self.item_price_value,self.pop_up_item_price)
            self.pop_up_add_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method='smartphone_select')

        #self.check_text(self.get_smartphones_paragraph(),'Смартфоны')
        #self.move_to(self.get_show_all_series())
        #self.click_sub_menu()
        #self.sub_menu_sent_keys('Huawei')
        #self.click_huawei_checkbox()
        #time.sleep(5)
        #self.move_to(self.get_smartphones_paragraph())


        #self.driver.execute_script('window.scrollTo(0, 1000)')








