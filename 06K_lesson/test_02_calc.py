from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    try:
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        driver.get(url)
        wait = WebDriverWait(driver, 60)

        delay = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")

        driver.find_element(By.XPATH, "//button[. = '7']").click()
        driver.find_element(By.XPATH, "//button[. = '+']").click()
        driver.find_element(By.XPATH, "//button[. = '8']").click()
        driver.find_element(By.XPATH, "//button[. = '=']").click()

        result_el = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "screen")
            )
        )

        result = result_el.text
        assert result == "15", (
            f"Ожидали 15, получили {result}"
        )

        print("✅ Тест калькулятора пройден!")

    finally:
        driver.quit()
