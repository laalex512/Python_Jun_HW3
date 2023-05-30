import copy


list1 = []
list2 = [1, "hi", 5]

print(list2[-1])  # 5

a = 40
b = "Hello"
c = [8, 3, 1]

# list2.extend(a)  - error
list2.extend(b)
list2.extend(c)
print(list2)  # [1, 'hi', 5, 'H', 'e', 'l', 'l', 'o', 8, 3, 1]

print(list2.count(1))  # 2 раза

start = 2
stop = 70
print(list2.index(5, start, stop))  # 2 индекс

list2.insert(-2, 4)
print(list2)  # [1, 'hi', 5, 'H', 'e', 'l', 'l', 'o', 8, 4, 3, 1]

print("--------------------------------------------")

list3 = [3, 5, 8, 1, 2, 0, 6]
list3_sort = sorted(list3, reverse=True)
print(list3_sort)  # [8, 6, 5, 3, 2, 1, 0], list3 не поменялся
list3.sort(reverse=True)
print(list3)  # [8, 6, 5, 3, 2, 1, 0], list3 поменялся

list3_rev = reversed(list3)
print(list(list3_rev))  # [0, 1, 2, 3, 5, 6, 8], list3 не поменялся
list3.reverse()
print(list3)  # [0, 1, 2, 3, 5, 6, 8], list3 поменялся
list3 = list3[::-1]
print(list3)  # [8, 6, 5, 3, 2, 1, 0]

print("--------------------------------------------")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = matrix.copy()
new_matrix[0][1] = 555
# тоже поменялась, тк поверхностное копирование:
print(matrix)
new_matrix2 = copy.deepcopy(matrix)
new_matrix2[0][0] = 444
print(matrix)  # не поменялась

print("--------------------------------------------")

tuple1 = (2, 3, 4)
print(f"{tuple1 = }")
