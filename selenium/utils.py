from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.action_helpers import ActionHelpers
from PIL import Image
from io import BytesIO
from config import *


filepath = os.path.dirname(__file__)
app_path = os.path.dirname(os.path.dirname(os.path.dirname(filepath)))
WD_WAIT_TIMEOUT = 30
WD_WAIT_TIMEOUT_QUICK = 3
IMPLICIT_WAIT_TIMEOUT = 10


def wait_element(driver, locator, time=WD_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located(locator))


def wait_element_clickable(driver, locator, time=WD_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))


# region android webdriver utils
def click_on_element(driver, loc, time=IMPLICIT_WAIT_TIMEOUT):
    wait_element(
        driver=driver,
        locator=loc,
        time=time
    ).click()


def send_text_into_element(driver, loc, text, time=IMPLICIT_WAIT_TIMEOUT):
    wait_element(
        driver=driver,
        locator=loc,
        time=time
    ).send_keys(text)


def check_element_displayed(driver, loc, time=IMPLICIT_WAIT_TIMEOUT):
    # implicitly_wait is set default in init appium webdriver. We can change implicitly_wait here
    # driver.implicitly_wait(3)
    try:
        WebDriverWait(driver, time).until(EC.presence_of_element_located(loc))
    except NoSuchElementException as e:
        print("Element not found: {}".format(e))
        return False
    except TimeoutException as e:
        print("Timeout: {}".format(e))
        return False
    return True


def swipe_to_right_screen(driver, times=1):
    for t in range(times):
        ActionHelpers.swipe(driver, 1000, 500, 100, 500)


def swipe_to_left_screen(driver, times=1):
    for t in range(times):
        ActionHelpers.swipe(driver, 100, 100, 1000, 100)


def tap_on_location(driver, tuple_x_y):
    ActionHelpers.tap(driver, tuple_x_y)


def scroll_from_el1_to_el2(driver, loc1, loc2):
    el1 = wait_element(driver, loc1)
    el2 = wait_element(driver, loc2)
    ActionHelpers.scroll(driver, el1, el2)


def press_android_keycode(driver, keycode):
    driver.press_keycode(keycode)


def wait_xpath(driver, xpath, time=IMPLICIT_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH, xpath)))


def appium_is_displayed_xpath(driver, xpath, time=IMPLICIT_WAIT_TIMEOUT):
    try:
        wait_element = WebDriverWait(driver, time)
        wait_element.until(EC.visibility_of_element_located((AppiumBy.XPATH, xpath)))
    except TimeoutException:
        return False
    except WebDriverException:
        return False
    return True


def wait_seconds(s=3):
    sleep(s)


def drag_drop(driver, f_locator, t_locator, add_wait_time=0):
    drag = WebDriverWait(driver, WD_WAIT_TIMEOUT + add_wait_time).until(EC.visibility_of_element_located(f_locator))
    drop = WebDriverWait(driver, WD_WAIT_TIMEOUT + add_wait_time).until(EC.visibility_of_element_located(t_locator))
    ActionChains(driver).drag_and_drop(drag, drop).perform()


def slide_element(driver, locator, x, y, add_wait_time=0):
    move = ActionChains(driver)
    slider = WebDriverWait(driver, WD_WAIT_TIMEOUT + add_wait_time).until(EC.visibility_of_element_located(locator))
    move.click_and_hold(slider).move_by_offset(x, y).release().perform()


def wait_xpath_clickable(driver, xpath, time=IMPLICIT_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath)))


def is_displayed_xpath(driver, xpath, time=IMPLICIT_WAIT_TIMEOUT):
    try:
        WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except WebDriverException:
        return False
    return True


def appium_wait_accessibility_id(driver, accessibility_id, time=IMPLICIT_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id)))


def appium_wait_xpath(driver, xpath, time=IMPLICIT_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((AppiumBy.XPATH, xpath)))


def appium_wait_uiselector_text(driver, text, time=IMPLICIT_WAIT_TIMEOUT):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')))

# endregion android webdriver utils


#region manual wait10s
def wait():
    sleep(3)

def wait_for_loading():
    sleep(20)
#endregion manual wait10s

#region wait_loading
def wait_for_loading_venta(wd, timeout:'max seconds to wait10s'=60):
    i=0; step=0.3
    while True:
        loading_icon = wd.find_elements(By.XPATH, '//*[contains(@style, "react-spinners-SyncLoader-sync")]')
        still_loading = len(loading_icon) > 0
        if not still_loading: break

        sleep(step); i += step
        if i >= timeout: raise Exception('Page loading too long')

def wait_loading_dashboard(wd, timeout:'max seconds to wait10s'=90):
    i=0; step=0.3
    while True:
        loading_icon = wd.find_elements(By.XPATH, '//*[contains(@style, "animation")]')
        still_loading = len(loading_icon) > 0
        if not still_loading: break

        sleep(step); i += step
        if i >= timeout: raise Exception('Page loading too long')

def wait_loading_mer_dashboard(wd, timeout:'max seconds to wait10s'=90):
    i=0; step=0.3
    while True:
        loading_icon = wd.find_elements(By.XPATH, '//*[@class="-loading -active"]')
        still_loading = len(loading_icon) > 0
        if not still_loading: break

        sleep(step); i += step
        if i >= timeout: raise Exception('Page loading too long')

def wait_loading_direct_bank(wd, timeout:'max seconds to wait10s'=90):
    i=0; step=0.3
    while True:
        loading_icon = wd.find_elements(By.XPATH, '//*[contains(@style, "react-spinners-PulseLoader-pulse")]')
        still_loading = len(loading_icon) > 0
        if not still_loading: break

        sleep(step); i += step
        if i >= timeout: raise Exception('Page loading too long')

def pet_wait_loading_direct_bank(wd, timeout:'max seconds to wait10s'=90):
    i=0; step=0.3
    while True:
        loading_icon = wd.find_elements(By.XPATH, '//*[(@src="/img/notice/purchase-pending.png")]')
        still_loading = len(loading_icon) > 0
        if not still_loading: break

        sleep(step); i += step
        if i >= timeout: raise Exception('Page loading too long')

def wait_loading_credit_iframe(wd, timeout:'max seconds to wait10s'=90):
    i=0; step=0.3
    while True:
        loading_icon = wd.find_elements(By.XPATH, '//*[@class="loader"]')
        still_loading = len(loading_icon) > 0
        if not still_loading: break

        sleep(step); i += step
        if i >= timeout: raise Exception('Page loading too long')

#endregion wait_loading

def take_element_screenshot(driver, element, filename='screenshot.png'):
    # Ref https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python

    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png()  # saves screenshot of entire page

    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save(filename)  # saves new cropped image


def save_element_as_png(element, file_name_wo_ext):
    # open file in write and binary mode
    with open(f"{file_name_wo_ext}.png", 'wb') as file:
        # write file
        file.write(element.screenshot_as_png)


def click_element_by_location(driver, element):
    location = element.location
    size = element.size

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    ac = ActionChains(driver)
    ac.move_to_element(element).move_by_offset(top - 1, right - 1).click().perform()

