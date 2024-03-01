# Задание 5:
    # Создайте input и спросите у пользоваетля как работает встроенная функция reversed().
    # В терминале пользователя должен ввести пример функции reversed() и отправить это вашей программе.
    # Ваша программа должна исполнить ту часть кода которую ввёл пользователь и вывести на экран результат.
    # Если пользователь ввёл что-то не по синтаксису Python поймайте это с помощью try: except:
    # Если пользователь всё ввёл верно выполните его программу.
    # Если поймали ошибку ---> Спросите снова как работает встроенная функция reversed().

name = "Python"
text = input("Enter how you use reversed with a given 'name' variable: ")  #reversed(name)


while text != "reversed(name)":
    text = input("Enter how you use reversed with a given 'name' variable: ")
try:
    print(list(reversed(name)))
except:
        text = input("Enter how you use reversed with a given 'name' variable: ")   