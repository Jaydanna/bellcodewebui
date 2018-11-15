# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get("https://www.bellcode.com/#/")
        driver.find_element_by_class_name("user-info").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[7]/div/div/div[1]/div[2]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[7]/div/div/div[2]/div[1]/input').send_keys("jaydan")
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[7]/div/div/div[2]/div[2]/input').send_keys("111111")
        driver.find_element_by_link_text(u"登录").click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::div[3]").click()
    
    # # def test_login(self):
    #     driver = self.driver
    #     driver.get("https://www.bellcode.com/#/")
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='首页'])[1]/preceding::div[1]").click()
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='扫码登录'])[1]/following::div[1]").click()
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[1]").click()
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[1]").clear()
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[1]").send_keys("jaydan")
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[2]").clear()
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::input[2]").send_keys("111111")
    #     driver.find_element_by_link_text(u"登录").click()
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='账号登录'])[1]/following::div[3]").click()
    
    # def test_gotoclassroom(self):
    #     driver = self.driver
    #     driver.get("https://www.bellcode.com/#/")
    #     driver.implicitly_wait(2)
    #     driver.find_element_by_link_text(u"上课").click()
    #     driver.implicitly_wait(2)
    #     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[6]/div/div[4]').click()
    #     driver.implicitly_wait(2)
    #     driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='[测试]L2直播课'])[1]/following::div[1]").click()
    #     driver.find_element_by_xpath("(//*[@id=\"app\"]/div/div/div[2]/div/div[2]/ul/li[1]/a/div[4]/div)").click()
    #     driver.find_element_by_xpath("(//*[@id=\"app\"]/div/div/div/div/div[2]/div/span)").click()

    def test_watchvideo(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.bellcode.com/#/cm/stu_lesson_map/?package_id=69&lesson_id=294&class_id=439")
        driver.find_element_by_xpath("(//*[@id=\"app\"]/div/div/div/div/div[2]/div/span)").click()
        # WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        # locator.click()
        driver.find_element_by_xpath("(//*[@id=\"app\"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/img)").click()
        driver.find_element_by_xpath("(//*[@id=\"app\"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/div/div[2]/div[3]/div[3]/span[1])").click()
        driver.find_element_by_id("control-play").click()
        driver.find_element_by_id("control-fullscreen").click()
        driver.implicitly_wait(1)
        driver.find_element_by_id("control-fullscreen").click()
        driver.find_element_by_id("control-play").click()
        time.sleep(200)
        driver.find_element_by_xpath(u'//*[@id="app"]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/div/div[2]/div[3]/div[3]/span[2]').click()
     
    
   
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
