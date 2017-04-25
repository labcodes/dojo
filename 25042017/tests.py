from main import troco



assert troco(10, 10) == []
assert troco(10, 50) == [(10, 4)]
assert troco(100, 300) == [(100, 2)]
assert troco(100, 400) == [(100, 3)]
assert troco(50, 100) == [(50, 1)]
assert troco(50, 200) == [(100, 1), (50, 1)]
# assert troco(5.25, 10) == [
	# (1, 4), (0.50, 1), (0.10, 2), (0.05, 1)]