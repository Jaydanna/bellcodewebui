#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from python.driver.browsers import *
from selenium import webdriver
import time
import unittest

class HeaderBar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.bellcode.com"
        self.driver.get(self.base_url + "/")
        time.sleep(5)
        self.all_tabs = ['首页', '上课', '游乐场', '编程教育']
        print ("setup")

    def tearDown(self):
        self.driver.quit()
        print ("teardown")

    # _tab_1 = "//*[@id="app"]/div/div/div[1]/div[1]/div/div[2]/div[1]"
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(30)
    #     cls.base_url = "https://www.bellcode.com"
    #     cls.driver.get(cls.base_url + "/")
    #     time.sleep(5)
    #     cls.all_tabs = ['首页', '上课', '游乐场', '编程教育']
    #     # cls.driver = webdriver.Chrome()
    #     # cls.base_url = "https://www.bellcode.com"

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_find_all_tabs(self,cls):
        s_tab = self.driver.find_element_by_class_name("tab").text
        l_tab = s_tab.split() #<class 'list'> ['首页', '上课', '游乐场', '编程教育']
        self.assertSequenceEqual(l_tab,self.all_tabs)
        tab_1 = self.driver.find_element_by_class_name("selected")
        self.assertEqual(tab_1.text,l_tab[0])
        print ("当前处于首页")
    
    def test_click_classroom(self):
        tab = self.driver.find_element_by_link_text("上课")
        tab.click()
        time.sleep(2)
        cur_url = self.driver.current_url
        except_url = self.base_url + "/#/login"
        self.assertEqual(cur_url,except_url)
        print ("跳转至登录√")

    def test_click_game(self):
        tab = self.driver.find_element_by_link_text("游乐场")
        tab.click()
        time.sleep(2)
        cur_url = self.driver.current_url
        except_url = self.base_url + "/#/play/cardbook/characters"
        self.assertEqual(cur_url,except_url)
        print ("跳转至游乐场√")

    def test_click_codeEdu(self):
        tab = self.driver.find_element_by_link_text("编程教育")
        tab.click()
        time.sleep(2)
        except_url = self.base_url + "/#/bell_education"
        now_handle = self.driver.current_window_handle #获取当前窗口句柄
        all_handles = self.driver.window_handles #获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                # print (handle)    #输出待选择的窗口句柄
                self.driver.switch_to_window(handle)
                time.sleep(5)
                cur_url = self.driver.current_url
                self.assertEqual(cur_url,except_url)             
        print ("跳转至少儿编程√")
        self.driver.close() #关闭当前窗口
        self.driver.switch_to_window(now_handle)

if __name__ == '__main__':
    unittest.main()