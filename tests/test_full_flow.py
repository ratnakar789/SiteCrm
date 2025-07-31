import pytest
import json
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','pages')))
from login_page import LoginPage




with open("D:\MyProject\DataDrivenTesting\PytestSetup1\SuiteCRM_Project2\tests_data\create_account_data.json", 'r') as f:
        data = f.read()
     json_data = json.loads(data)

@pytest.mark.usefixtures('init_driver')
class TestSuiteCRMLogin:
    @pytest.mark.parametrize('credential',json_data["valid_credential"])
    def test_valid_login(self,credential):
        page = LoginPage(self.driver)
        page.login(credential["username"],credential["password"])
        assert "/dashboard" in self.driver.current_url.lower()










