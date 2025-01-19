import allure


from conftest import driver
from pages.OrderPage import OrderPage
from pages.HomePage import HomePage

from URLS import Urls

class TestHomePage:

    @allure.title("Проверка кнопки 'Самокат' для перехода на главную страницу")
    @allure.description("Проверка кнопки 'Самокат' для перехода на главную страницу, перед этим зашли в форму оформления заказа")
    def test_samokat_logo_go_to_home_page(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        order_page.open_main_page()
        order_page.input_accept_cookie_button()
        order_page.input_first_make_order_button()
        home_page.input_samokat_button()
        current_url = home_page.current_url()
        assert Urls.MAIN_PAGE == current_url
    
    @allure.title("Проверка кнопки Дзен для перехода на страницу дзена")
    @allure.description("Проверка кнопки Дзен для перехода на страницу дзена, перед этим вошли в форму оформления заказа")
    def test_dzen_logo_go_to_home_page(self, driver):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        order_page.open_main_page()
        order_page.input_accept_cookie_button()
        order_page.input_first_make_order_button()
        home_page.input_yandex_button()
        home_page.switch_window()
        home_page.wait_for_urls()
        current_url = home_page.current_url()
        assert Urls.DZEN_PAGE == current_url
    
        