# Doubler lambda
doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

print()


# Tripler lambda
tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

print()


# Multiplier function
def multiplier(x):
    return lambda n: n * x


# Create multiplier variables
quadrupler = multiplier(4)

quintupler = multiplier(5)

sextupler = multiplier(6)

septupler = multiplier(7)

octupler = multiplier(8)

nonupler = multiplier(9)

decupler = multiplier(10)


# Test multiplier variables
print(quadrupler(2))

print(quintupler(2))

print(sextupler(2))

print(septupler(2))

print(octupler(2))

print(nonupler(2))

print(decupler(2))