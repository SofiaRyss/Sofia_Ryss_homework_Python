from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Находим поле ввода с названием custname
    name_field = driver.find_element(By.NAME, "custname")

    # Вводим имя
    name_field.send_keys("София")

    # Находим кнопку Submit и нажимаем
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Проверяем, что URL изменился
    assert driver.current_url != "https://httpbin.org/forms/post"

    driver.quit()
