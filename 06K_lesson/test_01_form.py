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

        driver.find_element(By.ID, "firstName").send_keys("Иван")
        driver.find_element(By.ID, "lastName").send_keys("Петров")
        driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.ID, "email").send_keys("test@skypro.com")
        driver.find_element(By.ID, "phone").send_keys("+7985899998787")
        driver.find_element(By.ID, "city").send_keys("Москва")
        driver.find_element(By.ID, "country").send_keys("Россия")
        driver.find_element(By.ID, "jobPosition").send_keys("QA")
        driver.find_element(By.ID, "company").send_keys("SkyPro")

        driver.find_element(By.ID, "submit").click()

        zip_el = driver.find_element(By.ID, "zipCode")
        zip_style = zip_el.get_attribute("style").lower()
        zip_class = zip_el.get_attribute("class").lower()
        assert (
            "red" in zip_style or "invalid" in zip_class
        ), "Zip code должен быть красным!"

        fn_el = driver.find_element(By.ID, "firstName")
        fn_style = fn_el.get_attribute("style").lower()
        fn_class = fn_el.get_attribute("class").lower()
        assert (
            "green" in fn_style or "valid" in fn_class
        ), "First name должен быть зеленым!"

        print("✅ Тест формы пройден!")

    finally:
        driver.quit()
