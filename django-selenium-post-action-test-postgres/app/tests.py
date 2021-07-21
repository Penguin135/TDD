from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
# Create your tests here.

class BaseTestCase(TestCase):
    def setUp(self):
        self.chrome = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        #self.chrome.implicitly_wait(5)
    
    def tearDown(self):
        self.chrome.quit()

    def test_submit(self):
        self.chrome.get('http://django:8000')
        profile_name = self.chrome.find_element_by_id('id_name')
        profile_height = self.chrome.find_element_by_id('id_height')

        submit = self.chrome.find_element_by_id('submit_button')

        profile_name.send_keys('test-name2')
        profile_height.send_keys('170')

        submit.send_keys(Keys.RETURN)

        self.chrome.get("http://django:8000")
        #self.chrome.find_element_by_xpath("//*[contains(text(), 'test-name2')]")

        self.assertIn('test-name2', self.chrome.page_source)