"""
Тест для интернет-магазина с использованием Page Object Model.
Браузер: Firefox (по ТЗ).
"""
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from shop_pages import LoginPage, ProductsPage, CartPage, CheckoutPage


@allure.title("Проверка полного цикла оформления заказа в SauceDemo")
@allure.description(
    "Тест выполняет авторизацию, добавляет три товара в корзину, "
    "переходит к оформлению, заполняет данные и проверяет "
    "итоговую сумму с учетом налога."
)
@allure.feature("Корзина и оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_checkout():
    """
    Тестирование процесса покупки в интернет-магазине.

    :return: None
    """
    with allure.step("Инициализация и настройка драйвера Firefox"):
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install())
        )

    try:
        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.open().login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину и переход в неё"):
            products_page = ProductsPage(driver)
            products_page.add_backpack_to_cart() \
                         .add_bolt_tshirt_to_cart() \
                         .add_onesie_to_cart() \
                         .go_to_cart()

        with allure.step("Переход к оформлению заказа"):
            cart_page = CartPage(driver)
            cart_page.proceed_to_checkout()

        with allure.step("Заполнение данных покупателя"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_info("Sofia", "Ryss", "12345")

        with allure.step("Получение итоговой суммы и проверка (assert)"):
            total_text = checkout_page.get_total_price()

            # ВАЖНО: Сайт добавляет налог к стоимости товаров.
            # Сумма товаров: $29.99 + $15.99 + $7.99
            # = $53.97
            # Плюс налог (~8%) = $4.32
            # Итого: $58.29
            assert "$58.29" in total_text, (
                f"Ожидали $58.29, получили: {total_text}"
            )

            # Добавляем итоговую сумму в отчёт для наглядности
            allure.attach(
                total_text,
                name="Итоговая сумма в чеке",
                attachment_type=allure.attachment_type.TEXT
            )

        print("✅ Тест интернет-магазина пройден успешно в Firefox!")

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
