from lib2to3.pgen2 import driver
from telnetlib import EC
import datetime
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self,driver):

        self.driver = driver
        self.action = ActionChains(driver)

    '''Move to element'''

    def move_to(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    '''Method check paragraph text'''

    def check_text(self, word, value):
        value_word = word.text
        try:
            assert value_word == value,'Wrong value!'
        except AssertionError:
            print(f'Test failed value_word: {value_word} != value: {value}')

        print(f'Test passed word {value_word}={value}')

    def check_value(self, word, value):
        value_word = word
        assert value_word == value,'Wrong value!'
        print('Word value test passed')

    '''Method make screenshot'''

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m..%d.%H.%M.%S')
        name_screenshot = 'screenshot' + str(now_date) + '.png'  # setting the proper file name and format
        self.driver.save_screenshot('C:\\Users\\Elgyn\\PycharmProjects\\main_project\\screen\\' + name_screenshot)

    def assert_url(self,result):
        current_url =  self.driver.current_url
        assert current_url == result, 'Wrong url!'
        print('Url test passed')

    def assert_final_cart_price(self,price):
        price = price.text[1:]  # using slice to get rid of $ simbol
        print('$ sliced off',price)

        price_total = self.driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[2]/div[6]")
        test_price_total = price_total.text
        print('Checking out total price')
        print(price_total.text)
        assert price_total.text == 'Item total: ' + '$' + str(price), 'Wrong total price'


