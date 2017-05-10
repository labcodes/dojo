from main import collatz, maior_caminho

assert collatz(1) == [1]
assert collatz(2) == [2, 1]
assert collatz(3) == [3, 10, 5, 16, 8, 4, 2, 1]
assert collatz(4) == [4, 2, 1]
assert collatz(5) == [5, 16, 8, 4, 2, 1]
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]

assert maior_caminho([1, 2, 3, 4, 5, 10]) == 3
assert maior_caminho([1, 2, 4, 5, 10]) == 10
