"""
Класс Page Object для страницы калькулятора.
Сайт: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
Браузер: Google Chrome (по ТЗ)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница медленного калькулятора."""

    URL = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/slow-calculator.html"
    )

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр WebDriver (например, Chrome).
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> "CalculatorPage":
        """
        Открыть страницу калькулятора.

        :return: Экземпляр класса CalculatorPage для цепочки вызовов.
        :rtype: CalculatorPage
        """
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Установить задержку в поле #delay.

        :param seconds: Время задержки в секундах (целое число).
        :type seconds: int
        :return: Экземпляр класса CalculatorPage для цепочки вызовов.
        :rtype: CalculatorPage
        """
        delay_field = self.driver.find_element(
            By.CSS_SELECTOR, "#delay"
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, button_text: str) -> "CalculatorPage":
        """
        Нажать на кнопку калькулятора по её тексту (JS-клик для надежности).

        :param button_text: Текст на кнопке, которую нужно нажать.
        :type button_text: str
        :return: Экземпляр класса CalculatorPage для цепочки вызовов.
        :rtype: CalculatorPage
        """
        # 1. Ждем, пока кнопка появится на экране
        button = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        # 2. Делаем клик через JavaScript (он пробивает любые перекрытия!)
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def wait_for_result(self, expected_text: str) -> None:
        """
        Явно ждать появления ожидаемого результата на экране.

        :param expected_text: Ожидаемый текст результата.
        :type expected_text: str
        :return: None
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                expected_text
            )
        )

    def get_result(self) -> str:
        """
        Получить текст результата с экрана.

        :return: Текст, отображаемый на экране калькулятора.
        :rtype: str
        """
        screen = self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        )
        return screen.text
