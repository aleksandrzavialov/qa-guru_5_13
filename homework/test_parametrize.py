"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selenium import webdriver
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1280, 1024), (1650, 1050)])
def browser_resolution(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser
    browser.quit()


@pytest.fixture(params=[(576, 720), (828, 1792), (750, 1334)])
def mobile_resolution(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield browser
    browser.quit()


full_hd_only = pytest.mark.parametrize("browser_resolution", [(1920, 1080)], indirect=True)
iphone11_only = pytest.mark.parametrize("mobile_resolution", [(828, 1792)], indirect=True)


@full_hd_only
def test_github_desktop(browser_resolution):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


@iphone11_only
def test_github_mobile(mobile_resolution):
    browser.open('https://github.com')
    browser.element('[aria-label="Toggle navigation"] .Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
