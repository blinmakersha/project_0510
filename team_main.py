from aditional_func import calculate


def calculate_two(eq: str):
    one, character, two = eq.split()
    return calculate(one, character, two)

print('Добро пожаловать в супер-мега калькулятор!!!\n\
    Введите математическое выражение по типу: 2 * 4')
operation = input('Введите выражение: ')
print('Ваш ответ: {0}'.format(calculate_two(operation)))
print('Историю операций можете посмотреть в файле "calculator.txt"')

