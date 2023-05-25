import os
import allure
from driver.driver import Driver


def pytest_runtest_setup(item):
    headless = headless_flag(item)

    driver_params = {"headless": headless}

    Driver.initialize(**driver_params)


def pytest_runtest_teardown(item):
    filename = 'screenshot-%s.png' % item.name
    console_log = Driver.driver.get_log('browser')
    Driver.driver.get_screenshot_as_file(os.path.abspath(
        os.path.join('.', 'screenshots', filename)))

    allure.attach(Driver.driver.get_screenshot_as_png(),
                  name="Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    allure.attach(str(console_log),
                  name="Console Log",
                  attachment_type=allure.attachment_type.TEXT)
    print('Screenshot saved as %s' % filename)

    Driver.quit()


def headless_flag(request):
    return request.config.getoption("-H")


def pytest_addoption(parser):
    parser.addoption("-H", "--headless",
                     dest="headless browser",
                     default="",
                     help="Run headless browser")