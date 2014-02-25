from django.test import TestCase
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

# Test Home Page
class HomeTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_home_site(self):
		# user open web browser, navigation to home page
		self.browser.get(self.live_server_url + '/')

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Login with Facebook', body.text)