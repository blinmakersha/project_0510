"""Calculates given operation and creates file with this operation."""


def calculate(first, sym, snd):
    """
    Calculates given operation and creates file with this operation.

    Args:
        first : str - first number of the operation.
        sym : str - arithmetic operator.
        snd : str - second number of the operation.
    """
    with open('calculator.txt', 'a') as newfile:
        try:
            first, snd = int(first), int(snd)
        except ValueError:
            print("Формат ввода: VALUE1 <+-*/> VALUE2\n\
                Пример: 1 * 2")
        else:
            if sym == '+':
                newfile.write('{0} + {1} = {2}\n'.format(first, snd, first + snd))
                return first + snd
            if sym == '-':
                newfile.write('{0} - {1} = {2}\n'.format(first, snd, first - snd))
                return first - snd
            if sym == '*':
                newfile.write('{0} * {1} = {2}\n'.format(first, snd, first * snd))
                return first * snd
            if sym == '/':
                if snd == 0:
                    print("It's not okay")
                else:
                    newfile.write('{0} / {1} = {2}\n'.format(first, snd, first / snd))
                    return first / snd
