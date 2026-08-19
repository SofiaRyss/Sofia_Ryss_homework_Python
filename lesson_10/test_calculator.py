"""
Тест для калькулятора с использованием Page Object Model.
Браузер: Google Chrome (по ТЗ).
"""
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.title("Проверка работы медленного калькулятора в Chrome")
@allure.description(
    "Тест открывает калькулятор, устанавливает задержку, "
    "вводит выражение '7 + 8 =' и проверяет корректность результата."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    """
    Тестирование базовых операций калькулятора.

    :return: None
    """
    with allure.step("Инициализация и настройка драйвера Chrome"):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    try:
        with allure.step("Создание объекта страницы и открытие сайта"):
            page = CalculatorPage(driver)
            page.open()

        with allure.step("Установка задержки и ввод выражения '7 + 8 ='"):
            page.set_delay(45)
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Ожидание и получение результата"):
            page.wait_for_result("15")
            result = page.get_result()

        with allure.step("Проверка (assert) полученного результата"):
            assert result == "15", f"Ожидали 15, получили {result}"
            allure.attach(result, name="Фактический результат",
                          attachment_type=allure.attachment_type.TEXT)

        print("✅ Тест калькулятора пройден успешно в Chrome!")

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
