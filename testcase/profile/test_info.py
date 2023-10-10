'''
@filename: /test_info
@time: 2023/9/20 13:49
'''

from page_object.homePage import ProfilePage


class TestProfile():
    def test_profile(self,driver):
        profile_page = ProfilePage(driver)
        profile_page.info()

    def test_open_offer(self,driver):
        profile_page = ProfilePage(driver)
        profile_page.open_offers()