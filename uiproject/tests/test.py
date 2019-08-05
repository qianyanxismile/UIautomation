# coding: utf-8
import os
from pathlib import Path
import sys
import unittest
import time
from configparser import ConfigParser
from appium import webdriver
sys.path.extend([str(Path(__file__).resolve().parents[0]), str(Path(__file__).resolve().parents[1])])
from conf.appium_config import appium_start

current_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(os.path.join(os.path.dirname(current_path), "conf"), "config.ini")

class ProductInformation(unittest.TestCase):
    """
    TestCase: xxxxx
    Description: xxxxx
    """
    # @classmethod,在此类中只进行一次初始化和清理工作
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_start()
        time.sleep(3)
        cfg = ConfigParser()
        cfg.read(config_path, encoding="u8")
        cls.tel_authorize = cfg.get("authorize", 'tel_authorize')
        cls.close_reward = cfg.get("reward", 'close_reward')

    def test_tel_authorize(self):
        """始终允许电话授权"""
        test_authorize = self.driver.find_element_by_id(self.tel_authorize)
        test_authorize.click()
        time.sleep(1)

    def test_close_reward(self):
        """关闭新人红包奖励"""
        close_reward = self.driver.find_element_by_android_uiautomator('new UiSelector().text({})'.format(self.close_reward))
        close_reward[0].click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# texture Testcase
def suite():
    tests = [
        "test_tel_authorize",
        "test_close_reward"
    ]
    return unittest.TestSuite(map(ProductInformation, tests))


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())