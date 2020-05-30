from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    '''
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_REPLY_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")

    SIGN_IN_EMAIL_FORM = (By.CSS_SELECTOR, "#id_login-username")
    SIGN_IN_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_login-password")
    '''
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():

    ADD_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
