from selenium.webdriver.common.by import By

class BasePageLocator:
    LOGO_YANDEX_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    LOGO_SAMOKAT_BUTTON = (By.XPATH, "//*[contains(@class,'Header_LogoScooter__3lsAR')]")
    FIRST_MAKE_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    SECOND_MAKE_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Заказать']")
    INPUT_ACCEPT_COOKIE = (By.CLASS_NAME, "App_CookieButton__3cvqF")

class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    INPUT_SURNAME = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    INPUT_ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    INPUT_METRO = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    @staticmethod
    def metro_button(metro):
        return [By.XPATH, f".//div[text()='{metro}']/parent::button"]
    INPUT_PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон: на него позвонит курьер')]")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    INPUT_DATE = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]")
    INPUT_RENTAL_PERIOD = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    HOW_LONG_INPUT = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    INPUT_COMMENT = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")
    ORDER_NUMBER = (By.XPATH, ".//div[contains(text(),'Номер заказа')]")
    INPUT_COLOR = (By.CLASS_NAME, "Checkbox_Input__14A2w")
    INPUT_YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")

class QuestionAndAnswerPage:
    FIRST_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")
    FIRST_ANSWER = (By.XPATH, "//div[@id='accordion__panel-0']")
    SECOND_QUESTION = (By.XPATH, "//div[@id='accordion__heading-1']")
    SECOND_ANSWER = (By.XPATH, "//div[@id='accordion__panel-1']")
    THIRD_QUESTION = (By.XPATH, "//div[@id='accordion__heading-2']")
    THIRD_ANSWER = (By.XPATH, "//div[@id='accordion__panel-2']")
    FOURTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-3']")
    FOURTH_ANSWER = (By.XPATH, "//div[@id='accordion__panel-3']")
    FIFTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-4']")
    FIFTH_ANSWER = (By.XPATH, "//div[@id='accordion__panel-4']")
    SIXTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-5']")
    SIXTH_ANSWER = (By.XPATH, "//div[@id='accordion__panel-5']")
    SEVENTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-6']")
    SEVENTH_ANSWER = (By.XPATH, "//div[@id='accordion__panel-6']")
    EIGHTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7']")
    EIGHTH_ANSWER = (By.XPATH, "//div[@id='accordion__panel-7']")
