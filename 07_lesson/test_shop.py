"""
Тест для интернет-магазина с использованием Page Object Model.
Браузер: Firefox (по ТЗ).
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from shop_pages import LoginPage, ProductsPage, CartPage, CheckoutPage


def test_shop_checkout():
    # 1. Создаем и настраиваем драйвер (Firefox)
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )

    try:
        # 2. Авторизация
        login_page = LoginPage(driver)
        login_page.open().login("standard_user", "secret_sauce")

        # 3. Добавление товаров в корзину и переход в неё
        products_page = ProductsPage(driver)
        products_page.add_backpack_to_cart() \
                     .add_bolt_tshirt_to_cart() \
                     .add_onesie_to_cart() \
                     .go_to_cart()

        # 4. Переход к оформлению
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        # 5. Заполнение данных (можешь вписать свои реальные данные)
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("Sofia", "Ryss", "12345")

        # 6. Получение итоговой суммы и проверка
        total_text = checkout_page.get_total_price()

        # ВАЖНО: Сайт добавляет налог к стоимости товаров.
        # Сумма товаров: $29.99 + $15.99 + $7.99 = $53.97
        # Плюс налог (~8%) = $4.32
        # Итого: $58.29
        assert "$58.29" in total_text, f"Ожидали $58.29, получили: {total_text}"

        print("✅ Тест интернет-магазина пройден успешно в Firefox!")

    finally:
        # 7. Закрываем браузер
        driver.quit()
