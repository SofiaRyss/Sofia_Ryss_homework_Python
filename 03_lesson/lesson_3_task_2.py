from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79002345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79003456789"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79004567890"))
catalog.append(Smartphone("Google", "Pixel 8", "+79005678901"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
