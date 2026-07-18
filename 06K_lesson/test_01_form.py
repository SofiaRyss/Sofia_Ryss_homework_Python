from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install())
    )

    try:
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/data-types.html"
        )
        driver.get(url)

        # Меняем By.ID на By.NAME!
        driver.find_element(By.NAME, "firstName").send_keys("Иван")
        driver.find_element(By.NAME, "lastName").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "jobPosition").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        # Проверяем zip code (он тоже по name)
        zip_el = driver.find_element(By.NAME, "zipCode")
        zip_style = zip_el.get_attribute("style").lower()
        zip_class = zip_el.get_attribute("class").lower()
        assert (
            "red" in zip_style or "invalid" in zip_class
        ), "Zip code должен быть красным!"

        # Проверяем firstName
        fn_el = driver.find_element(By.NAME, "firstName")
        fn_style = fn_el.get_attribute("style").lower()
        fn_class = fn_el.get_attribute("class").lower()
        assert (
            "green" in fn_style or "valid" in fn_class
        ), "First name должен быть зеленым!"

        print("✅ Тест формы пройден!")

    finally:
        driver.quit()
