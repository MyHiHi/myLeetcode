import itertools
S = "a1b3"


def f(x): return (x.lower(), x.upper()) if x.isalpha() else x


print(list(map(''.join, itertools.product(*map(f, S)))))
# p=itertools.product()
