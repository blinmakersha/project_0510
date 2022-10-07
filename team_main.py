from aditional_func import calculate


def calculate_two(eq: str):
    one, character, two = eq.split()
    return calculate(one, character, two)


operation = input('Введите выражение: ')
print('Ваш ответ: {0}'.format(calculate_two(operation)))
print('Историю операций можете посмотреть в файле "calculator.txt"')
