with open("python.txt", 'w') as file: 
	file.write("Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.")


with open("python.txt", 'r') as file:
	my_list = file.read()

t_words = []
words = my_list.split(" ")
for i in range(len(words)):
	for m in range(len(words[i])):
		if 't' == words[i][m]  or 'T' == words[i][m]:
			t_words.append(words[i])
print(t_words)