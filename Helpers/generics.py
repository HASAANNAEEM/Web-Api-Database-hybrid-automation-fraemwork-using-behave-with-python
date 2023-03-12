import logging
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.log import Logger


class GenericMethods:
    def __init__(self):
        self.data = []
        self.log = Logger(logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'))

    # I check the visibility of element
    def wait_for_visibility_of_element(self, context, element, locate_by):
        if locate_by == "xpath":
            try:
                web_element = WebDriverWait(context.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, element)),
                    message="Element " + element + " is not present or taking too long to display")
            except TimeoutError as e:
                raise Exception('Element %s is not visible' % element)
                self.log.logger.warning(str(e))
                assert False
            return web_element

        elif locate_by == "id":
            try:
                web_element = WebDriverWait(context.driver, 20).until(
                    EC.visibility_of_element_located(By.ID(element)))
            except TimeoutError:
                raise Exception('Element %s is not visible' % element)
                log.logger.warning(e)
                assert False
            return web_element

        else:
            raise Exception('Not a valid locator')
            log.logger.warning('Not a valid locator')
            assert False

    # Check whether the element is clickable or not
    def wait_for_element_to_be_clickable(self, context, element):
        try:
            WebDriverWait(context.driver, 20).until(
                EC.element_to_be_clickable(element)
            )
        except TimeoutError:
            raise Exception('Element %s is not clickable' % element)
            self.log.logger.warning(e)
            assert False

    # Send data in input fields using send keys #
    def send_data_in_fields(self, context, input_field, value):
        self.log.logger.info("Send data in input fields using send keys")
        input_field.clear()
        input_field.send_keys(value)

    def verify_element_displayed(self, context, by_locator):
        try:
            element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutError:
            raise Exception('Element %s is not clickable' % element)
            self.log.logger.warning('Element %s is not clickable' % element)
            assert False

    def click_element_using_js(self, context, by_locator):
        try:
            element = WebDriverWait(context.driver, 30).until(EC.visibility_of_element_located(by_locator))
            context.driver.execute_script("arguments[0].click();", element)
        except TimeoutError:
            raise Exception('Element %s is not clickable' % element)
            self.log.logger.warning('Element %s is not clickable' % element)
            assert False

    def click_element(self, context, by_locator):
        try:
            time.sleep(1)
            element = WebDriverWait(context.driver, 30).until(EC.visibility_of_element_located(by_locator))
            element.click()
        except TimeoutError:
            raise Exception('Element %s is not clickable' % element)
            self.log.logger.warning('Element %s is not clickable' % element)
            assert False

    def click_element_with_locator(self, context, locator):
        try:
            time.sleep(1)
            by_locator = (By.XPATH, locator)
            element = WebDriverWait(context.driver, 30).until(EC.visibility_of_element_located(by_locator))
            context.driver.execute_script("arguments[0].click();", element)
        except TimeoutError:
            raise Exception('Element %s is not clickable' % element)
            self.log.logger.warning('Element %s is not clickable' % element)
            assert False

    def input_element(self, context, by_locator, text):
        try:
            WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
            WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutError:
            raise Exception('Input value into element is not possible')
            self.log.logger.warning('Input value into element is not possible')
            assert False

    # Scrolling to element
    def scroll_to_element(self, context, by_locator):
        try:
            self.log.logger.info("Scrolling to element")
            element = WebDriverWait(context.driver, 15).until(EC.presence_of_element_located(by_locator))
            actions = ActionChains(context.driver)
            actions.move_to_element(element).perform()
            # actions.click()
        except Exception as e:
            raise Exception('Scrolling to element')
            self.log.logger.warning('Scrolling to element')
            assert False

    # Scrolling to element
    def scroll_to_element_with_locator(self, context, locator):
        try:
            time.sleep(1)
            self.log.logger.info("Scrolling to element")
            by_locator = (By.XPATH, locator)
            element = WebDriverWait(context.driver, 15).until(EC.presence_of_element_located(by_locator))
            actions = ActionChains(context.driver)
            actions.move_to_element(element).perform()
            # actions.click()
        except Exception as e:
            raise Exception('Scrolling to element')
            self.log.logger.warning('Scrolling to element')
            assert False

    # hover to element and click
    def hover_to_element_and_click(self, context, element):
        try:
            self.log.logger.info("hover to element and click")
            actions = ActionChains(context.driver)
            actions.move_to_element(element).perform()
            actions.click(element)
        except Exception as e:
            raise Exception('hover to element')
            self.log.logger.warning('hover to element and click')
            assert False

    # hover to element
    def hover_to_element(self, context, element):
        try:
            self.log.logger.info("hover to element")
            actions = ActionChains(context.driver)
            actions.move_to_element(element).perform()
        except Exception as e:
            raise Exception('hover to element')
            self.log.logger.warning('hover to element')
            assert False

    def verify_element_enable(self, context, by_locator):
        try:
            element = WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located(by_locator))
            return element.is_enabled()
        except Exception as e:
            self.log.logger.warning('Element is not clickable')

    def get_element_text(self, context, by_locator):
        try:
            element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except Exception as e:
            self.log.logger.warning('Element %s is not clickable' % element)

    def get_web_element(self, context, by_locator):
        try:
            element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element
        except Exception as e:
            self.log.logger.warning('Element %s is not clickable' % element)

    def get_web_elements(self, context, by_locator):
        try:
            element = WebDriverWait(context.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
            return element
        except Exception as e:
            self.log.logger.warning('Element %s is not clickable' % element)

    def get_web_element_text(self, context, element):
        try:
            return element.text
        except Exception as e:
            self.driver.quit()
            self.log.logger.warning('Element %s is not clickable' % element)

    def verify_values(self, context, actual, expected):
        try:
            assert actual in expected, "Error actual value : " + actual + " not as expected value : " + expected
        except AssertionError as e:
            self.log.logger.warning(str(e))
            assert False, str(e)
