from pages.main_page import MainPage
from pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', [f'{LINK}?promo=offer{n}' if n != 7 else pytest.param(
        f'{LINK}?promo=offer7', marks=pytest.mark.xfail
    ) for n in range(10)]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()


def test_guest_can_add_product_to_basket_with_promo_newyear(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_to_basket()


@pytest.mark.login_page
def test_guest_should_see_login_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.go_to_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_basket_is_empty()


@pytest.mark.xfail(reason="Сообщение об успехе должно быть всегда!")
def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Сообщение об успехе должно быть всегда!")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappear_success_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        email = fake.email()
        password = fake.password()
        test_guest_can_go_to_login_page_from_product_page(browser)
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_be_add_product_to_basket()
