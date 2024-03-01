
# Задание 4:
# Дан список  целых чисел:
numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.
newNumbers = []
for i in range(len(numbers)):
	if numbers[i] < 0:
		numbers[i] = -1
		newNumbers.append(numbers[i])
	if numbers[i] > 0:
		numbers[i] = 1
		newNumbers.append(numbers[i])
	if numbers[i] == 0:
		newNumbers.append(numbers[i])

print(newNumbers)