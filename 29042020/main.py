import unittest

def calcula_amigos_mais_proximos(amigo, lista_de_amigos):
    distancias = {}
    for migue in lista_de_amigos:
        distancia = ((amigo[1]-migue[1])**2 + ((amigo[0]-migue[0])**2))**(1/2)
        distancias[migue] = distancia
    print("distancias: {}".format(distancias))
    return distancias
    # return [
    #     amigo_proximo
    #     for amigo_proximo in lista_de_amigos
    #     if amigo_proximo != amigo
    # ]

# Função para calcular os amigos mais próximos
def mais_proximos(lista_de_amigos):
    resultado = {}
    for amigo in lista_de_amigos:
      amigos_mais_proximos = calcula_amigos_mais_proximos(amigo, lista_de_amigos)
      resultado[amigo] = amigos_mais_proximos

    return resultado

# Testes da função mais_proximos

class TesteAmigosMaisProximos(unittest.TestCase):

    def test_nenhum_amigo(self):
        assert mais_proximos([]) == {}

    def test_um_amigo(self):
        assert mais_proximos([(0, 0)]) == {(0, 0): []}

    def test_dois_amigos(self):
        assert mais_proximos([(0, 0), (0, 1)]) == {
            (0, 0): [(0, 1)],
            (0, 1): [(0, 0)]
        }

    def test_quatro_amigos(self):
        assert mais_proximos([(0, 0), (0, 1), (0, 2), (0, 3)]) == {
            (0, 0): [(0, 1), (0, 2), (0, 3)],
            (0, 1): [(0, 0), (0, 2), (0, 3)],
            (0, 2): [(0, 0), (0, 1), (0, 3)],
            (0, 3): [(0, 0), (0, 1), (0, 2)],
        }

    def test_cinco_amigos(self):
        assert mais_proximos([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]) == {
            (0, 0): [(0, 1), (0, 2), (0, 3)],
            (0, 1): [(0, 0), (0, 2), (0, 3)],
            (0, 2): [(0, 0), (0, 1), (0, 3)],
            (0, 3): [(0, 1), (0, 2), (0, 4)],
            (0, 4): [(0, 1), (0, 2), (0, 3)],
        }

if __name__ == '__main__':
    unittest.main()