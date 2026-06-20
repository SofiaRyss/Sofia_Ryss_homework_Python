from address import Address
from mailing import Mailing

# Создаём два адреса
to_address = Address("101000", "Москва", "ул. Ленина", "10", "5")
from_address = Address("190000", "Санкт-Петербург",
                       "Невский проспект", "25", "12")

# Создаём почтовое отправление
my_mailing = Mailing(to_address, from_address, 350, "RU123456789")

# Выводим информацию в нужном формате
print(
    f"Отправление {my_mailing.track} "
    f"из {my_mailing.from_address.index}, "
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)
