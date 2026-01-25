# tests/conftest.py
import pytest
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Создание скриншотов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            # Ищем драйвер в фикстурах теста
            driver = item.funcargs.get('driver')
            if driver:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name=f"screenshot_{rep.nodeid}",
                    attachment_type=allure.attachment_type.PNG
                )
        except:
            pass