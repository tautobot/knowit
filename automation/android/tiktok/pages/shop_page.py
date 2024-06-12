from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from automation.utils import (
    click_on_element,
    send_text_into_element,
    check_element_displayed,
    wait_seconds,
    swipe_to_right_screen,
    swipe_to_left_screen,
    tap_on_location,
    scroll_from_el1_to_el2,
    press_android_keycode
)


class AndroidTikTokShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.chrome_app = AppiumBy.ACCESSIBILITY_ID, 'Chrome'
        self.tiktok_app = AppiumBy.ACCESSIBILITY_ID, 'TikTok'

        self.home_btn = AppiumBy.ACCESSIBILITY_ID, 'Home'
        self.shop_btn = AppiumBy.ACCESSIBILITY_ID, 'Shop'
        self.friends_btn = AppiumBy.ACCESSIBILITY_ID, 'Friends'
        self.inbox_btn = AppiumBy.ACCESSIBILITY_ID, 'Inbox'
        self.profile_btn = AppiumBy.ACCESSIBILITY_ID, 'Profile'
        self.create_btn = AppiumBy.ACCESSIBILITY_ID, 'Create'

        self.orders                        = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Orders"]'
        self.free_shipping                 = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Free Shipping"]'
        self.messages                      = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Messages"]'
        self.buy_local                     = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Buy Local"]'
        self.bonus                         = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Bonus"]'
        self.creator                       = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Creator"]'
        self.address                       = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Address"]'
        self.payment                       = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Payment"]'
        self.help                          = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Help"]'
        self.policies                      = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.text.FlattenUIText[@content-desc="Policies"]'

        self.flash_sale_all                = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="::"]'
        self.flash_sale_1                  = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[contains(@content-desc,"₫")][1]'
        self.flash_sale_2                  = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[contains(@content-desc,"₫")][2]'
        self.flash_sale_3                  = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[contains(@content-desc,"₫")][3]'
        self.flash_sale_4                  = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[contains(@content-desc,"₫")][4]'
        self.flash_sale_product            = '//com.lynx.tasm.behavior.ui.list.UIList/following-sibling::com.ss.android.ugc.aweme.ecommerce.ui.EcomFlattenUIImage[{0}]'
        self.view_more                     = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.list.UIList/following-sibling::com.ss.android.ugc.aweme.ecommerce.ui.EcomFlattenUIImage[{0}]/preceding-sibling::com.lynx.tasm.behavior.ui.LynxFlattenUI[@content-desc="View more"]'

        self.horizontal_menu_all           = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="All"]'
        self.horizontal_menu_beauty        = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Beauty"]'
        self.horizontal_menu_womenswear    = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Womenswear"]'
        self.horizontal_menu_menswear      = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Menswear"]'
        self.horizontal_menu_personal_care = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Personal care"]'
        self.horizontal_menu_electronics   = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Electronics"]'
        self.horizontal_menu_baby          = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Baby"]'
        self.horizontal_menu_food          = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Food"]'
        self.horizontal_menu_foodwear      = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Foodwear"]'
        self.horizontal_menu_sports        = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Sports"]'
        self.horizontal_menu_health        = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Health"]'
        self.horizontal_menu_accessories   = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Accessories"]'
        self.horizontal_menu_household     = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Household"]'
        self.horizontal_menu_vehicle       = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Vehicle"]'
        self.horizontal_menu_bags          = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Bags"]'
        self.horizontal_menu_appliances    = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Appliances"]'
        self.horizontal_menu_textiles      = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Textiles"]'
        self.horizontal_menu_kidswear      = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Kidswear"]'
        self.horizontal_menu_kitchen       = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Kitchen"]'
        self.horizontal_menu_toys          = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Toys"]'
        self.horizontal_menu_pets_and_toys = AppiumBy.XPATH, '//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="Pets & Toys"]'

    def create_product_from_flash_sale(self):
        click_on_element(self.driver, self.shop_btn)
        wait_seconds(2)
        click_on_element(self.driver, self.flash_sale_all)
        count = 0
        # TODO: Change rule to always see 4 items, will never see 5th item
        for i in range(1, 3*1000, 3):
            count += 1
            # has_view_more = check_element_displayed(self.driver, self.view_more)
            loc1 = AppiumBy.XPATH, self.flash_sale_product.format(i)
            click_on_element(self.driver, loc1)
            wait_seconds(2)
            # Todo: Create product to owner shop here
            press_android_keycode(self.driver, AndroidKey.BACK)
            loc2 = AppiumBy.XPATH, self.flash_sale_product.format(i+3)
            scroll_from_el1_to_el2(self.driver, loc2, loc1)

    def demo(self):
        wait_seconds(1)
        loc1 = AppiumBy.XPATH, self.flash_sale_product.format(1 + 3)
        loc2 = AppiumBy.XPATH, self.flash_sale_product.format(1)
        scroll_from_el1_to_el2(self.driver, loc1, loc2)
