from screens.factory import Factory
from delayed_assert import delayed_assert
import allure


class TestHomepage:

    @allure.title("Verify that the expected headline text is found")
    def test_homepage_001_verify_headline_text(self):
        Factory.driver.driver.get(Factory.base.production_url)
        Factory.test_utils.verify_expected_text(Factory.homepage_screen.headline_text().text,
                                                "Mindblown: a blog about philosophy.")

        delayed_assert.assert_expectations()

    @allure.title("Verify that user landed on expected URL")
    def test_homepage_002_verify_current_url(self):
        Factory.driver.driver.get(Factory.base.production_url)
        Factory.homepage_screen.sample_page_header_menu_link().click()
        Factory.test_utils.verify_current_url(Factory.driver.driver.current_url,
                                                f"{Factory.base.production_url}sample-page/")

        delayed_assert.assert_expectations()
