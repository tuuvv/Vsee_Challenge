from commons.mobile_driver_handler import MobileDriverHandle
from locators.main_page_locators import mainPageLocators
import time


class LoginSendMsg:

    def __init__(self):
        self.main_page_locators = mainPageLocators()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "main" page')
        time.sleep(5)

    def fill_username(self, username):
        time.sleep(5)
        self.driver_handler.send_keys(self.main_page_locators.username_field, username)
        time.sleep(5)

    def fill_password(self, password):
        self.driver_handler.send_keys(self.main_page_locators.password_field, password)
        time.sleep(5)

    def hit_signin_btn(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.Sign_In_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking Sign_In button -->", e)

    def hit_message_tbn(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.message_menu)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking hit_message button -->", e)

    def tap_Start_new_chat_textview(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.Start_new_chat_textview)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tapping Start_new_chat_textview -->", e)

    def tap_Test_Call_option(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.Test_Call_option)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tapping Test_Call_option -->", e)

    def hit_DONE_tbn(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.DONE_tbn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking DONE_tbn -->", e)

    def fill_message(self, message):
        self.driver_handler.send_keys(self.main_page_locators.Input_field, message)
        time.sleep(5)

    def hit_send_tbn(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.Send_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking Send_btn -->", e)
