from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div#content_inner div.basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner > p")
