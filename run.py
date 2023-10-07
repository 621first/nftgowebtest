import os
import time
import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir=./report/result', '--clean-alluredir'])
    time.sleep(3)
    os.system("allure generate ./report/result -o report/html --clean")