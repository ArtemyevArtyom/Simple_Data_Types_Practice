# Задание 1
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

lst = [1, 1.3, 'abs', True, None, b'12']
for el in lst:
    print(type(el))

for i in range(len(lst[:3])):
    print(type(lst[i]))