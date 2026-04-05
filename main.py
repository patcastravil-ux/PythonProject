def calculator():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    result = 0

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 + num2
        else:
            print("Ошибка! Деление на нуль!")
    else:
        print("Ошибка!")

    print(f"Результат: {result}")

calculator()