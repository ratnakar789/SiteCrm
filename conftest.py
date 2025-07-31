from selenium import webdriver
import pytest
import json

def load_test_data():
    with open("D:\MyProject\DataDrivenTesting\PytestSetup1\SuiteCRM_Project2\tests_data\create_account_data.json",'r') as f:
        data = f.read()
        json_data = json.loads(data)
        return json_data

@pytest.fixture(scope="function")
def init_driver(request):
    driver =webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://demo.suiteondemand.com/index.php?action=Login&module=Users&login_module=Users&login_action=Logout')
    request.cls.driver = driver
    yield
    driver.quit()