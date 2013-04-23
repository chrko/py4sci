"""
normalized gaussian distribution for position x and parameters mu and sigma

(c) Christian Kohlstedde
"""

def gaussian(x, mu, sigma):
    import math
    
    temp1 = math.exp(-math.pow(x-mu,2)/(2 * sigma**2))
    temp2 = sigma * math.sqrt(2 * math.pi)
    return temp1 / temp2

print gaussian(1, 0.5, 0.63)

def integrate_gaussian(mu, sigma, xmin, xmax, n_steps):
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

print integrate_gaussian(mu, sigma, xmin, xmax, n_steps)
