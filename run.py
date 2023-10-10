import os
import time
import pytest
from commons.utils.emailUtil.sendemail import Email

if __name__ == '__main__':
    pytest.main(['--alluredir=./report/result', '--clean-alluredir'])
    # time.sleep(3)
    os.system("allure generate ./report/result -o report/html --clean")

    # 发送邮件
    time.sleep(1)
    name = r'D:\workspace\study\nftgowebtest\report\html\index.html'
    Email().send_email(name)

    os.system('allure serve ./report/result -o report/html')

