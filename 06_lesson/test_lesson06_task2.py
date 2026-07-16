from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_gitflic_cookies():
    # Запускаем браузер Chrome
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    try:
        # 1. Открываем главную страницу
        driver.get("https://gitflic.ru/")

        # ==========================================
        # ПОЛЬЗОВАТЕЛЬ 1
        # ==========================================
        # 2. Устанавливаем cookie пользователя 1
        driver.add_cookie({
            "name": "session",
            "value": "ZDRhOGY1ZjMtMWRmYS00NmUzLThhNzAtMTY4MThiMmIwYTBi",
            "domain": ".gitflic.ru"
        })

        # 3. Обновляем страницу
        driver.refresh()

        # 4. Переходим на страницу профиля пользователя 1
        driver.get("https://gitflic.ru/user/sofiaryss")

        # 5. Сохраняем текущий URL
        url_user1 = driver.current_url

        # ==========================================
        # ПОЛЬЗОВАТЕЛЬ 2
        # ==========================================
        # 6. Очищаем все куки
        driver.delete_all_cookies()

        # Снова открываем главную страницу
        driver.get("https://gitflic.ru/")

        # 7. Устанавливаем cookie пользователя 2
        driver.add_cookie({
            "name": "session",
            "value": "YWY5ZWNmNzYtNDdiNS00ZGY2LWE5MzAtOWM3MDdmZTBjMDBm",
            "domain": ".gitflic.ru"
        })

        # 8. Обновляем страницу
        driver.refresh()

        # 9. Переходим на страницу профиля пользователя 2
        driver.get("https://gitflic.ru/user/sofiarysakova")

        # 10. Сохраняем текущий URL
        url_user2 = driver.current_url

        # ==========================================
        # ПРОВЕРКА
        # ==========================================
        # 11. Проверяем, что URL разные
        assert url_user1 != url_user2, (
            f"URL должны быть разными! "
            f"User1: {url_user1}, User2: {url_user2}"
        )
        print("✅ Тест успешно пройден! Куки работают корректно.")

    finally:
        # Закрываем браузер
        driver.quit()
