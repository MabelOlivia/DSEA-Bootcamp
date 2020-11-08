from sympy import *

# we create a symbol called "x"
x = Symbol("x")

f = 2*x**2 + 3
f_prime = f.diff(x)

print("When we differentiate", {f}, "we get = ", {f_prime})

