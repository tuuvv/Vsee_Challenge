from pytest_bdd import parsers, scenarios, given, when, then

from pages.login_and_send_msg_page import LoginSendMsg

login_and_send_msg_page = LoginSendMsg()

scenarios('../features/login_and_send_msg.feature')


@given(parsers.parse("User fill '{username}' to Email field"))
def fill_username(username):
    login_and_send_msg_page.fill_username(username)

@when(parsers.parse("User fill '{password}' to Password field"))
def fill_password(password):
    login_and_send_msg_page.fill_password(password)

@then("User hit Sign In button")
def hit_signin_btn():
    login_and_send_msg_page.hit_signin_btn()

@then("User hit message button menu")
def hit_message_tbn():
    login_and_send_msg_page.hit_message_tbn()

@then("User tap on Start new chat textview")
def tap_Start_new_chat_textview():
    login_and_send_msg_page.tap_Start_new_chat_textview()

@then("User tap on Test Call option")
def tap_Test_Call_option():
    login_and_send_msg_page.tap_Test_Call_option()

@then("User hit on DONE button")
def hit_DONE_tbn():
    login_and_send_msg_page.hit_DONE_tbn()

@then(parsers.parse("User type '{message}' to the input"))
def fill_message(message):
    login_and_send_msg_page.fill_message(message)

@then("User hit send button")
def hit_send_tbn():
    login_and_send_msg_page.hit_send_tbn()