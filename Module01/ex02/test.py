from vector import Vector

print()
test = Vector(3)
print(test.values)
print(test.shape)
test = Vector((10, 15))
print(test.values)
print(test.shape)
test = Vector([0.0, 1.0, 2.0, 3.0])
print(test.values)
print(test.shape)
test = Vector([[0.0], [1.0], [2.0], [3.0]])
print(test.values)
print(test.shape)
test2 = Vector([[0.0], [1.0], [2.0], [3.0]])
print()

res = test + test2
print(res)
print(res.values)
print(res.shape)
print()

test = Vector([0.0, 1.0, 2.0, 3.0])
test2 = Vector([0.0, 1.0, 2.0, 3.0])

res = test + test2
print(res)
print(res.values)
print(res.shape)
print()
