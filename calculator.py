def calculate(a, b, operation):
    if operation == "+":
        return str(a + b)
    elif operation == "-":
        return str(a - b)
    elif operation == "*":
        return str(a * b)
    elif operation == "/":
        if b == 0:
            raise ValueError("Деление на ноль запрещено")
        return str(a // b)
    else:
        raise ValueError("Неподдерживаемая операция")


def main(input_str):
    try:
        tokens = input_str.split()
        if len(tokens) != 3:
            raise ValueError("Некорректный формат ввода")

        a = int(tokens[0])
        operation = tokens[1]
        b = int(tokens[2])

        if a < 1 or a > 10 or b < 1 or b > 10:
            raise ValueError("Числа должны быть от 1 до 10")

        result = calculate(a, b, operation)
        return result

    except ValueError as e:
        return str(e)


user_input = input("Введите арифметическое выражение: ")
output = main(user_input)
print("Результат:", output)