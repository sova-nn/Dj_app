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

        element_auth = driver.find_element_by_class_name('user-menu__item')
        element_auth.click()

        input_field = driver.find_element_by_id('msisdn')
        input_field.click()
        number = '9082304984'
        for i in range(len(number)):
            input_field.send_keys(number[i])
            time.sleep(1)

        my_btn = driver.find_element_by_xpath("//input[@id='auth-btn-by-ussd'][@type='submit']")
        my_btn.click()


        time.sleep(10)

        sms_finder = driver.find_element_by_id('auth-link-sms')
        sms_finder.click()

        time.sleep(11)
        driver.find_element_by_id('auth-link-retry-sms').click()

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=='main':
    unittest.main()