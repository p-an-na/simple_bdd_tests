
from playwright.sync_api import Page, expect
import sys
sys.path.append('.')
from utils.pages_url import login_page, home_page
import os

username_login = os.environ.get('USERNAME_LOGIN')
username_password = os.environ.get('USERNAME_PASSWORD')

class Login():
 
    def __init__(self, page):
        self.page = page
      
    def navigate(self):
        go_to_login_page = self.page.goto(login_page)
        expect(self.page).to_have_url(login_page)
     
    def user_input_username(self):
        username = self.page.locator('[data-test="username"]')
        username.fill(username_login)
 
    def user_input_password(self):
        password = self.page.locator('[data-test="password"]')
        password.fill(username_password)

    def click_login_button(self):
        login_button = self.page.locator('[data-test="login-button"]')
        login_button.click()
         
    def verify_home_page(self):
        expect(self.page).to_have_url(home_page)