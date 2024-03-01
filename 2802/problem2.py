with open("users.txt", 'w') as file:
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	file.write(username + " ")
	file.write(password + " ")

