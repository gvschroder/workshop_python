
def tipos():

    # Text Type
    texto = ''  # str()

    # Numeric Types
    inteiro = 1  # int('1')
    decimal = 1.0  # float('1'), float(1)

    # Sequence Types
    lista = []  # list()
    tupla = ()  # tuple()
    intervalo = range(1, 5, 1)

    # Mapping Type:
    dicionario = {"nome": "Guilherme"}  # dict()

    # Set Types
    conjunto = {'guilherme', 'itarare'}  # set()

    print(conjunto)
    print(set('12345'))
    print(set((1, 2, 3, 4, 5, 5)))
    print(set((1, 2, 3, 4, 5)))

    conjunto = {'guilherme'}
    conjunto.add('schroder')
    conjunto.add('schroder')
    print(conjunto)
    # print(conjunto[0])

    conjunto_imutavel = frozenset(['guilherme', 'itarare'])
    print(conjunto_imutavel)
    conjunto_imutavel_2 = conjunto_imutavel.union(['schroder'])
    print(conjunto_imutavel)
    print(conjunto_imutavel_2)

    # Slice Type
    fatia = slice(0, 2)
    print("01/01/2020"[fatia])
    print("01/01/2020"[0:2])

    # Boolean Type
    bool = True  # False

    # Binary Types

    # bytes
    print(b"Guilherme")
    print("Guilherme".encode())
    print(bytes('Guilherme', 'utf-8'))

    # bytearray 0 - 255
    x = bytearray(3)
    print(x)
    x[0] = 71  # G
    x[1] = 117  # u
    x[2] = 105  # i
    print(x)

    # memoryviewta
    # nome = "Guilherme"
    # x = memoryview(nome.encode())
    # x[0] = 103
    # print(x)

    x = memoryview(bytearray('Guilherme', 'utf-8'))
    print(bytes(x))
    print(id(x))
    x[0] = 103
    print(bytes(x))
    print(id(x))

    y = "Guilherme"
    print(y)
    print(id(y))
    y += " Schroder"
    print(y)
    print(id(y))


if __name__ == '__main__':
    tipos()
