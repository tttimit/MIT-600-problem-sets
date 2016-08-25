x = 0.0
numIters = 100000
for i in range(numIters):
    x += 0.1
print(x)
print(repr(x))
print(10.0 * x == numIters)
