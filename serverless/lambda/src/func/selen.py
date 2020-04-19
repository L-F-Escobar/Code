import time
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from lib.log import get_logger

LOG = get_logger(
    "selen.py",
    "'[%(levelname)s] [%(name)s] [%(asctime)s] [%(funcName)s::%(lineno)d] [%(message)s]'",
)

class SeleniumDriver():
    '''
        Allows a user to perform necessary selenium tasks.
    '''
    def __init__(self):
        try:
            self.vars = {}
            options = Options()
            options.binary_location = '/opt/headless-chromium'
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--single-process')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--enable-logging')
            options.add_argument('--log-level=0')
            options.add_argument('--user-data-dir=/tmp/user-data')
            options.add_argument('--ignore-certificate-errors')
            options.add_experimental_option("prefs", {
                "download.default_directory": r"/downloads",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            })
            self.driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
            LOG.info(f"Headless Chrome Initialized.")
            self.driver.implicitly_wait(2)
        except Exception as error:
            LOG.error(
                {
                    "exception_type": type(error).__name__,
                    "error_reason": error.args,
                    "traceback": traceback.format_exc(),
                }
            )


    def login_example(self, url=None, vars=None):
        '''
            Logs in to provided url.
    
            Parameters:
            - url (str) : 
            - vars (Box): Variables from custom_context.
    
            Returns:
            - T/F (bool) : Log in was successful or not.
        '''
        try:
            driver = self.driver
            driver.get(url)
    
            driver.find_element_by_id("signin-login").click()
            driver.find_element_by_id("signin-login").clear()
            driver.find_element_by_id("signin-login").send_keys(str(os.environ['username']))
        
            driver.find_element_by_id("signin-password").click()
            driver.find_element_by_id("signin-password").clear()
            driver.find_element_by_id("signin-password").send_keys(str(os.environ['password']))
        
            driver.find_element_by_id("signin-submit").click()

            if driver.title == 'Log in unsuccessful':
                LOG.info(f"Invalid username or password.")
                return False
            return True
        except Exception as error:
            LOG.error(
                {
                    "exception_type": type(error).__name__,
                    "error_reason": error.args,
                    "traceback": traceback.format_exc(),
                }
            )
            return False


    def end_session(self):
        ''' Simply ends the selenium session. '''
        try:
            self.driver.close();
            self.driver.quit();
            LOG.info("Selenium session ended.")
        except Exception as error:
            LOG.error(
                {
                    "exception_type": type(error).__name__,
                    "error_reason": error.args,
                    "traceback": traceback.format_exc(),
                }
            )


    def switch_to_new_window_example(self):
        '''
            Allows selenium bot to navigate from one window to another.

            Returns:
                - self.driver (selenium obj) : a webdriver with the new current window.
        '''
        driver = self.driver

        # Click on a button which produces a new window.
        driver.find_element(By.CSS_SELECTOR, ".css that will produce a new window").click()

        # Grab all current windows.
        self.vars["window_handles"] = driver.window_handles

        self.vars["new_window"] = self.wait_for_window(timeout=2000, driver=driver)

        driver.switch_to.window(self.vars["new_window"])

        self.driver = driver


    def wait_for_window(self, timeout=0, driver=None):
        '''
            Allows time for selenium script to execute html code target=_blank.
            Once a new window is opened, isolate new window and return it.

            Parameters:
                - timeout (int) : If a user passes in 2000, then timeout total will be 2 seconds.
                - driver (class obj) : selenium chrome webdriver session.

            Returns:
                - new window (str) : Will return the new window id.
        '''
        time.sleep(round(timeout / 1000))
        # All current windows.
        wh_now = driver.window_handles
        # Had previously caputred all current windows when there was only 1 window.
        wh_then = self.vars["window_handles"]

        # .difference .pop will drop all windows that are in common from both sets.
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()