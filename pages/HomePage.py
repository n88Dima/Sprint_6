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
    
    @allure.step("Нажать на вопрос")
    def click_on_question(self, question_locator):
        return self.driver.find_element(*question_locator).click()
    
    @allure.step("Нажать на первый вопрос")
    def click_on_first_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.FIRST_QUESTION).click()
    
    @allure.step("Нажать на второй вопрос")
    def click_on_second_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.SECOND_QUESTION).click()
    
    @allure.step("Нажать на третий вопрос")
    def click_on_third_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.THIRD_QUESTION).click()
    
    @allure.step("Нажать на четвертый вопрос")
    def click_on_fourth_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.FOURTH_QUESTION).click()
    
    @allure.step("Нажать на пятый вопрос")
    def click_on_fifth_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.FIFTH_QUESTION).click()
    
    @allure.step("Нажать на шестой вопрос")
    def click_on_sixth_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.SIXTH_QUESTION).click()
    
    @allure.step("Нажать на седьмой вопрос")
    def click_on_seventh_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.SEVENTH_QUESTION).click()

    @allure.step("Нажать на восьмой вопрос")
    def click_on_eighth_question(self):
        return self.driver.find_element(*QuestionAndAnswerPage.EIGHTH_QUESTION).click()

    @allure.step("Получить первый ответ")
    def get_first_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.FIRST_ANSWER)
    
    @allure.step("Получить второй ответ")
    def get_second_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.SECOND_ANSWER)
    
    @allure.step("Получить третий ответ")
    def get_third_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.THIRD_ANSWER)
    
    @allure.step("Получить четвертый ответ")
    def get_fourth_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.FOURTH_ANSWER)
    
    @allure.step("Получить пятый ответ")
    def get_fifth_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.FIFTH_ANSWER)
    
    @allure.step("Получить шестой ответ")
    def get_sixth_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.SIXTH_ANSWER)
    
    @allure.step("Получить седьмой ответ")
    def get_seventh_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.SEVENTH_ANSWER)

    @allure.step("Получить восьмой ответ")
    def get_eighth_answer(self):
        return self.driver.find_element(*QuestionAndAnswerPage.EIGHTH_ANSWER)

    
    