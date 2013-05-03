"""

"""
import numpy as np
import matplotlib.pyplot as plt

# var definition
# s_ => sigma
m_1 = 40*10**4
s_m_1 = 0.05*10**4
m_2 = 30*10**4
s_m_2 = 0.1*10**4
r = 3.2
s_r = 0.01
G = 6.67384*10**(-11)

# monte carlo
n = 10**6


def force(m_1, m_2, r):
    return G * m_1 * m_2 / r**2


def force_sigma(m_1, s_m_1, m_2, s_m_2, r, s_r):
    return np.sqrt(
        (G/r**2)**2
        * (
            (m_2 * s_m_1)**2
            + (m_1 * s_m_2)**2
            + (-2 * m_1 * m_2 / r * s_r)**2
        )
    )
