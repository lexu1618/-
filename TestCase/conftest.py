import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import Common_Datas as CD

driver = None
@pytest.fixture(scope="class")
def access_web():
    global driver
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver,lg)
    driver.quit()

@pytest.fixture()
def refresh_page():
    global driver
    yield
    driver.refresh()


# PytestUnknownMarkWarning: Unknown pytest.mark.   避免mark报错
def pytest_configure(config):
    marker_list =["smoke","retest","demo"]
    for markers in marker_list:
        config.addinivalue_line("markers",markers)