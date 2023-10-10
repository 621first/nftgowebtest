'''
@filename: /test_info
@time: 2023/9/20 13:49
'''

from page_object.main import MainPage


class TestMain():
    def test_login(self,driver):
       main_page = MainPage(driver)
       main_page.login()