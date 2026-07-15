from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    # Запускаем браузер Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # 1. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Находим и нажимаем на кнопку "Start"
        start_button = driver.find_element(By.CSS_SELECTOR, "#start")
        start_button.click()

        # 3. Дожидаемся появления текста "Hello World!"
        # Используем явное ожидание вместо time.sleep()
        wait = WebDriverWait(driver, 10)
        hello_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        # 4. Делаем скриншот страницы
        driver.save_screenshot("screenshot.png")

        # 5. Проверяем, что текст действительно равен "Hello World!"
        actual_text = hello_element.text
        assert actual_text == "Hello World!", (
            f"Ожидали 'Hello World!', а получили '{actual_text}'"
        )

    finally:
        # Закрываем браузер в конце теста (даже если произошла ошибка)
        driver.quit()
