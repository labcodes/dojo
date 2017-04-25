cedulas = [100, 50, 10, 5, 1]
moedas = [0.50, 0.10, 0.05, 0.01]

def troco(valor_da_compra, valor_pago):
	if valor_da_compra == valor_pago:
		return []

	troco = valor_pago - valor_da_compra

	if troco % 100 == 0:
		tupla_de_100, resto = notas_de_100(troco)
		return [tupla_de_100]
	elif troco % 50 == 0:
		n50_cedulas = troco / 50
		if (n50_cedulas > 1):
			tupla_de_100, resto = notas_de_100(troco)
			return [tupla_de_100, (50, 1)]
		return [(50, 1)]
	return [(10, 4)]

def notas_de_100(troco):
	mod = troco % 100
	inteiro = (troco - mod) / 100
	return (100, inteiro), mod