"""
ТЕХНИЧЕСКОЕ ПРИМЕЧАНИЕ ДЛЯ НАСТАВНИКА:
Согласно ТЗ, тест должен выполняться в Google Chrome.
Однако на данном рабочем месте браузеры на движке Chromium
(Chrome, Edge) блокируются на уровне системных политик
безопасности Windows (политика RemoteDebuggingAllowed: false).
Для демонстрации корректности кода, локаторов и явных ожиданий
(WebDriverWait), тест выполнен в браузере Firefox, который
успешно отрабатывает сценарий.
Локаторы кнопок оптимизированы через XPath для тегов span,
как указано в исходном коде страницы.
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )
    # Увеличиваем ожидание до 50 секунд
    wait = WebDriverWait(driver, 50)

    try:
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        driver.get(url)

        driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

        # ИСПРАВЛЕНО: используем XPath для span, как в оригинальном коде сайта
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Явное ожидание появления текста "15"
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        final_text = driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text
        assert final_text == "15", (
            f"Ожидали 15, получили {final_text}"
        )

        print("✅ Тест калькулятора пройден успешно в Firefox!")
    finally:
        driver.quit()
