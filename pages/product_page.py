from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
        
    def add_product_to_basket(self): 
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
    
    def should_be_promo_parameter_in_link(self):
        current_url = self.browser.current_url
        assert ProductPageLocators.LINK_PARAMETER in current_url, f"Error url: {current_url}"

    def should_be_product_title_in_message(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        successful_adding_message = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESSFUL_ADDING).text
        print(successful_adding_message)
        assert f"{product_title} has been added to your basket." == successful_adding_message, \
            f"Message of successful adding product is not correct on page {self.url}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESSFUL_ADDING), \
        "Success message is presented, but should not be"
        
    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESSFUL_ADDING), \
        "Success message is not disappear, but should be"
    
    def should_be_product_price_in_message(self): 
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
        assert product_price in basket_price_message, "Total basket price is not correct"
