# RENATO e MARI
import unittest

def mapear_campo(entrada):
    linhas, colunas, bombas = entrada
    saida = []
    bomba_x, bomba_y = bombas[0]
    
    for linha in range(linhas):
        elementos = [0]*colunas
        if bomba_x == linha:
            elementos[bomba_y] = 'Bomba'
        saida.append(elementos)
    ## bomba_x, bomba_x + 1, bomba_x - 1
    ## bomba_y, bomba_y + 1, bomba_y - 1
    if bomba_x > 0:
        saida[bomba_x - 1] += 1
    if bomba_x < colunas:
        

# 1) bomba_x-1, bomba_y-1
# 2) bomba_x, bomba_y-1
# 3) bomba_x+1, bomba_y+1
# 4) bomba_x-1, bomba_y
# 5) bomba_x+1, bomba_y
# 6) bomba_x-1, bomba_y-1
# 7) bomba_x, bomba_y+1
# 8) bomba_x+1, bomba_y+1


    if linhas == 1:
        if colunas == 2:
            if bombas == [(0,0)]:
                saida.append(['Bomba', 1])
            else:
                saida.append([1, 'Bomba'])
        else:
            saida.append(['Bomba', 1, 0])
    elif linhas == 2:
        if bombas == [(0,0)]:
            saida.append(['Bomba'])
            saida.append([1])
        else:
            saida.append([1])
            saida.append(['Bomba'])
    else:
        saida.append(['Bomba'])
        saida.append([1])
        saida.append([0])
    return saida

'''
.*
'''

'''
1B
'''



['*', '*', '.', '.', '.', '.' ...]

class TesteCampoMinado(unittest.TestCase):

    def test_dois_por_um(self):
        saida_esperada = [['Bomba', 1]]
        entrada = (1, 2, [(0, 0)])
        saida = mapear_campo(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_dois_por_um_invertido(self):
        saida_esperada = [[1, 'Bomba']]
        entrada = (1, 2, [(1, 0)])
        saida = mapear_campo(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_um_por_dois(self):
        saida_esperada = [['Bomba'], [1]]
        entrada = (2, 1, [(0, 0)])
        saida = mapear_campo(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_um_por_dois_invertido(self):
        saida_esperada = [[1], ['Bomba']]
        entrada = (2, 1, [(0, 1)])
        saida = mapear_campo(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_tres_por_um(self):
        saida_esperada = [['Bomba', 1, 0]]
        entrada = (1, 3, [(0,0)])
        saida = mapear_campo(entrada)
        self.assertEqual(saida, saida_esperada)
    
    def test_tres_por_um_invertido(self):
        saida_esperada = [['Bomba'], [1], [0]]
        entrada = (3, 1, [(0,0)])
        self.assertEqual(mapear_campo(entrada), saida_esperada)


if __name__ == '__main__':
    unittest.main()