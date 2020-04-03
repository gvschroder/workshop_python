def bitwise_operators_vs_logical_operators():

    print('\nBitwise operators vs Logical operators\n=============================')
    x = 10
    if x is not None and x > 5:
        print('Logical: Não nulo e maior que 5')

    if (x is not None) & (x > 5):
        print('Bitwise: Não nulo e maior que 5')

    x = 1
    if (x is None) or ((x + 1) == 2):
        print('Logical: Nulo ou X + 1 == 2')

    if (x is None) | ((x + 1) == 2):
        print('Bitwise: Nulo ou X + 1 == 2')


def relational_operators():

    print('\nRelational operators\n=============================')
    print('Test 1', 10 > 3 < check(10, 'Test 1'))
    print('Test 2', 1 > 3 < check(10, 'Test 2'))
    print('Test 3', 1 == 1 < check(10, 'Test 3'))


def check(i, test):
    print(f'{test} Check')
    return i


def any_all():

    print('All -',
          all(check(value, f'All - Test {ix}') for ix, value in enumerate([True, True, True, False, True])))

    print('Any - ',
          any(check(value, f'Any - Test {ix}') for ix, value in enumerate([False, True, True, False, False])))


if __name__ == '__main__':
    # bitwise_operators_vs_logical_operators()
    # relational_operators()
    any_all()
