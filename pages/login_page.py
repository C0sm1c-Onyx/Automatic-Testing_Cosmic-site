from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, *args):
        super().__init__(*args)

    def get_url(self):
        return self.browser.current_url
