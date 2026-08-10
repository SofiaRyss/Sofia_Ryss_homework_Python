"""
Тест для калькулятора с использованием Page Object Model.
Браузер: Google Chrome (по ТЗ).
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_calculator():
    # 1. Создаем и настраиваем драйвер
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    try:
        # 2. Создаем объект страницы
        page = CalculatorPage(driver)

        # 3. Выполняем сценарий через методы страницы
        page.open()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        # 4. Ждем результат и получаем его
        page.wait_for_result("15")
        result = page.get_result()

        # 5. ПРОВЕРКА (assert)
        assert result == "15", f"Ожидали 15, получили {result}"

        print("✅ Тест калькулятора пройден успешно в Chrome!")

    finally:
        # 6. Закрываем браузер
        driver.quit()
