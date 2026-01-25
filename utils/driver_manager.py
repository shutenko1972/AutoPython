import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ПЕРЕКЛЮЧАТЕЛЬ: True = браузер виден, False = скрытый режим
SHOW_BROWSER = True

def get_driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    if os.path.exists('/.dockerenv'):
        # Docker всегда headless
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
    else:
        # Windows: зависит от SHOW_BROWSER
        if SHOW_BROWSER:
            options.add_argument('--start-maximized')
        else:
            options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver