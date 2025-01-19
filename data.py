from locators import QuestionAndAnswerPage

class Answers:
    ANSWER1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ANSWER2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ANSWER3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ANSWER4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ANSWER5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ANSWER6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ANSWER7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ANSWER8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class UserData:
    data1 = {
        "name" : "Дмитрий",
        "surname" : "Терехов",
        "address" : "Кантемировская",
        "phone" : "89661479944",
        "date" : "01.02.2025",
        "metro" : "Кантемировская",
        "comment" : "Позвонить за 10 минут"
    }

    data2 = {
        "name" : "Оксана",
        "surname" : "Алексеева",
        "address" : "Максима Горького 46",
        "phone" : "89661339944",
        "date" : "06.02.2025",
        "metro" : "Фили",
        "comment" : "Не стучите в дверь, звоните в звонок"
    }

class QuestionAndAnswersData:
    questions_and_answers = [
        (QuestionAndAnswerPage.FIRST_QUESTION, QuestionAndAnswerPage.FIRST_ANSWER, Answers.ANSWER1),
        (QuestionAndAnswerPage.SECOND_QUESTION, QuestionAndAnswerPage.SECOND_ANSWER, Answers.ANSWER2),
        (QuestionAndAnswerPage.THIRD_QUESTION, QuestionAndAnswerPage.THIRD_ANSWER, Answers.ANSWER3),
        (QuestionAndAnswerPage.FOURTH_QUESTION, QuestionAndAnswerPage.FOURTH_ANSWER, Answers.ANSWER4),
        (QuestionAndAnswerPage.FIFTH_QUESTION, QuestionAndAnswerPage.FIFTH_ANSWER, Answers.ANSWER5),
        (QuestionAndAnswerPage.SIXTH_QUESTION, QuestionAndAnswerPage.SIXTH_ANSWER, Answers.ANSWER6),
        (QuestionAndAnswerPage.SEVENTH_QUESTION, QuestionAndAnswerPage.SEVENTH_ANSWER, Answers.ANSWER7),
        (QuestionAndAnswerPage.EIGHTH_QUESTION, QuestionAndAnswerPage.EIGHTH_ANSWER, Answers.ANSWER8),
    ]