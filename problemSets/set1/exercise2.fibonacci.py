"""
exercise 2
the fibonacci numbers

(C) Christian Kohlstedde

how to run:
python exercise2.fibonacci.py
"""

# initial fibonacci list
fib = [0, 1]

# running the while loop until the sum of the last two entries are over 100000
while (fib[-1] + fib[-2]) < 100000:
    # append the sum of the last two entries
    fib.append(fib[-1] + fib[-2])

# printing out the list
print fib

# iterating over the fibonacci list to find squares
for num in fib:
    # added the 0.5 to ceil
    for sqrt in range(0, int(num / 2.0 + 0.5) + 1):
        # getting the square and checking with fibonacci number
        sqrtTest = sqrt * sqrt
        if sqrtTest == num:
            print num
            break
