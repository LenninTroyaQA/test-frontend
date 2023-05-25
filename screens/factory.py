from driver.driver import Driver
from screens.homepage_screen import HomepageScreen
from screens.base import Base
from screens.test_utils import TestUtils

class Factory:

    test_utils = TestUtils()
    base = Base()
    driver = Driver()
    homepage_screen = HomepageScreen()
