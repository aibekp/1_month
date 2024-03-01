# Задание 3:
# Вам дан список:
numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# Определите количество четных и не четных.

chet = 0
neChet = 0
 
for i in range(len(numbers)):
	if numbers[i] % 2 == 0:
		chet += 1
	else: 
		neChet +=1
print("Chetnoe: ", chet)
print("Nechetnoe: ", neChet)