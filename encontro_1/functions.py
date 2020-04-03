

def simple_function():
    print(simple_function.__name__)


def function_args(nome, idade, sobrenome):
    print(f'Nome Completo: {nome} {sobrenome}, Idade: {idade}')


def function_args_default(nome='', idade=0, sobrenome=''):
    print(f'Nome Completo: {nome} {sobrenome}, Idade: {idade}')

"""
Armadilha dos argumentos com valor default
Nome:  Schroder
Idade: 1
Contatos: {'1_tel': '15 981145866', '1_email': 'gvschroder@gmail.com'}
Metas: ['Fazer uma viagem para Alemanha', 'Conhecer a Nasa', 'Comprar uma cadeita Gamer']
Nome:  Schroder
Idade: 1
Contatos: {'1_tel': '15 981145866', '1_email': 'gvschroder@gmail.com', '2_email': 'gvschroder@gmail.com'}
Metas: ['Fazer uma viagem para Alemanha', 'Conhecer a Nasa', 'Comprar uma cadeita Gamer', 'Conhecer a Nasa', 'Comprar uma cadeita Gamer']
"""
def function_args_default_trap(
        nome='',
        idade=0,
        contantos={'1_tel': '15 981145866'},
        metas=['Fazer uma viagem para Alemanha']
):

    nome += ' Schroder'
    idade += 1
    contantos.update({f'{len(contantos.keys())}_email': 'gvschroder@gmail.com'})
    metas += ['Conhecer a Nasa']
    metas.append('Comprar uma cadeita Gamer')

    print(f'Nome: {nome}\n'
          f'Idade: {idade}\n'
          f'Contatos: {contantos}\n'
          f'Metas: {metas}')


def function_args_default_trap_fix(
        nome='',
        idade=0,
        contantos=None,
        metas=None
):

    if contantos is None:
        contantos = {'1_tel': '15 981145866'}

    if metas is None:
        metas = ['Fazer uma viagem para Alemanha']

    nome += ' Schroder'
    idade += 1
    contantos.update({f'{len(contantos.keys())}_email': 'gvschroder@gmail.com'})
    metas += ['Conhecer a Nasa']
    metas.append('Comprar uma cadeita Gamer')

    print(f'Nome: {nome}\n'
          f'Idade: {idade}\n'
          f'Contatos: {contantos}\n'
          f'Metas: {metas}')


if __name__ == '__main__':
    print('\nFunção simples')
    simple_function()

    print('\nArgumentos posicionais')
    function_args('Itararé', 'Sensei', 28)

    print('\nArgumentos nomeados')
    function_args(idade=28, nome='Guilherme', sobrenome='Schröder')

    print('\nArgumentos posicionais e nomeados')
    function_args('Guilherme', sobrenome='Schröder', idade=28)

    print('\nArgumentos por lista/tupla')
    t_args = ('Itararé', 'Sensei', 28)
    function_args(*t_args)

    print('\nArgumentos por dicionario')
    d_args = {'idade': 28, 'nome': 'Guilherme', 'sobrenome': 'Schröder'}
    function_args(*d_args)
    function_args(**d_args)

    print('\nArgumentos por lista/tupla e dicionario')
    l_args = ['Guilherme']
    d_kwargs = {'idade': 28, 'sobrenome': 'Schröder'}
    function_args(*l_args, **d_kwargs)

    print('\nArgumentos com valor default')
    function_args_default('Guilherme', sobrenome='Schröder')

    print('\nArmadilha dos argumentos com valor default')
    function_args_default_trap()
    function_args_default_trap(contantos={}, metas=[])

    print('\nSolução: Armadilha dos argumentos com valor default')
    function_args_default_trap_fix()
    function_args_default_trap_fix()
