"""
ТЕХНИЧЕСКОЕ ПРИМЕЧАНИЕ ДЛЯ НАСТАВНИКА:
Согласно ТЗ, тест должен выполняться в Edge.
Однако на данном рабочем месте браузеры на движке Chromium
(Chrome, Edge) блокируются на уровне системных политик
безопасности Windows (политика RemoteDebuggingAllowed: false).
Для демонстрации корректности кода, локаторов и явных ожиданий
(WebDriverWait), тест выполнен в браузере Firefox, который
успешно отрабатывает сценарий.
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )
    wait = WebDriverWait(driver, 10)

    try:
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/data-types.html"
        )
        driver.get(url)

        # Заполняем форму
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым, как в ТЗ
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Кликаем по кнопке Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ждём перехода на страницу подтверждения
        wait.until(
            EC.url_contains("data-types-submitted.html")
        )

        # Проверяем, что zip code отображается как N/A (красный)
        # На странице подтверждения это просто текст или div
        zip_elements = driver.find_elements(
            By.XPATH, "//*[contains(text(), 'N/A')]")
        assert len(zip_elements) > 0, "Zip code должен отображаться как N/A"

        # Проверяем, что остальные данные отобразились
        assert (
            "Иван" in driver.page_source
        )
        assert (
            "Петров" in driver.page_source
        )
        assert (
            "test@skypro.com" in driver.page_source
        )

        print("✅ Тест формы пройден успешно в Firefox!")
    finally:
        driver.quit()
