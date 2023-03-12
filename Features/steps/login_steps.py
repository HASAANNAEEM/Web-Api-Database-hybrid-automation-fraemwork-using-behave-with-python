from behave import *
from pages.login import LoginClass

login_page = LoginClass()


@Given('I am on login screen')
def i_am_on_login_screen(context):
    login_page.open_website(context)


@When('I enter the valid {Credential} credential')
def enter_credentials(context, Credential):
    login_page.enter_credentials(context, Credential)


@When('I hit login button')
def hit_login_button(context):
    login_page.hit_login(context)


@When('I verify dashboard is displayed')
def verify_dashboard_is_opened(context):
    login_page.verify_dashboard(context)


@Then('I quit the browser')
def quit_browser(context):
    login_page.quit_browser(context)


