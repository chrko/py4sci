"""
Compute primes up to 1000

(C) @ Christian Kohlstedde
"""

print 2
for prime in range(3,1000):
    for test in range(3, prime, 2):
        if prime % test !== 0:
            print prime