def guess_number():
    min_num = 1
    max_num = 100

    while True:
        guessed_num = (min_num + max_num) // 2
        print("Загаданное число равно", guessed_num, "?")
        answer = input("Введите 'Больше', 'Меньше' или 'Верно': ")

        if answer.lower() == "больше":
            min_num = guessed_num + 1
        elif answer.lower() == "меньше":
            max_num = guessed_num - 1
        elif answer.lower() == "верно":
            print("Число угадано!")
            break
        else:
            print("Неверный ответ, попробуйте еще раз.")

guess_number()
