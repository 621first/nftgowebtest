'''
@filename: /topcollPage
@time: 2023/10/7 16:03
'''
from selenium.webdriver.common.by import By
from page.basePage import BasePage
import time
from selenium.webdriver.common.keys import Keys



from selenium import webdriver

SNAPSHOTS_DIR = 'snapshots'


class TopcollPage(BasePage):

	def open_topcoll(self):
		self.driver.get('https://nftgo.io/discover/top-collections')
		self.find_element(self.driver,By.XPATH,'//span[@class="sc-bczRLJ sc-gsnTZi fNQVyA fuKjun pop-up-modal_closeIcon__Jst7n"]').click()


	def search_coll(self,keyword):
		# ele = self.find_element(self.driver,By.XPATH,"//input[@class='search-input_searchInput__hmtqI']")
		ele = self.find_elements(self.driver,By.XPATH,'//input[@id="scaffoldSearchInput"]')[1]
		if ele.is_displayed():
			ele.send_keys(keyword)
		else:
			print(1111111111111)
		time.sleep(10)

