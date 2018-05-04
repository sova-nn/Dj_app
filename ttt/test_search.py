# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class GoSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://gudok.tele2.ru/info')

    def test_Goo(self):
        driver = self.driver

        titles = driver.find_elements_by_class_name('container textpage smallpad')
        for title in titles:
            assert '0550' in title.text()

    def tearDown(self):
        self.driver.quit()

if __name__=='main':
    unittest.main()