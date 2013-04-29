"""
dice simulation

(C) Christian Kohlstedde

how to run:
python exercise1.dice.py
"""

# Defining a dice function
# returns the sum of the thrown dices
def dice(diceCount=1):
    import random
    sum = 0

    for i in range(diceCount):
        sum += random.randint(1, 6)
    return sum

# parameters
dices = 2
throws = 10000

# statistics dictionary
d = {}

# init the dictionary
for i in range(dices, dices * 6 + 1):
    d[i] = 0

# simulating the dice throws
for i in range(throws):
    d[dice(dices)] += 1

# printing out beautiful statistics
for sum in d:
    print sum, ": ", d[sum] / float(throws) * 100, "%"
