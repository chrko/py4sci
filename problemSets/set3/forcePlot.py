"""

"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# function to compute the force between two masses
def force(m_1, m_2, r):
    return G * m_1 * m_2 / r**2


# compute the sigma of the force by given values
def force_sigma(m_1, s_m_1, m_2, s_m_2, r, s_r):
    return np.sqrt(
        (G/r**2)**2
        * (
            (m_2 * s_m_1)**2
            + (m_1 * s_m_2)**2
            + (-2 * m_1 * m_2 / r * s_r)**2
        )
    )


# returning x/y-values for a gaussian distribution
def gaussian(mean, sigma, xmin=0., xmax=10., steps=100):
    x = np.linspace(xmin, xmax, steps)
    y = (1. / (sigma * np.sqrt(2. * np.pi))
         * np.exp(-(x - mean)**2 / (2. * sigma**2)))
    return x, y


# monte carlo plotting
def mc_plot(filename="fig.png"):
    m_1s = np.random.normal(m_1, s_m_1, n)
    m_2s = np.random.normal(m_2, s_m_2, n)
    rs = np.random.normal(r, s_r, n)

    force_calc = force(m_1, m_2, r)
    forces = force(m_1s, m_2s, rs)
    sigma = force_sigma(m_1, s_m_1, m_2, s_m_2, r, s_r)

    x, y = gaussian(force_calc, sigma, np.min(forces), np.max(forces))

    # clearing plt to remove old things
    plt.cla()

    # plotting the hist and the line
    plt.hist(forces, bins=50, normed=True)
    plt.plot(x, y, linewidth=3, color='red')

    # saving the fig under the given filename
    plt.savefig(filename)

# var definition
# s_ => sigma
m_1, m_2, r = 40*10**4, 30*10**4, 3.2
G = 6.67384*10**(-11)

# monte carlo
n = 10**6

s_m_1, s_m_2, s_r = 0.05*10**4, 0.1*10**4, 0.01
mc_plot('fig1.png')

s_m_1, s_m_2, s_r = 2*10**4, 10*10**4, 1
mc_plot('fig2.png')
