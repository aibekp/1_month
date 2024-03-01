with open("users.txt", 'r') as file: 
	my_list = "".join(file)
	if "w" in my_list:
		print("Да, в тексте есть w")
	else: 
		print("Нет, в тексте нет w")
