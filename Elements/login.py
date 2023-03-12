from selenium.webdriver.common.by import By


class LoginElements:
    username_field = '//input[@name="UserName"]'
    password_field = '//input[@name="Password"]'
    login_button = '//button[@type="submit"]'
    verification_text = '//span[text()="Control Tower"]'
    ignore_button = '//button[contains(text(),"Ignore and continue")]'

