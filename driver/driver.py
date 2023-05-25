from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver(object):
    driver = None
    wait_timeout = 30
    base_url = ''
    options = Options()

    @classmethod
    def initialize(cls, **driver_params):
        cls.headless = driver_params['headless']

        cls.options.add_argument('--user-agent="Mozilla/5.0 ' +
                                 '(Macintosh; Intel Mac OS X 10_14_5)' +
                                 ' AppleWebKit/537.36 (KHTML, like Gecko)' +
                                 ' Chrome/77.0.3865.90 Safari/537.36 ViceQA/1.0"')

        if cls.headless == "true":
            cls.options.add_argument("--headless")
            cls.options.add_argument("--window-size=1920,1080")
            cls.options.add_argument("--no-sandbox")
            cls.options.add_argument("--disable-dev-shm-usage")
            cls.options.add_argument("--disable-gpu")
            cls.driver = webdriver.Chrome(options=cls.options)
        else:
            cls.options.add_argument("--no-sandbox")
            cls.options.add_argument("--disable-dev-shm-usage")
            cls.options.add_argument("--disable-gpu")
            cls.options.add_argument("--start-maximized")
            cls.driver = webdriver.Chrome(options=cls.options)

    @classmethod
    def quit(cls):
        if cls.driver:
            cls.driver.quit()
