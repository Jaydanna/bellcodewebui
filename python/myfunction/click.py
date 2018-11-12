from selenium import webdriver
import unittest

def click_button(self,button, exc_url, cur_url):
    button.click()
    self.assertEqual(exc_url,cur_url)