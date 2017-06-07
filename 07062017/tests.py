from main import por_extenso

assert por_extenso(0.05) == "cinco centavos"
assert por_extenso(0.25) == "vinte e cinco centavos"
assert por_extenso(0.32) == "trinta e dois centavos"
assert por_extenso(0.18) == "dezoito centavos"
assert por_extenso(0.89) == "oitenta e nove centavos"
assert por_extenso(1.00) == "um real"
assert por_extenso(2.00) == "dois reais"
assert por_extenso(0.01) == "um centavo"
assert por_extenso(1.50) == "um real e cinquenta centavos"
assert por_extenso(17.50) == "dezessete reais e cinquenta centavos"
assert por_extenso(99.99) == "noventa e nove reais e noventa e nove centavos"
