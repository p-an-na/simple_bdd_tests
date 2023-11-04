import os
import sys
import pytest
from playwright.sync_api import Page, expect
sys.path.append('.')
from utils.pages_url import login_page, home_page


username_login = str(os.environ.get('USERNAME_LOGIN'))
username_password = str(os.environ.get('USERNAME_PASSWORD'))

@pytest.fixture
def set_up(page):
    
     page.goto(login_page)
     expect(page).to_have_url(login_page)    
     username = page.locator('[data-test="username"]').fill(username_login)
     password = page.locator('[data-test="password"]').fill(username_password)
     login_button = page.locator('[data-test="login-button"]')
     login_button.click()
     expect(page).to_have_url(home_page)
     yield page
     page.close()
    
