# #
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

# class Soldier:
#
# class Guns:
#     def __init__(self, gun = "AK-47"):
#         self.gun = gun
#
# class Act_of_Shooting:
#     def __init__(self, ):
#
#     def reload(self):
#





# # 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.
#
# bedroom = 4
# wardrobe = 2
# table = 1.5
#
# class House():
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#
#     def add_furniture(self, total_area):
#         global fur_area
#         furniture = input("Enter furniture (bedroom / wardrobe / table: ")
#         if furniture == "bedroom":
#             fur_area = 4
#         elif furniture == "wardrobe":
#             fur_area = 2
#         elif furniture == "table":
#             fur_area = 1.5
#         else:
#             print("Enter correct furniture")
#         free_area = total_area - fur_area
#
#         return f"House type: {self.house_type}, Total area: {self.area}, Free area: {free_area}, Furniture: {furniture}"
#
#
# my_house = House("private", 10)
# print(my_house.add_furniture(10))


# # 3 
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student:
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major
#
#     def __str__(self):
#         return f"<name: {self.name}, age: {self.age}, major: {self.major}"
#
#
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)


# # 4 
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567) 
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

# class MoneyFmt:
#     def __init__(self, money):
#         self.money = money
#
#     def update(self, new_amount):
#         self.money = new_amount
#         return new_amount
#
#     def __repr__(self):
#         return str(self.money)
#     def __str__(self):
#         form_cur = "${:,.2f}".format(self.money)
#         return str(form_cur)
# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(repr(cash))


# # 5  
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle



# # 6 
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название 
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# Данные отдать в csv

