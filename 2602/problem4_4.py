# Задание 4:
    # Вам даны несколько последовательностей чисел:
sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

    # Нужно проверить, все ли числа в КАЖДОЙ последовательности уникальны.
    # Если в последовательности были найдены дубликаты ---> Выведите на экран: "Последовательность не уникальна."
    # Если в последовательности дубликатов найдено не было ---> Выведите на экран: "Последовательность уникальна."
    # Если в решении задания не присутствует цикл ---> Задание не защитано.

flag_0 = True
for i in sequence_0:
    if sequence_0.count(i) > 1:
        flag_0 = False
        break
if(flag_0):
    print("List 0 contains all unique elements")
else:
    print("List 0 doesn't contain all unique elements")

flag_1 = True
for i in sequence_1:
    if sequence_1.count(i) > 1:
        flag_1 = False
        break
if(flag_1):
    print("List 1 contains all unique elements")
else:
    print("List 1 doesn't contain all unique elements")

flag_2 = True
for i in sequence_2:
    if sequence_2.count(i) > 1:
        flag_2 = False
        break
if(flag_2):
    print("List 2 contains all unique elements")
else:
    print("List 2 doesn't contain all unique elements")

flag_3 = True
for i in sequence_3:
    if sequence_3.count(i) > 1:
        flag_3 = False
        break
if(flag_3):
    print("List 3 contains all unique elements")
else:
    print("List 3 doesn't contain all unique elements")