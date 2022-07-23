from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By

class BasePage():

    BASE_URL = "https://www.gmail.com"

    @property
    @abstractmethod
    def PAGE_TITLE(self):
      pass

    @abstractmethod
    def get_page_title_text(self):
      pass


    def __init__(self, browser):
        self.browser = browser

