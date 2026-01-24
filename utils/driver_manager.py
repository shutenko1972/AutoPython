import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Проверяем, запущены ли в Docker
    if os.path.exists('/.dockerenv') or os.environ.get('RUNNING_IN_DOCKER'):
        # Docker режим
        options.add_argument('--headless')
        options.binary_location = '/usr/bin/chromium'
        service = Service(executable_path='/usr/bin/chromedriver')
    else:
        # Локальный режим (Windows)
        service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver