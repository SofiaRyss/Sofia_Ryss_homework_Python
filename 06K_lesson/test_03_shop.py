from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def test_shop_purchase():
    # 1. Открываем в Firefox
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )

    try:
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизуемся
        driver.find_element(
            By.ID, "user-name"
        ).send_keys("standard_user")
        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")
        driver.find_element(
            By.ID, "login-button"
        ).click()

        # 3. Добавляем товары
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

        # 4. Корзина
        driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()

        # 5. Checkout
        driver.find_element(By.ID, "checkout").click()

        # 6. Форма
        driver.find_element(
            By.ID, "first-name"
        ).send_keys("Иван")
        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Петров")
        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("123456")

        # 7. Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Читаем Total
        total_el = driver.find_element(By.ID, "total")
        total = total_el.text

        # 9. Закрываем
        driver.close()

        # 10. Проверяем
        assert total == "$58.29", (
            f"Ожидали $58.29, получили {total}"
        )

        print("✅ Тест покупки пройден!")

    finally:
        driver.quit()
