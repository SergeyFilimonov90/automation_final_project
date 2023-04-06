from selenium.webdriver.common.by import By

class HomePageLocators:
    CITY_SELECT_BUTTON = (By.XPATH, "//button[@class='e1x3msk40 css-wsr9k9 etyxved0']")
    CITY_SEARCH_FIELD = (By.XPATH, "//input[@name='search-city']")
    SELECTED_CITY = (By.XPATH, "//span[@class='css-sl5paq ek3bndn0']")
    HOME_PAGE_CHECK_TEXT = (By.XPATH, "//h3[text()='Популярные категории']")
    SMARTPHONES = (By.XPATH, "//span[text()='Смартфоны']")

class SmartphonesPageLocators:
    SMARTPHONES_PARAGRAPH = (By.XPATH, "//h1[@class='e1e4gwta0 eml1k9j0 app-catalog-yhwyfr e1gjr6xo0']")
    SHOW_ALL_BUTTON = (By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[6]/div[2]/div/div[2]/button")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[2]/button/span/span/span[2]")
    SERIES_SPAN = (By.XPATH, "//span[text()='Серия']")
    HUAWEI = (By.XPATH, "//input[@id='huawei']")
    SHOW_ALL_SERIES = (By.XPATH,"//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[7]/div[2]/div/div[2]/button")
    SMARTPHONES_SUB_MENU_SEARCH_FIELD = (By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[1]/div/div/div[2]/div[3]/div/div[3]/div[3]/div[6]/div[2]/div/div[1]/div/input")
    HUAWEI_CHECKBOX = (By.XPATH, "//*[@id='huawei']")
    ITEM_NAME = (By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/a")
    ITEM_PRICE = (By.XPATH, "//*[@id='__next']/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[7]/div[1]/div[2]/span/span/span[1]")
    POP_UP_ITEM_NAME = (By.XPATH, "//div[@class='css-hdphih e1xk8xnt0']")
    POP_UP_ITEM_PRICE = (By.XPATH, "/html/body/div[11]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[4]/div[2]/span/span/span/span[1]")
    POP_UP_ITEM_PRICE_CCS = (By.CSS_SELECTOR, "body > div.PopupScrollContainer > div > div > div > div > div.css-10n8sd6.e73syig0 > div > div > div > div.css-10hz06r.e1r8mzjd0 > div > div.css-19i70pr.e1e9kkl20 > div.css-qfdd9t.ezset5n0 > span > span > span > span.e1j9birj0.e106ikdt0.css-175fskm.e1gjr6xo0")
    POP_UP_ADD_TO_CART = (By.XPATH, "//span[text()='Перейти в корзину']")

class CartLocators:

   CART_PARAGRAPH = (By.XPATH, "//span[@class='e1ys5m360 e106ikdt0 css-1f8xctp e1gjr6xo0']")

   ITEM_NAME = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[2]/div/a/span/span")
   ITEM_PRICE_TAG_1 = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/section/div[1]/div/div/div/div[4]/div/div[2]/span/span/span[1]")
   ITEM_PRICE_TAG_2 = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[1]/div[1]/div[4]/div/span/span/span[1]")
   CHECKOUT_BUTTON = (By.XPATH, "//*[@id='__next']/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[1]/div[1]/div[5]/button/span")


class FinalCheckout:
    FINAL_CHECKOUT_TEXT = (By.XPATH, "//span[@class='e1ys5m360 e106ikdt0 css-j8h82j e1gjr6xo0']")
    ITEM_TEXT = (By.XPATH, "//*[@id='__next']/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/span[1]")
    ITEM_PRICE_MINI = (By.XPATH, "//*[@id='__next']/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/span[2]")
    ITEM_PRICE = (By.XPATH, "//*[@id='__next']/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/span/span/span[1]")
    ITEM_PRICE_TOTAL = (By.XPATH, "//*[@id='__next']/div/div[2]/div/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[3]/div/div[1]/div/div/span[2]/span/span[1]")












