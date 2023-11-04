from pathlib import Path
from pytest_bdd import scenario, given, when, then
import sys
sys.path.append('.')
from models.login import Login


@scenario('features/login.feature', 'User Login')
def test_login_bdd():
    print('starting bdd test')

    
@given('there is a login page')    
def goto_website(page):
    login_page = Login(page)
    login_page.navigate()
     
@when('user input correct username')    
def user_input_username(page):
    login_page = Login(page)
    login_page.user_input_username()

@when('user input correct password')    
def user_input_password(page):
    login_page = Login(page)
    login_page.user_input_password()

@when('user click login button')    
def login(page):
    login_page = Login(page)
    login_page.click_login_button()

        
@then('user can see home page')    
def home_page(page):
    login_page = Login(page)
    login_page.verify_home_page()