import os
from pathlib import Path
import sys
import unittest
import time
#from HTMLTestRunner import HTMLTestRunner
from configparser import ConfigParser
# from appium import webdriver
sys.path.extend([str(Path(__file__).resolve().parents[0]), str(Path(__file__).resolve().parents[1])])
from conf.appium_config import appium_start


current_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(os.path.join(os.path.dirname(current_path), "conf"), "config.ini")

class ProductInformation(unittest.TestCase):
    """
    TestCase: 应用首页
    Description: 1.电话授权2.关闭新人红包
    """
    # @classmethod,在此类中只进行一次初始化和清理工作
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_start()
        cls.driver.implicitly_wait(5)
        cfg = ConfigParser()
        cfg.read(config_path, encoding="u8")
        cls.tel_authorize = cfg.get("authorize", 'tel_authorize')
        cls.close_reward = cfg.get("reward", 'close_reward')

    def test_1_tel_authorize(self):
        """始终允许电话授权"""
        while True:
            if u'禁止' in self.driver.page_source:
                self.driver.switch_to.alert.accept()
                break
        time.sleep(5)

    def test_2_close_reward(self):
        """关闭新人红包奖励"""
        time.sleep(20)
        # close_reward = self.driver.find_element_by_android_uiautomator('new UiSelector().text({})'.format(self.close_reward))
        close_reward = self.driver.find_element_by_xpath("(//android.widget.TextView[@text='先去逛逛' \
        or @text='暂不更新' \
         or @text='以后更新' \
         or @text='忽略'] |\
          /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[2])[last()]")
        self.driver.implicitly_wait(60)
        close_reward.click()
        #time.sleep(1)

    def test_3_slide_player(self):
        """滑动当前页，定位播放元素"""
        shipin_bar = self.driver.find_element_by_xpath("//*[@text='视频' or @text='刷新'")
        shipin_bar.click()
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        i = 0
        while i < 10:
            try:
                """//hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/*/*/android.widget.ImageView[@clickable=\"true\"] | //hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/*/android.widget.ImageView[@clickable=\"true\"]")
"""

                """/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView
"""
                res = self.driver.find_element_by_class_name("android.widget.ImageView")
                res.click()#
                time.sleep(30)
                break
            except Exception as e:
                driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)  # 滑动屏幕

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# texture Testcase
def suite():
    suite_case = unittest.TestSuite()
    # suite.addTest(ProductInformation('test_1_tel_authorize'))  # 需要测试的用例就addTest，不加的就不会运行
    suite.addTest(ProductInformation('test_2_close_reward'))
    suite.addTest(ProductInformation('test_3_slide_player'))

    return suite_case


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
    # timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    # print(timestr)
    # 本地日期时间作为测试报告的名字
    # filename = '/Users/wangqianwen/UIautomation/uiproject/logs/' + timestr + '.html'  # 这个路径改成自己的目录路径
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='result',
    #     description=' ui report'
    # )
    # runner.run(suite)
    # fp.close()
