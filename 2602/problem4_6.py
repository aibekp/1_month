# Задание 6:
#     Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию? 
#     Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.

flag = True
number = input("Vvedite chislo: ")
for i in range(len(number) - 1):
	if int(number[i]) > int(number[i + 1]):
		flag = True
	else:
		flag = False
if flag == True:
	print("Yes")
else: 
	print("No")

