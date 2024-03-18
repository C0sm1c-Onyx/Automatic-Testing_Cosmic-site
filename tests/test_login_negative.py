from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import pytest


@pytest.mark.xfail
def test_login(browser):
    lp = LoginPage(browser, 'http://127.0.0.1:8000/admin/login/?next=/admin/')
    lp.open()
    lp.find((By.ID, 'id_username')).send_keys('Onyx111')
    lp.find((By.ID, 'id_password')).send_keys('root111')
    lp.find((By.CSS_SELECTOR, "input[type='submit']")).click()
    assert lp.get_url() != 'http://127.0.0.1:8000/admin/login/?next=/admin/'
