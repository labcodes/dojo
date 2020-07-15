import unittest

def apertar_interruptor(lampada):
    if lampada == 'on':
        return 'off'
    if lampada == 'off':
        return 'on'

def caminhar_corredor(num_lampadas):
    corredor_de_lampadas = ['off' for _ in range(num_lampadas)]

    for caminhada in range(1, num_lampadas+1):
        corredor_de_lampadas = [
            lampada if (indice + 1) % caminhada else apertar_interruptor(lampada)
            for indice, lampada in enumerate(corredor_de_lampadas)
        ]

    return corredor_de_lampadas


class TesteJose(unittest.TestCase):

    def test_uma_lampada(self):
        self.assertEqual(caminhar_corredor(1), ['on'])

    def test_dois_lampadas(self):
        self.assertEqual(caminhar_corredor(2), ['on', 'off'])

    def test_tres_lampadas(self):
        self.assertEqual(caminhar_corredor(3), ['on', 'off', 'off'])

    def test_quatro_lampadas(self):
        self.assertEqual(caminhar_corredor(4), ['on', 'off', 'off', 'on'])

    def test_quebra_isso(self):
        resultado = caminhar_corredor(10000)


if __name__ == '__main__':
    # entrada numero de lampadas
    # saida vetor de estado de cada lampada [on, off]
    unittest.main()
