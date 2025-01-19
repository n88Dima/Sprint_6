import allure
import pytest


from conftest import driver
from data import UserData
from pages.OrderPage import OrderPage



class TestOrderPage:


    @allure.title("Создание заказа через верхнюю кнопку 'Заказать'")
    @allure.description("Проверка, через верхнюю кнопку 'Заказать', что при корректном заполнении всех полей для заказа он успешно создаться и ему присвоится номер заказа")
    @pytest.mark.parametrize('data1', [UserData.data1])    
    def test_upper_order_button_order_created_successful(self, driver, data1):
        order_page = OrderPage(driver)
        order_page.open_main_page()
        order_page.input_accept_cookie_button()
        order_page.input_first_make_order_button()
        order_page.fill_user_data(data1)
        order_page.input_next_button()
        order_page.fill_order_data(data1)
        order_page.input_order_button_in_order_form()
        order_page.input_yes_button()
        result = "Номер заказа"
        assert result in order_page.get_the_order_number()

    @allure.title("Создание заказа через среднюю кнопку 'Заказать'")
    @allure.description("Проверка, через среднюю кнопку 'Заказать', что при корректном заполнении всех полей для заказа он успешно создаться и ему присвоится номер заказа")
    @pytest.mark.parametrize('data2', [UserData.data2]) 
    def test_middle_order_button_order_created_successful(self, driver, data2):
        order_page = OrderPage(driver)
        order_page.open_main_page()
        order_page.input_accept_cookie_button()
        order_page.input_second_make_order_button()
        order_page.fill_user_data(data2)
        order_page.input_next_button()
        order_page.fill_order_data(data2)
        order_page.input_order_button_in_order_form()
        order_page.input_yes_button()
        result = "Номер заказа"
        assert result in order_page.get_the_order_number()

