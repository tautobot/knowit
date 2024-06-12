from automation.chrome.tiktok.pages.home_page import TiktokHomePage
from automation.chrome.base import BaseTest


class Test(BaseTest):

    def setUp_fixture(self):
        # self.login_page                 = LoginWebPortalPage(self.driver)
        self.home_page                  = TiktokHomePage(self.driver)

    def test_login_tiktok(self):
        self.setUp_fixture()
        self.home_page.login_w_qr('URL.TIKTOK_HOME')

