import allure
from delayed_assert import expect


class TestUtils:

    @allure.step("Verify expected text")
    def verify_expected_text(self, returned_text, expected_text):
        if returned_text == expected_text:
            expect(True)
        else:
            expect(False)
            print(f"The returned text: '{returned_text}' does not match the expected text: '{expected_text}'\n")

    @allure.step("Verify expected current URL")
    def verify_current_url(self, current_url, expected_current_url):
        if current_url == expected_current_url:
            expect(True)
        else:
            expect(False)
            print(f"The current url '{current_url}' does not match the expected current url: '{expected_current_url}'\n")