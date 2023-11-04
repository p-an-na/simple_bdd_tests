import sys
sys.path.append('.')
from models.login import Login


def test_login(page):
    
    login_page = Login(page)    
    login_page.navigate()
    login_page.user_input_username()
    login_page.user_input_password()
    login_page.click_login_button()
    login_page.verify_home_page()
    
    


