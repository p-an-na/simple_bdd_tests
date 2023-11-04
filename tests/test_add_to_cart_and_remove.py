import sys
sys.path.append('.')
from models.add_to_cart_and_remove import AddToCartAndRemove


def test_add_to_cart_and_remove(set_up):
    page = set_up
    
    home_page = AddToCartAndRemove(page)
    home_page.add_to_cart_first_item()
    home_page.go_to_cart()
    home_page.check_items_in_cart_and_remove()
    
    