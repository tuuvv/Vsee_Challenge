from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base import BasePage
import time

SLOW = 5


class HomePage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h1')

    USERNAME = (By.ID, 'identifierId')
    GGBTN = (By.XPATH, '//*[@id="openid-buttons"]/button[1]')
    NEXTBTN = (By.ID, 'identifierNext')
    PASSWORD = (By.NAME, 'password')
    NEXTPASSBTN = (By.ID, 'passwordNext')
    COMPOSEBTN = (By.XPATH, '//div[@class="aic"]/div/div')
    RECIPIPENTS = (By.XPATH, '//div[@class="aH9"]/input')
    SUBJECT = (By.NAME,'subjectbox')
    CONTENT = (By.XPATH, '//div[@aria-label="Message Body"]')
    CONTENTAVAILABLE = (By.XPATH, '//div[@class="Ao"]')
    SENDBTN = (By.XPATH,'//div[4]/table/tbody/tr/td/div/div[2]/div')

    def __init__(self, browser):
        self.browser = browser

    def type_username_to_input(self, username):
        self.browser.find_element(*self.USERNAME).send_keys(username)
        time.sleep(SLOW)

    def type_password_to_input(self, password):
        self.browser.find_element(*self.PASSWORD).send_keys(password)
        time.sleep(SLOW)

    def type_recipients_input(self, email):
        self.browser.find_element(*self.RECIPIPENTS).send_keys(email)
        time.sleep(SLOW)

    def type_subject_input(self, subject):
        self.browser.find_element(*self.SUBJECT).send_keys(subject)
        time.sleep(SLOW)

    def type_content_input(self, content):
        ele = self.browser.find_element(*self.CONTENT)
        ele.click()
        ele.send_keys(content)
        time.sleep(SLOW)

    def click_sub_page_link(self, page_name):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        for link in links:
            if link.text.startswith(page_name):
                link.click()
                break


    def get_subpage_list(self):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        titles = [link.text.split(" (")[0] for link in links]
        return titles

    def get_current_url(self):
        return self.browser.current_url

    def click_next_button(self):
        links = self.browser.find_elements(*self.NEXTBTN)
        for link in links:
            link.click()
            time.sleep(SLOW)
            break

    def click_pass_next_button(self):
        links = self.browser.find_elements(*self.NEXTPASSBTN)
        for link in links:
            link.click()
            break
        time.sleep(SLOW)

    def click_Compose_button(self):
        links = self.browser.find_elements(*self.COMPOSEBTN)
        print("lenght:", len(links))
        links[0].click()
        time.sleep(5)

    def click_send_button(self):
        links = self.browser.find_elements(*self.SENDBTN)
        print("lenght:", len(links))
        links[0].click()
        time.sleep(5)

