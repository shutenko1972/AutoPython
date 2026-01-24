# -*- coding: utf-8 -*-
import pytest
import allure
import traceback
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.driver_manager import get_driver


@allure.feature("Авторизация")
class TestLogin:
    
    def _take_screenshot(self, driver, test_name):
        """Сделать скриншот и прикрепить к Allure"""
        try:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, 
                         name=f"screenshot_{test_name}",
                         attachment_type=allure.attachment_type.PNG)
        except:
            pass
    
    @allure.title("Успешный логин standard_user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        """standard_user / secret_sauce"""
        driver = None
        try:
            driver = get_driver()
            page = LoginPage(driver).open()
            page.login("standard_user", "secret_sauce")
            
            assert "inventory" in page.get_current_url()
            assert not page.is_error_displayed()
            
            self._take_screenshot(driver, "success_login")
            
        except AssertionError as e:
            if driver:
                self._take_screenshot(driver, "success_login_failed")
            raise e
        except Exception as e:
            if driver:
                self._take_screenshot(driver, "success_login_error")
            raise e
        finally:
            if driver:
                driver.quit()
    
    @allure.title("Логин с неверным паролем")
    def test_wrong_password(self):
        """Неверный пароль"""
        driver = None
        try:
            driver = get_driver()
            page = LoginPage(driver).open()
            page.login("standard_user", "wrong_password")
            
            assert page.is_error_displayed()
            error = page.get_error_message()
            assert "do not match" in error
            
            self._take_screenshot(driver, "wrong_password")
            
        except AssertionError as e:
            if driver:
                self._take_screenshot(driver, "wrong_password_failed")
            raise e
        except Exception as e:
            if driver:
                self._take_screenshot(driver, "wrong_password_error")
            raise e
        finally:
            if driver:
                driver.quit()
    
    @allure.title("Логин заблокированного пользователя locked_out_user")
    def test_locked_user(self):
        """locked_out_user / secret_sauce"""
        driver = None
        try:
            driver = get_driver()
            page = LoginPage(driver).open()
            page.login("locked_out_user", "secret_sauce")
            
            assert page.is_error_displayed()
            error = page.get_error_message()
            assert "locked out" in error.lower()
            
            self._take_screenshot(driver, "locked_user")
            
        except AssertionError as e:
            if driver:
                self._take_screenshot(driver, "locked_user_failed")
            raise e
        except Exception as e:
            if driver:
                self._take_screenshot(driver, "locked_user_error")
            raise e
        finally:
            if driver:
                driver.quit()
    
    @allure.title("Логин с пустыми полями")
    def test_empty_fields(self):
        """Пустые поля"""
        driver = None
        try:
            driver = get_driver()
            page = LoginPage(driver).open()
            driver.find_element(By.ID, "login-button").click()
            
            assert page.is_error_displayed()
            error = page.get_error_message()
            assert "required" in error.lower()
            
            self._take_screenshot(driver, "empty_fields")
            
        except AssertionError as e:
            if driver:
                self._take_screenshot(driver, "empty_fields_failed")
            raise e
        except Exception as e:
            if driver:
                self._take_screenshot(driver, "empty_fields_error")
            raise e
        finally:
            if driver:
                driver.quit()
    
    @allure.title("Логин performance_glitch_user")
    def test_performance_user(self):
        """performance_glitch_user / secret_sauce"""
        driver = None
        try:
            driver = get_driver()
            page = LoginPage(driver).open()
            page.login("performance_glitch_user", "secret_sauce")
            
            assert "inventory" in page.get_current_url()
            assert not page.is_error_displayed()
            
            self._take_screenshot(driver, "performance_user")
            
        except AssertionError as e:
            if driver:
                self._take_screenshot(driver, "performance_user_failed")
            raise e
        except Exception as e:
            if driver:
                self._take_screenshot(driver, "performance_user_error")
            raise e
        finally:
            if driver:
                driver.quit()