import time
import datetime
import allure
from datetime import date
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import HomePageLocators
from utilities.logger import Logger


class Home_page(Base):

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Getters

    def get_select_city_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((HomePageLocators.CITY_SELECT_BUTTON)))

    def get_city_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((HomePageLocators.CITY_SEARCH_FIELD)))

    def get_selected_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((HomePageLocators.SELECTED_CITY)))

    def get_h3_word_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((HomePageLocators.HOME_PAGE_CHECK_TEXT)))

    def get_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((HomePageLocators.SMARTPHONES)))


    #Actions

    def click_city_select(self):
        self.get_select_city_button().click()
        print('cliking city select button')

    def input_city(self, city):
        self.get_city_search().send_keys(city)
        print('Input password')

    def click_selected_city(self):
        self.get_selected_city().click()
        print('clicking selected city')

    def click_smartphones(self):
        self.get_smartphones().click()

    #Methods

    def city_select(self):
        with allure.step('City select'):
            Logger.add_start_step(method='city_select')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_city_select()
            self.input_city('Москва')
            self.check_text(self.get_selected_city(),'Москва')
            self.click_selected_city()
            self.check_text(self.get_select_city_button(), 'Москва')
            self.click_smartphones()
            Logger.add_end_step(url=self.driver.current_url,method='city_select')






