def arithmetic_operators():
    """
    Arithmetic operators:
    =====================

    OPERATOR   DESCRIPTION              SYNTAX
    +          Addition                 x + y
    -          Subtraction              x - y
    *          Multiplication           x * y
    /          Division                 x / y
    %          Modulus                  x % y
    //         Floor division	        x // y
    **         Exponentiation           x ** y
    """

    x = 9
    y = 2

    print('\nArithmetic Operators\n============================')
    print('(x + y)', f'{x} + {y} = {x+y}')
    print('(x - y)', f'{x} - {y} = {x-y}')
    print('(x * y)', f'{x} * {y} = {x*y}')
    print('(x / y)', f'{x} / {y} = {x/y}')
    print('(x % y)', f'{x} % {y} = {x%y}')
    print('(x // y)', f'{x} // {y} = {x//y}')
    print('(x ** y)', f'{x} ** {y} = {x**y}')


def relational_operators():
    """
    Relational Operators
    ============================
    OPERATOR   DESCRIPTION                                                         SYNTAX
    >          Greater than: True if left operand is greater than the right        x > y
    <          Less than: True if left operand is less than the right              x < y
    ==         Equal to: True if both operands are equal	                       x == y
    !=         Not equal to - True if operands are not equal	                   x != y
    >=         Greater than or equal to: True if left operand is greater than      x >= y
               or equal to the right
    <=         Less than or equal to: True if left operand is less than or equal   x <= y
               to the right
    """
    x = 1
    y = 3

    print('\nRelational operators\n============================')
    print('(>)', f'{x} > {y} = {x>y}')
    print('(<)', f'{x} < {y} = {x<y}')
    print('(==)', f'{x} == {y} = {x==y}')
    print('(!=)', f'{x} != {y} = {x!=y}')
    print('(>=)', f'{x} >= {y} = {x>=y}')
    print('(<=)', f'{x} <= {y} = {x<=y}')


def logical_operators():
    """
    Logical operators
    =====================
    OPERATOR   DESCRIPTION                                                         SYNTAX
    and        Logical AND: True if both the operands are true                     x and y
    or         Logical OR: True if either of the operands is true                  x or y
    not        Logical NOT: True if operand is false                               not x
    """
    x = True
    y = False

    print('\nLogical operators\n============================')
    print('and', x and y)
    print('or', x or y)
    print('not', not x)


def bitwise_operators():
    """
    Bitwise operators
    =================
    OPERATOR   DESCRIPTION                                                         SYNTAX
    &          Bitwise AND                                                         x & y
    |          Bitwise OR                                                          x | y
    ~          Bitwise NOT                                                         ~x
    ^          Bitwise XOR                                                         x ^ y
    >>         Bitwise right shift                                                 x>>
    <<         Bitwise left shift                                                  x<<
    """

    x = 100
    y = 20

    print('\nBitwise operators\n============================')
    print('\nBitwise AND')
    print('{0:08b}'.format(x), f'x={x}')
    print('{0:08b}'.format(y), f'y={y}')
    print('{0:08b}'.format(x & y), f'x&y={x&y}')

    print('\nBitwise OR')
    print('{0:08b}'.format(x), f'x={x}')
    print('{0:08b}'.format(y), f'y={y}')
    print('{0:08b}'.format(x | y), f'x|y={x|y}')

    print('\nBitwise NOT')
    x = 19
    print('{0:08b}'.format(x), f' x={x}')
    print('{0:08b}'.format(~x), f'~x={~x}')

    print('\nBitwise XOR')
    print('{0:08b}'.format(x), f'x={x}')
    print('{0:08b}'.format(y), f'y={y}')
    print('{0:08b}'.format(x ^ y), f'x^y={x^y}')

    x = 10
    y = 2

    print('\nBitwise Right Shift')
    print('{0:08b}'.format(x), f'x={x}', f'shift={y}')
    print('{0:08b}'.format(x >> y), f'x >> y={x >> y}')

    print('\nBitwise Left Shift')
    print('{0:08b}'.format(x), f'x={x}', f'shift={y}')
    print('{0:08b}'.format(x << y), f'x >> y={x << y}')


if __name__ == '__main__':
    arithmetic_operators()
    relational_operators()
    logical_operators()
    bitwise_operators()

    """
    Assignment operators
    =====================
    OPERATOR   DESCRIPTION                                                         SYNTAX
    =          Assign value of right side of expression to left side operand	   x = y + z
    +=         Add AND: Add right side operand with left side operand and          a += b, a = a+b
               then assign to left operand
    -=         Subtract AND: Subtract right operand from left operand and          a -= b, a = a-b
               then assign to left operand
    *=         Multiply AND: Multiply right operand with left operand and          a *= b, a = a*b
               then assign to left operand
    /=         Divide AND: Divide left operand with right operand and then         a /= b, a = a/b
               assign to left operand
    %=         Modulus AND: Takes modulus using left and right operands and        a %= b, a = a%b
               assign result to left operand
    //=        Divide(floor) AND: Divide left operand with right operand and       a //= b, a = a//b
               then assign the value(floor) to left operand
    **=        Exponent AND: Calculate exponent(raise power) value using           a **= b, a = a**b
               operands and assign value to left operand
    &=         Performs Bitwise AND on operands and assign value to left           a &= b, a = a&b
               operand
    |=         Performs Bitwise OR on operands and assign value to left            a |= b, a = a|b
               operand
    ^=         Performs Bitwise xOR on operands and assign value to left           a ^= b, a = a^b
               operand
    >>=        Performs Bitwise right shift on operands and assign value to left   a >>= b, a = a>>b
               operand
    <<=	       Performs Bitwise left shift on operands and assign value to left    a <<= b, a = a << b
               operand
    """




