def calculator():
    print("---Калькулятор запущен! Для выхода введите 'exit'")

    while True:
        user_input = input("Введите первое число: ")

        if user_input.lower() == 'exit':
            print("Сессия закончена")
            break

        try:
            num1 = float(user_input)
            operator = input("Введите оператор (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Ошибка! Деление на нуль!")
                    continue
            else:
                print("Ошибка!")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Вводи числа а не буквы!")

calculator()