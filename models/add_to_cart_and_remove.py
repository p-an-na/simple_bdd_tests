import sys
from playwright.sync_api import expect
sys.path.append('.')
from utils.pages_url import cart_page

class AddToCartAndRemove():
    def __init__(self, page):
        self.page = page
        
    def add_to_cart_first_item(self):
        first_item_add_to_cart = self.page.locator('text=Add to cart').first
        first_item_add_to_cart.click()
        
    def go_to_cart(self):
        cart = self.page.locator('#shopping_cart_container a')
        cart.click()
        expect(self.page).to_have_url(cart_page)
        
    def check_items_in_cart_and_remove(self):
        number_of_items = self.page.locator('#cart_contents_container >> text=1')
        expect(number_of_items).to_have_text('1')

        remove_button = self.page.locator('text=Remove')
        remove_button.click()
        expect(number_of_items).not_to_be_visible()
        
        
        

        