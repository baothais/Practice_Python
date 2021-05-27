# thislist = list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# for i in thislist: print(i)
# thisdict = dict(brand = "Ford", model = "Everest", price = "50,000$")
# l = list(map(lambda x: x[0], thisdict.items()))
# for i in l: print(i)
# syntax
"""lambda arguments : expression"""     # The expression is executed and the result is returned
# Example
x = lambda i: i*2
print(x(2))
y = lambda x, *y: x*y
print(y(2, 3, 4))                      # x=2, y=(3, 4) => x * y = 2 * (3, 4) = (3, 4, 3, 4)
thistuple = 2 * (2, 4)
print(thistuple)
z = lambda x, *y, **z: f"{x} + {y} + {z}"
print(z([1, 2], 3, 4, a=2, b=3, c=4))
# Advanced example
X = [1, 2, 3, 4]
X1 = (1, 2, 3)
X2 = {
    "model": "hello",
    "price": "3500"
}
def parabolic(x, a=1.0, b=0.0, c=0.0):
    return a * x * x + b * x + c
# Y = list(map(parabolic, X))
# for y in Y: print(y, end=' ')
print()
Y = lambda x, *y, **z: f"{x} + {y} + {z}"
print(Y(X, X1, X2))





