import allure
from locators import QuestionAndAnswerPage, BasePageLocator
from pages.BasePage import BasePage


class HomePage(BasePage):
    @allure.step("Нажать на кнопку Яндекс")
    def input_yandex_button(self):
        return self.driver.find_element(*BasePageLocator.LOGO_YANDEX_BUTTON).click()
    
    @allure.step("Нажать на кнопку Самокат")
    def input_samokat_button(self):
        return self.driver.find_element(*BasePageLocator.LOGO_SAMOKAT_BUTTON).click()
    
    @allure.step("Получить текст вопроса")
    def get_question_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Получить текст ответа")
    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text