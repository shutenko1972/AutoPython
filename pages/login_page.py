# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы логина"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Открыть страницу логина"""
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def login(self, username, password):
        """Выполнить логин"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return self
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
    
    def get_error_message(self):
        """Получить сообщение об ошибке"""
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        except:
            return None
    
    def is_error_displayed(self):
        """Проверить, есть ли ошибка"""
        return self.get_error_message() is not None