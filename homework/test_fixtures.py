"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(params=[(1920, 1080), (1280, 1024), (1650, 1050)], ids=['Full HD', '5:4', '16:10'])
def desktop_running(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser
    browser.quit()


@pytest.fixture(params=[(576, 720), (828, 1792), (750, 1334)], ids=['Generic Phone', 'IPhone11', 'IPhone SE'])
def mobile_running(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser
    browser.quit()


@pytest.mark.usefixtures('desktop_running')
def test_github_desktop():
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


@pytest.mark.usefixtures("mobile_running")
def test_github_mobile():
    browser.open('https://github.com')
    browser.element('[aria-label="Toggle navigation"] .Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
