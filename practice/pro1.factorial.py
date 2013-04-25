"""
doing some factorial stuff

(c) Christian Kohlstedde
"""

def factorial_iter(num):
    num = int(num)
    if num == 0:
	return 1
    else:
	fac = 1
	for i in range(1, num + 1):
	    fac *= i
	return fac

print factorial_iter( 5 )
