import csv
from faker import Faker
import random
import os

# Ініціалізація Faker з українською локалізацією
fake = Faker('uk_UA')

# Словники з чоловічими і жіночими по батькові
male_patronymics = ["Олексійович", "Іванович", "Сергійович", "Миколайович", "Андрійович",
                    "Юрійович", "Васильович", "Олександрович", "Петрович", "Володимирович",
                    "Григорович", "Романович", "Степанович", "Дмитрович", "Богданович",
                    "Євгенович", "Максимович", "Павлович", "Арсенійович", "Тимофійович"]
female_patronymics = ["Олексіївна", "Іванівна", "Сергіївна", "Миколаївна", "Андріївна",
                      "Юріївна", "Василівна", "Олександрівна", "Петрівна", "Володимирівна",
                      "Григорівна", "Романівна", "Степанівна", "Дмитрівна", "Богданівна",
                      "Євгенівна", "Максимівна", "Павлівна", "Арсеніївна", "Тимофіївна"]

# Ім'я CSV-файлу з абсолютним шляхом
filename = os.path.join(os.getcwd(), 'employees.csv')

# Функція для створення записів
def generate_employees_data():
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Прізвище', 'Ім\'я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

        # Генерація 2000 записів з 40% жінок і 60% чоловіків
        for _ in range(1200):  # Чоловіки
            last_name = fake.last_name_male()
            first_name = fake.first_name_male()
            patronymic = random.choice(male_patronymics)
            gender = 'Чоловік'
            birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
            position = fake.job()
            city = fake.city()
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()
            writer.writerow([last_name, first_name, patronymic, gender, birth_date, position, city, address, phone, email])

        for _ in range(800):  # Жінки
            last_name = fake.last_name_female()
            first_name = fake.first_name_female()
            patronymic = random.choice(female_patronymics)
            gender = 'Жінка'
            birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
            position = fake.job()
            city = fake.city()
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()
            writer.writerow([last_name, first_name, patronymic, gender, birth_date, position, city, address, phone, email])

    print(f"CSV файл успішно створено за шляхом: {filename}")

# Виклик функції для генерації даних
generate_employees_data()
