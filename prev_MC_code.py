import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt

def kroupa_imf(mf):
    if mf < 0.08:
        return mf**(-0.3)
    elif 0.08 <= mf < 0.5:
        return mf**(-1.3)
    elif 0.5 <= mf < 1:
        return mf**(-2.3)
    elif 1 <= mf:
        return mf**(-2.3)

n_star = [100, 1000, 10000, 100000]

for star in n_star:
    masa_min = 0.01
    masa_max = 100
    gen_masa = np.random.uniform(masa_min, masa_max, star)
    output = [kroupa_imf(mf) for mf in gen_masa]

    log_gm = np.log(gen_masa)
    log_out = np.log(output)

    plt.figure() 
    plt.scatter(log_gm, log_out)
    plt.xlabel("log(mf)")
    plt.ylabel("log(Resultado Kroupa IMF)")
    plt.title("Kroupa IMF para {num_estrellas} estrellas")

plt.show()

edad_max = 10**(7) #x10^10
edad= np.random.uniform(0, edad_max, num_estrellas)
datos_estrellas = [(masa, edad) for masa, edad in zip(gen_masa, edad)] 

def MS_lifetime(masa):
    t_lifetime = (10**10) / masa**(2.5)
    return t_lifetime

def masa_final(m_i):
    if m_i < 8:
        m_f_WD = 0.109 * m_i + 0.394
        return m_f_WD, "wd", m_i
    elif 8 <= m_i < 13:
        m_f_NS1 = 2.24 + 0.508 * (m_i - 14.75) + 0.125 * (m_i - 14.75)**2 + 0.011 * (m_i - 14.75)**3
        return m_f_NS1, "ns", m_i
    elif 13 <= m_i < 15:
        m_f_NS2 = 0.123 + 0.112 * m_i
        return m_f_NS2, "ns", m_i
    elif 15 <= m_i < 17.8:
        m_f_NS3 = 0.996 + 0.384 * m_i
        return m_f_NS3, "ns", m_i
    elif 17.8 <= m_i < 18.5:
        m_f_NS4 = -0.02 + 0.1 * m_i
        return m_f_NS4, "ns", m_i
    elif 18.5 <= m_i < 45:
        m_f_BH1 = 15.52 - 0.3294 * (m_i - 25.97) - 0.02121 * ((m_i - 25.97)**2) + 0.003120 * ((m_i - 25.97)**3)
        return m_f_BH1, "bh", m_i
    elif 45 < m_i < 120:
        m_f_BH2 = 5.697 + (7.8598 * 10**8) * ((m_i)**(-4.858))
        return m_f_BH2, "bh", m_i
    else:
        return None, None, m_i
