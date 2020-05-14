import math
import numpy as np


def f(x):  # Function of x
    x = float(x)
    y = (math.e ** x) / x
    return y


def fillaray(n):  # this function will make an array of x+ih
    xi = float(a)
    for i in range(0, n - 1):
        xi = xi + h
        barry.append(xi)


def multi():  # this function will multiply the odd elemnts in barry with 4 and even with 2
    for i in range(0, len(barry)):
        barry[i] = f(barry[i])
    for i in range(len(barry)):
        if i % 2 == 0:
            # print("odd",barry[i])
            barry[i] = float(barry[i]) * 4
        if i % 2 != 0:
            # print("even",barry[i])
            barry[i] = barry[i] * 2
    # print(barry)


def final():  # this function will complete(add then divide by h/3) the formula
    sumarray = float(0)
    for i in range(0, len(barry)):
        sumarray = barry[i] + sumarray

    # print(h/3,"[ ",functionx(a),"+",barry,"+",functionx(b)," ]")
    simpson = sumarray + f(a) + f(b)
    simpson = (h / 3) * simpson
    return simpson


a = 1  # lower bound of integration
b = 2  # upper bound of integration
n = 1000  # number of subintervals [Must be even]
simpson = float(0)
barry = []
h = (float(b) - float(a)) / float(n)
fillaray(n)
multi()
exact = final()
print("The Exact value is", exact)

for i in range(10, 110, 10):  # n is considered i
    a = 1
    b = 2
    barry = []  # array which will hold values of Xi
    h = (float(b) - float(a)) / float(i)
    fillaray(i)
    multi()
    simpson = final()
    print(i, "|Approximation:", simpson, "|Error:", np.abs(exact - simpson))
'''
n = 200
barry = []
h = (float(b) - float(a)) / float(n)
print("a =", a, ",b =", b, ",h =", h)
fillaray()
print(barry)
loop()
simp = final()
#print(barry)
#print("a =", a, ",b =", b, ",h =", h)
print(n, "-approximation: ", simp,"--",)
'''
