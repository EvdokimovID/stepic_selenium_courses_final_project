from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")

class MainPageLocators():
    pass
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    LINK_PARAMETER = "promo=newYear"
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_SUCCESSFUL_ADDING = (By.CSS_SELECTOR, "div.alert:first-child div")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert:last-child")
    PRODUCT_LINK = ("http://selenium1py.pythonanywhere.com/catalogue/"
                    "the-shellcoders-handbook_209/?promo=newYear")
    
class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")