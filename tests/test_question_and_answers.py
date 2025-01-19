import pytest
from pages.HomePage import HomePage
from pages.OrderPage import OrderPage
from data import QuestionAndAnswersData

class TestQuestionAndAnswers:

    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", QuestionAndAnswersData.questions_and_answers)
    def test_questions_and_answers(self, driver, question_locator, answer_locator, expected_answer):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.open_main_page()
        order_page.input_accept_cookie_button()
        home_page.scroll_to_element(question_locator)
        home_page.click_on_question(question_locator)
        actual_answer = home_page.get_answer_text(answer_locator)
        assert actual_answer == expected_answer
