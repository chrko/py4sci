"""
Compute primes up to 1000

(C) Christian Kohlstedde

how to run:
python exercise1.prime.py
"""

# printing the 2 all times
# just knowing her good enough
print 2

# running for loop over the range from 3 to 1000 excluding the even numbers by submitting 2 as the step
for prime in range(3,1000,2):

    # helper var
    isprime = True

    # running the test, starting a 3 to the testing number,
    # also excluding the evens
    for test in range(3, prime, 2):
        # test
        if (prime % test) == 0:
        isprime = False

    if isprime:
        print prime