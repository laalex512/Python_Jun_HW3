# Вручную создайте список с целыми числами, которые повторяются.
#  Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков

def task1():
    input_list = [3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 5, 8, 1]
    result = []
    for i in input_list:
        if i not in result:
            result.append(i)
    print(result)


# task1()

# ---------------------------------------------------------------------

# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях


def task2():
    input_data = input("Enter data: ")
    if input_data.isdigit():
        result = int(input_data)
    elif (input_data.count(".") == 1 or (input_data.count("-") == 1 and input_data.startswith("-"))) and \
            (input_data.replace("-", "").replace(".", "").isdigit()):
        result = float(input_data)
    elif not input_data.islower():
        result = input_data.lower()
    else:
        result = input_data.upper()
    print(f"{result}")


# task2()

# ---------------------------------------------------------------------

# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где
# ключ - тип элемента,
# значение - список элементов данного типа

def task3():
    input_tuple = (3, 5, "asd", True, 5.45, False, "jlh",
                   8.4, (5, 1, 5), [4, "dsg", True])
    result_dict = {}
    for i in input_tuple:
        if type(i) not in result_dict:
            result_dict[type(i)] = []
        result_dict[type(i)].append(i)

    print(result_dict)


# task3()

# ---------------------------------------------------------------------

# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.


def task4():
    input_list = [2, 3, 4, 6, 8, 2, 2, 3]
    for i in set(input_list):
        if input_list.count(i) > 1:
            while i in input_list:
                input_list.remove(i)
    print(input_list)


# task4()

# ---------------------------------------------------------------------

# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы


def task5():
    input_list = [2, 3, 4, 5, 6, 2, 3, 4, 2]
    result = []
    for index, item in enumerate(input_list):
        if item % 2:
            result.append(index)
    print(result)


# task5()

# ---------------------------------------------------------------------

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки

def task6():
    input_data = input("Enter your data: ")
    words_list = input_data.split()
    max_length = len(words_list[0])
    for i in words_list:
        if len(i) > max_length:
            max_length = len(i)

    words_list.sort()
    for num_line, line in enumerate(words_list, start=1):
        print(f"{num_line} {line:>{max_length}}")


# task6()

# ---------------------------------------------------------------------

# Homework

# ---------------------------------------------------------------------

# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def home_task1():
    input_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9]
    # Первый вариант (довольно затратный)
    result_list1 = []
    for i in input_list:
        if input_list.count(i) > 1 and i not in result_list1:
            result_list1.append(i)

    # Второй вариант (по идее, тоже затратный)
    result_list2 = []
    for i in input_list:
        if input_list.count(i) > 1:
            result_list2.append(i)
    result_list2 = list(set(result_list2))

    # Третий вариант (экономичнее ничего не придумал))
    counts_dict = {}
    for i in input_list:
        counts_dict.setdefault(i, 0)
        counts_dict[i] += 1
    result_list3 = []
    for key, value in counts_dict.items():
        if value > 1:
            result_list3.append(key)

    print(result_list1, result_list2, result_list3, sep="\n")


# home_task1()


# ---------------------------------------------------------------------

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def home_task2():
    import re

    COUNT_COMMON = 10

    pattern = r"[.,;:!?\(\)\-\\n]"
    input_data = input("Paste data: ")  # Для удобства рядом лежит файл input.txt, можно скопипастить

    words_list = input_data.split()
    common_dict = {}
    for i in words_list:
        i = re.sub(pattern, "", i).lower()  # Убираем знаки препинания и переводим в нижний регистр
        if i.isalpha():
            common_dict.setdefault(i, 0)
            common_dict[i] += 1
    result_dict = {}
    for _ in range(COUNT_COMMON):
        max_common = 0
        key_max = ""
        for key, value in common_dict.items():
            if value > max_common:
                max_common = value
                key_max = key
        result_dict[key_max] = common_dict.pop(key_max)
    print(result_dict, )


# home_task2()

# ---------------------------------------------------------------------

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


def home_task3(bag_size: int):
    things = {
        "first aid kit": 15,
        "bottle": 20,
        "mug": 10,
        "flashlight": 5,
        "sleeping bag": 80,
        "tent": 120,
        "mat": 40,
        "dishes": 30,
        "food": 50
        }
    things = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))
    result_things = {}
    sum_weight = 0
    for thing, weight in things.items():
        if sum_weight + weight <= bag_size:
            sum_weight += weight
            result_things[thing] = weight

    print(f"Вещи в рюкзаке: {result_things}, Общий вес: {sum_weight}")

# home_task3(300)
