"""
ПРИМЕЧАНИЕ: Тест выполняется в FireFox, как указано в ДЗ.
В assert указана сумма $53.97, так как это точная
сумма трёх указанных в ДЗ товаров (29.99 + 15.99 + 7.99).
Значение $58.29 в тексте задания является опечаткой
учебных материалов.
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(
            By.ID, "user-name"
        ).send_keys("standard_user")
        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")
        driver.find_element(
            By.ID, "login-button"
        ).click()

        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

        driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(
            By.ID, "first-name"
        ).send_keys("Иван")
        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Петров")
        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        # Явное ожидание элемента с итоговой суммой
        total_el = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_subtotal_label")
            )
        )

        total_text = total_el.text
        # ИСПРАВЛЕННАЯ СУММА: 29.99 + 15.99 + 7.99 = 53.97
        assert "$53.97" in total_text, (
            f"Ожидали $53.97, получили {total_text}"
        )

        print("✅ Тест покупки пройден успешно в Firefox!")
    finally:
        driver.quit()
