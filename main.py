students = {
    "Vitaly_Prikhodko": 203,
    "Dmytro_Kropyvnytskyi": 196,
    "Mikhail_Romanenko": 193,
    "Maxim_Derizemlya": 188,
    "Victoria_Zhuk": 182,
    "Andrey_Kuryanov": 177,
    "Oksana_Dubovets": 175,
    "Nikita_Stroganov": 173,
    "Karina_Nikolaenko": 169,
    "Eugenia_Dron": 167
}

def print_sorted_students(students):
    sorted_students = {k: v for k, v in sorted(students.items(), key=lambda item: item[1], reverse=True)}
    for surname, height in sorted_students.items():
        print(f" {surname}, Зріст: {height} см")

def add_student(students, surname, height):
    if surname in students:
        print(f"Учень з прізвищем {surname} вже існує.")
    else:
        students[surname] = height
        print(f"Учень {surname} з ростом {height} см доданий.")
        print("\nСписок учнів після додавання нового учня (відсортовано за зростом):")
        print_sorted_students(students)

def remove_student(students, surname):
    if surname in students:
        del students[surname]
        print(f"Учень {surname} видалений.")
        print("\nСписок учнів після видалення (відсортовано за зростом):")
        print_sorted_students(students)
    else:
        print(f"Учня з прізвищем {surname} не знайдено.")

def students_shorter_than_new(students_dict, new_height):
    shorter_students = [surname for surname, height in students_dict.items() if height < new_height]
    return shorter_students

def find_insert_position(students_dict, new_height):
    sorted_students = sorted(students_dict.items(), key=lambda x: x[1], reverse=True)
    for i, (surname, height) in enumerate(sorted_students):
        if height > new_height and sorted_students[i + 1][1] < new_height:
            return surname

def find_closest_height(students_dict, new_height):
    closest_surname = None
    min_difference = float('inf')
    for surname, height in students_dict.items():
        difference = abs(height - new_height)
        if difference < min_difference:
            min_difference = difference
            closest_surname = surname
    return closest_surname

def process_new_student(students_dict, new_surname, new_height):
    print(f"\nНовий учень: {new_surname}, зріст: {new_height} см\n")

    shorter_students = students_shorter_than_new(students_dict, new_height)
    print("Учні з меншим зростом:")
    print(shorter_students)

    insert_after = find_insert_position(students_dict, new_height)
    print(f"Новачка слід записати після учня з прізвищем: {insert_after}")

    closest_student = find_closest_height(students_dict, new_height)
    print(f"Учень, зріст якого найближче до новачка: {closest_student}")

def menu():
    print("\nМеню:")
    print("1. Вивести всіх учнів")
    print("2. Додати нового учня")
    print("3. Видалити учня")
    print("4. Вийти")

    choice = input("Виберіть дію (1/2/3/4): ")

    if choice == '1':
        print("\nСписок учнів (відсортовано за зростом):")
        print_sorted_students(students)
        menu()  

    elif choice == '2':
        surname = input("Введіть прізвище нового учня: ")
        try:
            height = int(input("Введіть зріст нового учня (в см): "))
            process_new_student(students, surname, height)
            add_student(students, surname, height)
        except ValueError:
            print("Некоректне значення зросту. Спробуйте ще раз.")
        menu() 

    elif choice == '3':
        surname = input("Введіть прізвище учня для видалення: ")
        remove_student(students, surname)
        menu()  

    elif choice == '4':
        print("Вихід із програми.")
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
        menu()  

menu()