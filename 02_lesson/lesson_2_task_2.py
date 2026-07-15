# Объявляем функцию is_year_leap, которая принимает один аргумент — год
def is_year_leap(year):
    # Проверяем, делится ли год на 4 без остатка
    if year % 4 == 0:
        return True
    else:
        return False


# Вызываем функцию и сохраняем результат в переменную
result = is_year_leap(2024)

# Выводим результат в нужном формате
print(f"год 2024: {result}")

# Проверяем ещё один год
result2 = is_year_leap(2023)
print(f"год 2023: {result2}")
