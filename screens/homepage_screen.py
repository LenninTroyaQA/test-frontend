from driver.driver import Driver
from selenium.webdriver.common.by import By


class HomepageScreen:

    def headline_text(self):
        return Driver.driver.find_element(By.XPATH, '//h1[@class="alignwide wp-block-heading"]')

    def sample_page_header_menu_link(self):
        return Driver.driver.find_element(By.XPATH, '//a[text()="Sample Page"]')

