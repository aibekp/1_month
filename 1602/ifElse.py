#Problem 2
print ("Problem 2")
a = int (input("Enter a = "))
b = int (input("Enter b = ")) 
c = int (input("Enter c = "))
if a > b and a > c:
	print (a)
if b > a and b > c:
	print(b)
else:
	print(c)

print ("")

#Problem 3

print ("Problem 3")
a3 = 17391 % 17
b3 = 546 % 17
c3 = 934 % 17

if a3 > b3 and a3 > c3:
	print(a3)
if b3 > a3 and b3 > c3:
	print(b3)
else:
	print(c3)

#Problem 4

print ("Problem 4")
x = 13 ** 2
y = 172
if x < 172:
	x = x ** 2
else:
	print("x is more than 172 with one ** 2")
print("x ** 2 what less than 172 and new x = ", x)

#Problem 5

print("Problem 5")

a5 = int (input("Enter number: "))
if a5 % 2 == 0:
	print ("Number is even")
else: 
	print ("Number is odd")
if a5 % 3 == 0:
	print ("Number is divided by 3 without remainder")
else: 
	print ("Number is not divided by 3 without remainder")
if a5 ** 2 > 1000:
	print(a5, " ** 2 is more than 1000")
else:
	print(a5, " ** 2 is less than 1000")

#Problem 6
print("")
print("Problem 6")
a6 = int(input("Enter your number: "))
if a6 > 0 and a6 < 21:
	print("Your number allowed")
if a6 > 57 and a6 < 100:
	print("You number allowed")
else:
	print("Your number is not allowed")

#Problem 7
print("")
print("Problem 7")
x7 = 1
if x == 1:
	print ("Hooray")
else:
	print ("neeehaaaa")

#Problem 8
print("")
print("Problem 8")
x = int(input("Enter your number: "))
if x > 0 and x < 100:
	if x > 25 and x < 50:
		if x > 30 and x < 40:
			print("30 < x < 40")
		print("25 < x < 50")
	print ("0 < x < 100")
else: 
	print("x is not between the range of 0 and 100")

#Problem 9
print("")
print("Problem 9")
a9 = 10//5
b9 = 10/5
print("10//5 == 10/5", sum9 = a9 + b9) if a == b else print("10//5 is not equal to 10/5")

#Problem 10
print("")
print("Problem 10")
a10 = int(input('Enter your number: '))
print(a10) if a10 < 0 else print ("you number is positive")

#Problem 11
print("")
print("Problem 11")
a11 = 10
b11 = 5
if a11 > 0 and b11 > 0:
	print("Numbers are positive")
else:
	print("Numbers are negative")

#Problem 12
print('')
print('Problem 12')

print("New a11 value is ", a11 + 2) if a > b else print("New b11 value is ", b11 +2)
