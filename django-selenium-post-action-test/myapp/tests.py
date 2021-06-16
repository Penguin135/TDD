from unittest import signals
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

import subprocess
import os
import signal

# Create your tests here.
class MyTest(TestCase):
    def setUp(self):
        sp = subprocess.Popen(
        ['python', 'manage.py', 'runserver'], stdout=subprocess.PIPE)
        self.sp_pid = sp.pid
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()
        os.kill(self.sp_pid, signal.SIGTERM)

    # def test_1(self):
    #     self.assertEqual(1+1, 2)

    def test_2(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('myapp', self.browser.title)

        # try:
        #     myElement = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'submit_button')))
        #     print('page is ready')
        # except TimeoutException:
        #     print('Loading took too much time')

    def test_3(self):
        self.browser.get('http://localhost:8000')
        # try:
        #     myElement = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'submit_button')))
        #     print('page is ready')
        # except TimeoutException:
        #     print('Loading took too much time')

        profile_name = self.browser.find_element_by_id('id_name')
        profile_height = self.browser.find_element_by_id('id_height')

        submit = self.browser.find_element_by_id('submit_button')

        profile_name.send_keys('test-name2')
        profile_height.send_keys('170')

        submit.send_keys(Keys.RETURN)

        self.browser.get("http://localhost:8000")
        self.browser.find_element_by_xpath("//*[contains(text(), 'test-name2')]")

        self.assertIn('test-name2', self.browser.page_source)