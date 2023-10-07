'''
@filename: /homePage
@time: 2023/9/20 11:50
'''
from selenium.webdriver.common.by import By
from page.basePage import BasePage


from selenium import webdriver

class ProfilePage(BasePage):

	def open_profile(self):
		self.driver.get('https://nftgo.io/account/ETH/0x59d63f8a9c8de8e1ff59898638f53597b6d41ee3/NFT')

	def info(self):
		self.portfolio_value = self.find_element(self.driver, By.CLASS_NAME, 'tokenClassName')
		print("portfolio_value:",self.portfolio_value.text)

	def open_offers(self):
		self.find_element(self.driver,By.XPATH,"//span[@class='page-tab_text__i9_Uf' and text()='Offers']").click()
		print("11111111open_offers")

