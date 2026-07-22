"""
Классы Page Object для интернет-магазина SauceDemo.
Сайт: https://www.saucedemo.com/
Браузер: Firefox (по ТЗ)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации."""
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return self


class ProductsPage:
    """Главная страница магазина со списком товаров."""

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        return self

    def add_bolt_tshirt_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        return self

    def add_onesie_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return self


class CartPage:
    """Страница корзины."""

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        return self


class CheckoutPage:
    """Страница оформления заказа."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total_price(self):
        # Ждем появления блока с итоговой суммой
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label"))
        )
        return total_element.text
