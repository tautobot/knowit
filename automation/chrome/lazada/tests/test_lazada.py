from automation.chrome.lazada.pages.adsense_login_page import LazadaAdsensePage
from automation.chrome.base import BaseTest
from common.enums import Languages, LoginTypes


class Test(BaseTest):

    def setUp_fixture(self):
        self.home_page = LazadaAdsensePage(self.driver)

    def test_login_adsense_lazada(self):
        print(f"self: {self}")
        self.setUp_fixture()
        self.home_page.login('URL.LAZADA_ADSENSE_HOME', Languages.EN, LoginTypes.ACCOUNT)

