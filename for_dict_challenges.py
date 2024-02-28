# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print(f'Задание 1')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = dict()

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

for name, count in names.items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
print(f'\nЗадание 2')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = dict()

for student in students:
    if student['first_name'] not in names.keys():
        names[student['first_name']] = 1
    else:
        names[student['first_name']] += 1

max_name = max(names, key=names.get)

print(f'Caмое частое имя среди учеников: {max_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print(f'\nЗадание 3')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
names = dict()
i = 1

for student_list in school_students:
    for student in student_list:
        if student['first_name'] not in names.keys():
            names[student['first_name']] = 1
        else:
            names[student['first_name']] += 1
    max_name = max(names, key=names.get)
    print(f'Caмое частое имя среди учеников в классе {i}: {max_name}')
    i += 1
    names = dict()


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
print(f'\nЗадание 4')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

i = 0
girls = 0
boys = 0


for school_student in school:
    one_class = school[i]
    k = 0
    for j in school_student["students"]:
        class_names = one_class['students']
        class_first_name = class_names[k]
        student_name = class_first_name['first_name']
        if student_name in is_male.keys():
            x = is_male.get(student_name)
            if x is False:
                girls += 1
            else:
                boys += 1
        k += 1
    print(f'Класс {school[i]["class"]}: девочки {girls}, мальчики {boys}')
    boys = 0
    girls = 0
    i += 1


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print(f'\nЗадание 4')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

i = 0
girls = 0
boys = 0


for school_student in school:
    one_class = school[i]
    k = 0
    for j in school_student["students"]:
        class_names = one_class['students']
        class_first_name = class_names[k]
        student_name = class_first_name['first_name']
        if student_name in is_male.keys():
            x = is_male.get(student_name)
            if x is False:
                girls += 1
            else:
                boys += 1
        k += 1
    if boys > girls:
        print(f'Больше всего мальчиков в классе {school[i]["class"]}')
    else:
        print(f'Больше всего девочек в классе {school[i]["class"]}')
    boys = 0
    girls = 0
    i += 1
