from selenium.webdriver.common.by import By
from pages.home_page import HomePage


def test_link_asteroid(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img1')).click()


def test_link_planet(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img2')).click()


def test_link_star(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img3')).click()


def test_link_nebula(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img4')).click()


def test_link_galaxy(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img5')).click()


def test_link_blackhole(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img6')).click()


def test_link_spacetime(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img7')).click()


def test_link_darkenergy(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img8')).click()


def test_link_universe(browser):
    hp = HomePage(browser, 'http://127.0.0.1:8000')
    hp.open()
    hp.find((By.ID, 'img9')).click()

