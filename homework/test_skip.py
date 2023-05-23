"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(params=[(1920, 1080), (1280, 1024), (1650, 1050), (576, 720), (828, 1792), (750, 1334)])
def calculate_resolution(request):
    width = request.param[0]
    height = request.param[1]
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_width = width
    browser.config.window_height = height
    platform = 'desktop' if width / height > 1 else 'mobile'

    yield browser, platform
    browser.quit()


def test_github_desktop(calculate_resolution):
    platform = calculate_resolution[1]

    if platform != 'desktop':
        pytest.skip('Not for mobile')

    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()


def test_github_mobile(calculate_resolution):
    platform = calculate_resolution[1]

    if platform != 'mobile':
        pytest.skip('Not for desktop')

    browser.open('https://github.com')
    browser.element('[aria-label="Toggle navigation"] .Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[type="submit"]').click()
