"""
doing some factorial stuff

(c) Christian Kohlstedde
"""
import math

def unit_test_num(value1, value2):
    test = value1 == value2
    if test:
        text = "check!"
    else:
        text = "something has gone wrong :o"
    print value1, "=", value2, "=> " + text

def factorial_iter(num):
    num = int(num)
    if num == 0:
        return 1
    else:
        fac = 1
    for i in range(1, num + 1):
        fac *= i
    return fac

def factorial_rec(num):
    num = int(num)
    if num > 1:
        return num * factorial_rec(num - 1)
    else:
        return 1

print "iterative"
unit_test_num(factorial_iter(5), math.factorial(5))

print "recursive"
unit_test_num(factorial_rec(5), math.factorial(5))
