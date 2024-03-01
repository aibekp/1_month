file = open('database.txt', 'r')

words = []
words = file.read()
pairs = words.split("\n")
print(pairs)
for i in range(len(pairs)):
	print(pairs[i])


file.close()
# username = input("Enter your username: ")
