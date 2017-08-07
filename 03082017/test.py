from main import n_erdos

entrada1 = [['P. Erdos', 'A. Selberg']]
entrada2 = [['P. Erdos', 'J. Silva']]
entrada3 = [['Z. Souza']]
entrada4 = [['P. Erdos', 'J. Silva', 'M. Mattar']]
entrada5 = [['J. Silva', 'M. Mattar']]
entrada6 = [['P. Erdos', 'A. Selberg'],
            ['P. Erdos', 'J. Silva', 'M. Mattar']]
entrada7 = [['P. Erdos', 'A. Selberg'],
            ['J. Silva', 'M. Mattar']]
entrada8 = [['P. Erdos', 'A. Selberg'],
            ['A. Selberg', 'M. Mattar']]


assert n_erdos(entrada1) == {'A. Selberg': 1}

assert n_erdos(entrada2) == {'J. Silva': 1}

assert n_erdos(entrada3) == {'Z. Souza': 'infinito'}

assert n_erdos(entrada4) == {
    'J. Silva': 1,
    'M. Mattar': 1
}

assert n_erdos(entrada5) == {
    'J. Silva': 'infinito',
    'M. Mattar': 'infinito'
}

assert n_erdos(entrada6) == {
    'A. Selberg': 1,
    'J. Silva': 1,
    'M. Mattar': 1
}

assert n_erdos(entrada7) == {
    'A. Selberg': 1,
    'J. Silva': 'infinito',
    'M. Mattar': 'infinito'
}

assert n_erdos(entrada8) == {
    'A. Selberg': 1,
    'M. Mattar': 2
}
