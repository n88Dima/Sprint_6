import allure
from pages.BasePage import BasePage
from locators import OrderPageLocators, BasePageLocator


class OrderPage(BasePage):
    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def input_first_make_order_button(self):
        return self.driver.find_element(*BasePageLocator.FIRST_MAKE_ORDER_BUTTON).click()
    
    @allure.step("Нажать на нижнюю кнопку 'Заказать'")
    def input_second_make_order_button(self):
        return self.driver.find_element(*BasePageLocator.SECOND_MAKE_ORDER_BUTTON).click()
    
    @allure.step("Ввод в поле 'Имя'")
    def input_name_field(self, name):
        return self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)
    
    @allure.step("Ввод в поле 'Фамилия'")
    def input_surname_field(self,surname):
        return self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)
    
    @allure.step("Ввод в поле 'Адрес'")
    def input_address_field(self,address):
        return self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)
    
    @allure.step('Выбор метро')
    def choice_metro(self, metro):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO).click()
        return self.driver.find_element(*OrderPageLocators.metro_button(metro)).click()

    @allure.step("Ввод номера телефона'Телефон'")
    def input_phone_field(self,phone):
        return self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)
    
    @allure.step("Нажать на кнопку 'Далее")
    def input_next_button(self):
        return self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
    
    @allure.step("Ввод даты")
    def input_date_field(self,date):
        return self.driver.find_element(*OrderPageLocators.INPUT_DATE).send_keys(date)
    
    @allure.step("Выбор срока аренды")
    def input_rental_period(self):
        self.driver.find_element(*OrderPageLocators.INPUT_RENTAL_PERIOD).click()
        return self.driver.find_element(*OrderPageLocators.HOW_LONG_INPUT).click()
    
    @allure.step("Выбор цвета")
    def input_color(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_COLOR).click()

    @allure.step("Ввод комментария")
    def input_comment(self, comment):
        return self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)
    
    @allure.step("Получение информации о заказе")
    def get_the_order_number(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_NUMBER).text
    
    @allure.step("Нажать на кнопку 'Заказать' под формой заполнения информации о заказе")
    def input_order_button_in_order_form(self):
        return self.driver.find_element(*BasePageLocator.SECOND_MAKE_ORDER_BUTTON).click()
    
    @allure.step("Нажать на кнопку 'да все привыкли' для принятия кук")
    def input_accept_cookie_button(self):
        return self.driver.find_element(*BasePageLocator.INPUT_ACCEPT_COOKIE).click()

    @allure.step("Заполнить данные пользователя для заказа")
    def fill_user_data(self, data):
        self.input_name_field(data["name"])
        self.input_surname_field(data["surname"])
        self.input_address_field(data["address"])
        self.choice_metro(data["metro"])
        self.input_phone_field(data["phone"])

    @allure.step("Заполнить данные заказа") 
    def fill_order_data(self, data):
        self.input_date_field(data["date"])
        self.input_rental_period()
        self.input_color()
        self.input_comment(data["comment"])

    @allure.step("Нажать на кнопку 'Да' после заказа")
    def input_yes_button(self):
        return self.driver.find_element(*OrderPageLocators.INPUT_YES_BUTTON).click()

