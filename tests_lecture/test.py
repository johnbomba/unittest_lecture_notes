from app.number import Number

n = Number(10)
assert n.value == 10, "value should be set by initializer"

r = Number.random()
assert 0 <= r.value < 100, "value should be within boundaries"