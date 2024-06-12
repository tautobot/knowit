import unittest
from automation.appium_weddriver import android_webdriver
from automation.android.tiktok.pages.home_page import AndroidTikTokHomePage
from automation.android.tiktok.pages.shop_page import AndroidTikTokShopPage


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = android_webdriver()
        self.home_page = AndroidTikTokHomePage(self.driver)
        self.shop_page = AndroidTikTokShopPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # group fixed
    def test_login_tiktok(self):
        self.home_page.open_app()
        self.home_page.login_w_username('TIKTOK_ACC', 'TIKTOK_PASS', 'TIKTOK_LOGGED')
        self.shop_page.create_product_from_flash_sale()
        # self.shop_page.demo()

