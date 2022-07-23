import time

from pytest_bdd import scenarios, when, then, parsers, given
from pages.Login_function import HomePage
from pages.base import BasePage
from sttable import parse_str_table

scenarios('../features/Login_function.feature')


# a
@given('I have navigated to the gmail.com page')
def navigate_to(browser):
    url = BasePage.BASE_URL
    browser.get(url)


@when(parsers.parse("I type '{username}' to the input field"))
def type_username_to_input(browser, username):
    print("step type_username_to_input")
    HomePage(browser).type_username_to_input(username)


@then(parsers.parse("I type '{password}' to the input field"))
def type_password_to_input(browser, password):
    print("step type_password_to_input")
    HomePage(browser).type_password_to_input(password)

@then(parsers.parse("I entering the '{email}' to the mail recipients input"))
def type_recipients_input(browser, email):
    print("step type_precipients_input")
    HomePage(browser).type_recipients_input(email)

@then(parsers.parse('I entering the "{subject}" to the Subject input'))
def type_subject_input(browser, subject):
    print("step type_subject_input")
    HomePage(browser).type_subject_input(subject)

@then(parsers.parse('the body message text is\n{paragraph}'))
def type_content_input(browser, paragraph):
    print("step type_content_input")
    HomePage(browser).type_content_input(paragraph)


@then("the gmail.com page opens")
def verify_gmail_page_opens(browser):
    print("step verify_gmail_page_opens")
    assert "inbox" in HomePage(browser).get_current_url()


@then("I click on the next button")
def click_next_button(browser):
    print("step click_next_button")
    HomePage(browser).click_next_button()

@then("I click on the password next button")
def click_pass_next_button(browser):
    print("step click_pass_next_button")
    HomePage(browser).click_pass_next_button()

@then("I click on Compose button")
def click_Compose_button(browser):
    print("step click_Compose_button")
    HomePage(browser).click_Compose_button()

@then("I click send button")
def click_send_button(browser):
    print("step click_send_button")
    HomePage(browser).click_send_button()

