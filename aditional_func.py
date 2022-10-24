def calculate(first, sym, snd):
    """
    Calculates given operation and creates file with this operation.

    Args:
        first : str - first number of the operation.
        sym : str - arithmetic operator.
        snd : str - second number of the operation.
    """
    file = open('calculator.txt', 'a')
    try:
        first, snd = int(first), int(snd)
    except ValueError:
        print("Формат ввода: VALUE1 <+-*/> VALUE2\n\
            Пример: 1 * 2")
    else:
        if sym == '+':
            file.write('{0} + {1} = {2}\n'.format(first, snd, first + snd))
            return first + snd
        elif sym == '-':
            file.write('{0} - {1} = {2}\n'.format(first, snd, first - snd))
            return first - snd
        elif sym == '*':
            file.write('{0} * {1} = {2}\n'.format(first, snd, first * snd))
            return first * snd
        elif sym == '/':
            if snd == 0:
                print("It's not okay")
            else:
                file.write('{0} / {1} = {2}\n'.format(first, snd, first / snd))
                file.close()
                return first / snd
