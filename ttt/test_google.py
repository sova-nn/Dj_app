# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class Auth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://gudok.tele2.ru')

    def test_auth(self):
        driver = self.driver

        element_auth = driver.find_element_by_xpath("//input[@id='auth-btn-by-ussd'][@type='submit']")
        print (element_auth)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=='main':
    unittest.main()