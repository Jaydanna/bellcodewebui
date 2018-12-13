#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import unittest, time, re

class TestPuzzle2(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get("https://www.bellcode.com/#/")
        driver.implicitly_wait(30)
        driver.find_element_by_class_name("user-info").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[7]/div/div/div[1]/div[2]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[7]/div/div/div[2]/div[1]/input').send_keys("jaydan")
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[7]/div/div/div[2]/div[2]/input').send_keys("111111")
        driver.find_element_by_link_text(u"登录").click()
    
    def test_puzzle2(self):
        driver = self.driver
        driver.implicitly_wait(2)
        driver.get("https://ide.bellcode.com/puzzle2?pid=263&actid=3254&classid=439&package_id=69&lessonid=294&cburl=https%3A%2F%2Fwww.bellcode.com%2F%23%2Fcm%2Fstu_lesson_map%2F%3Fpackage_id%3D69%26lesson_id%3D294%26class_id%3D439")
        time.sleep(5)
        driver.find_element_by_link_text(u"跳过").click()
        when_click = driver.find_element_by_css_selector('#blocks > div.injectionDiv > svg.blocklySvg > g > g.blocklyBlockCanvas')
        move = driver.find_element_by_css_selector('#blocks > div.injectionDiv > svg.blocklyFlyout > g > g.blocklyBlockCanvas > g')
        
        # fail。。。。↓
        # number = driver.find_element_by_xpath("//*[@id='blocks']/div[1]/*[name()='svg'][4]/*[name()='g']/*[name()='g'][1]/*[name()='g']/*[name()='g'][2]/*[name()='g']")
        # # number.click()
        # print (number.text)
        # number.send_keys("100")
        when_click_xy = when_click.location
        move_xy = move.location
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(move,when_click_xy['x'],when_click_xy['y'])
        action.perform()
        time.sleep(10)
        # action.release(move)
        
       
        print (when_click_xy,move_xy)
        # self.assertEquals(when_click_xy,move_xy)
      



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
   
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
