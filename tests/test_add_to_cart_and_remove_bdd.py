from pathlib import Path
from pytest_bdd import scenario, given, when, then
import sys
sys.path.append('.')
from models.add_to_cart_and_remove import AddToCartAndRemove

@scenario('features/cart.feature', 'Add to cart and remove')
def test_add_to_cart_and_remove():
    pass

@given('there is a home page')
def go_to_home_page(set_up):
    page = set_up
        
@when('user add to cart first item')
def go_to_cart(page):
    home_page = AddToCartAndRemove(page)
    home_page.add_to_cart_first_item()
    
@when('user go to cart')
def user_go_to_cart(page):
    home_page = AddToCartAndRemove(page)
    home_page.go_to_cart()
    
@then('user check item in cart and remove it')
def user_remove_item_from_cart(page):
    home_page = AddToCartAndRemove(page)
    home_page.check_items_in_cart_and_remove()
    
    