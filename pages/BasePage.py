from URLS import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def open_main_page(self):
        self.driver.get(Urls.MAIN_PAGE)

    def current_url(self):
        return self.driver.current_url
    
    def switch_window(self, window_number = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])
    
    def wait_for_urls(self, time = 10, url = Urls.DZEN_PAGE):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))
    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)