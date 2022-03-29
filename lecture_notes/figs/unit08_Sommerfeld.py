#!/usr/bin/python3
# ------------------------------------------------------------------
# Adapting from
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (6,3)

x = np.arange(-12, 12, 0.001)
integrand = np.exp(x) / (np.exp(x) + 1)**2
plt.plot(x, integrand, label="$e^x / (e^x + 1)^2$")
plt.xlabel('$\\beta(E - \\mu)$')
plt.xticks([-15,-10,-5,0,5,10,15])
plt.ylim([0.0, 0.26])
plt.legend(loc='upper right')
#plt.show()
plt.savefig('unit08_Sommerfeld.pdf', bbox_inches='tight')
# ------------------------------------------------------------------
