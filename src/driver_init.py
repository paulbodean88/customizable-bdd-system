from selenium import webdriver


class MyDriver:
    def __init__(self, driver):
        if driver == 'Firefox':
            self._driver = webdriver.Firefox(executable_path="/Users/paulb/GitHub/workshop-eu/public/geckodriver")
        elif self._driver == 'Chrome':
            self._driver = webdriver.Chrome()
        else:
            raise Warning('To be defined')

    def get_driver(self):
        return self._driver
