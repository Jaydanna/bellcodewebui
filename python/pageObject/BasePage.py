from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    '''基础类，实际界面继承该类'''
    def __init__(self,selenium_driver,base_url,title):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self,title):
        '''获取当前页面的title，检查输入的title是否在当前页面中，返回比较结果'''
        return title in self.driver.driver

    def _open(self,base_url,title):
        '''默认使用get请求'''
        self.driver.get(base_url)
        assert self.on_page(title),u'打开网页失败'%base_url
    
    def open(self):
        self._open(self.base_url,self.driver.title)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print ('%s也没未找到%s元素'%(self,loc))

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc=getattr(self,'_%s'%loc)
            if clear_first:
                self.find_element(*loc).click()
                self.find_element(*loc).send_keys(value)

        except AttributeError:
            print ('%s页面中未能找到%s元素'%(self,loc))  