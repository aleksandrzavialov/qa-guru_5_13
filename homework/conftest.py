import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def browser_configuration():

    yield browser
    browser.quit()

