from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    # Localizadores de elementos
    USER = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    SINGUP_LINK = (By.LINK_TEXT, "Sign up")

    # Constructor de clase página login
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    # Acciones de página login

    # Usado para obtener el título de la página
    def get_login_page_title(self, title):
        return self.get_title(title)

    # Usado para chequear el link de ingreso
    def is_signup_link_exist(self):
        return self.is_visible(self.SINGUP_LINK)

    # Usado para hacer login a la aplicación
    def do_login(self, username, password):
        self.do_send_keys(self.USER, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
