from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
        
    def should_not_be_product_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
    