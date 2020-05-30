from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_basket(self):
        self.add_product_in_basket()
        self.go_to_basket_page()

    def add_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Product didn't in basket"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket_link.click()
