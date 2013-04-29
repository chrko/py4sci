"""
normalized gaussian distribution for position x and parameters mu and sigma

(c) Christian Kohlstedde

run by python exercise2.gaussian.py
"""

def gaussian(x, mu, sigma):
    import math

    temp1 = math.exp(-math.pow(x-mu, 2)/(2 * sigma**2))
    temp2 = sigma * math.sqrt(2 * math.pi)
    return temp1 / temp2

print gaussian(1, 0.5, 0.63)

def integrate_gaussian(mu, sigma, xmin, xmax, n_steps):
    mu = float(mu)
    sigma = float(sigma)
    xmin = float(xmin)
    xmax = float(xmax)
    n_steps = int(n_steps)
    h = (xmax - xmin) / n_steps
    s = gaussian(xmin, mu, sigma) + gaussian(xmax, mu, sigma)
    for i in xrange(1, n_steps):
        s += 2 * gaussian(xmin + i * h, mu, sigma)
    return s * h / 2

mu = 3.
sigma = 1.
xmin = -10.
xmax = +10.
n_steps = 1000

print "integrate_gaussian(mu = 3., sigma =1., xmin = -10., xmax = +10., n_steps) ", integrate_gaussian(mu, sigma, xmin, xmax, n_steps)

# Decreasing the n_steps causes much less accurancy
# => the used numerous integral depends on small steps
# in relation to the integrated function
# so the resolution is great enough to recognize small changes in the graph

print "n_steps at 300 ", integrate_gaussian(mu, sigma, xmin, xmax, 300)
print "n_steps at 100 ", integrate_gaussian(mu, sigma, xmin, xmax, 100)
print "n_steps at 30 ", integrate_gaussian(mu, sigma, xmin, xmax, 30)
print "n_steps at 10 ", integrate_gaussian(mu, sigma, xmin, xmax, 10)
print "n_steps at 3 ", integrate_gaussian(mu, sigma, xmin, xmax, 3)

# The mu is 3, so setting the xmin also to 3
# gives only the a small area of the wanted graph
print "xmin = 3.", integrate_gaussian(mu, sigma, 3., xmax, n_steps)
print "xmin = 3., n_steps = 3", integrate_gaussian(mu, sigma, 3., xmax, 3)
