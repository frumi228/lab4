import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt


# Визначення вікових категорій
def get_age_category(age):
    if age < 25:
        return 'до 25'
    elif 25 <= age < 35:
        return '25-34'
    elif 35 <= age < 45:
        return '35-44'
    elif 45 <= age < 55:
        return '45-54'
    elif 55 <= age < 65:
        return '55-64'
    else:
        return '65+'


# Відкриття CSV-файлу
filename = 'employees.csv'
try:
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    print("Ok")
except FileNotFoundError:
    print("Файл не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка при відкритті файлу: {e}")
    exit(1)

# Рахуємо кількість чоловіків і жінок
gender_counts = defaultdict(int)
for row in data:
    gender_counts[row['Стать']] += 1

# Виведення кількості чоловіків і жінок у консоль
print("Кількість чоловіків:", gender_counts['Чоловік'])
print("Кількість жінок:", gender_counts['Жінка'])

# Побудова діаграми для статей
plt.figure(figsize=(6, 4))
plt.bar(gender_counts.keys(), gender_counts.values(), color=['blue', 'pink'])
plt.title("Кількість співробітників за статтю")
plt.xlabel("Стать")
plt.ylabel("Кількість")
plt.show()

# Рахуємо кількість співробітників у кожній віковій категорії
age_counts = defaultdict(int)
gender_age_counts = defaultdict(lambda: defaultdict(int))

for row in data:
    birth_date = datetime.strptime(row['Дата народження'], '%Y-%m-%d')
    age = (datetime.now() - birth_date).days // 365
    age_category = get_age_category(age)

    age_counts[age_category] += 1
    gender_age_counts[age_category][row['Стать']] += 1

# Виведення кількості співробітників у кожній віковій категорії
print("Кількість співробітників у кожній віковій категорії:")
for category, count in age_counts.items():
    print(f"{category}: {count}")

# Побудова діаграми для вікових категорій
plt.figure(figsize=(10, 6))
plt.bar(age_counts.keys(), age_counts.values(), color='green')
plt.title("Кількість співробітників за віковими категоріями")
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість")
plt.show()

# Виведення та побудова діаграм для статі у кожній віковій категорії
print("\nКількість співробітників кожної статі у кожній віковій категорії:")
for category, genders in gender_age_counts.items():
    print(f"\n{category}:")
    for gender, count in genders.items():
        print(f"  {gender}: {count}")

    # Побудова діаграми для кожної вікової категорії
    plt.figure(figsize=(6, 4))
    plt.bar(genders.keys(), genders.values(), color=['blue', 'pink'])
    plt.title(f"Кількість {category} за статтю")
    plt.xlabel("Стать")
    plt.ylabel("Кількість")
    plt.show()
