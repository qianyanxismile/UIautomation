import unittest
import time
from configparser import ConfigParser
from appium import webdriver
from ..conf.appium_config import appium_start


class ProductInformation(unittest.TestCase):
    """
    TestCase: xxxxx
    Description: xxxxx
    """
    # @classmethod,在此类中只进行一次初始化和清理工作
    @classmethod
    def setUpClass(self):
        self.driver = appium_start()
        time.sleep(3)

    def test_initial(self):
        cfg = ConfigParser()
        cfg.read('..conf.config.ini')
        tel_authorize = cfg.get('tel_authorize')
        close_reward = cfg.get('close_reward')
        return tel_authorize, close_reward

    def test_tel_authorize(self):
        """始终允许电话授权"""
        test_authorize = self.driver.find_element_by_id(tel_authorize)
        test_authorize.click()
        time.sleep(1)

    def test_close__reward(self):
        """关闭新人红包奖励"""
        close_reward = self.driver.find_element_by_android_uiautomator('new UiSelector().text(\"先去逛逛\")')
        close_reward[0].click()


    @classmethod
    def tearDownClass(self):
        self.driver.quit()


# texture Testcase
def suite():
    tests = [
        "test_initial",
        "test_tel_authorize",
        "test_close_reward"
    ]
    return unittest.TestSuite(map(ProductInformation, tests))


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())