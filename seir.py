import sys
import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
import time
from matplotlib.figure import Figure

# we initialize data up till April 12th, 2020

# Sources:
# https://coronavirus.1point3acres.com/en
# https://www.chwsny.org/wp-content/uploads/2018/04/Full_CHWS_NY_Tracking_Report-2018b-1.pdf

# Population of Erie County, NY
N = 918702  # source: https://www.census.gov/quickfacts/eriecountynewyork

# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1624, 560

# People exposed to COVID19 up to 4/12/2020
E0 = 113000

# Everyone else, S0, is susceptible to infection initially
S0 = N - I0 - R0 - E0
#print(S0)
# Contact rate (set by user)
beta = float(sys.argv[1])
#beta = float(input("Enter how many people outside will you be in contact with per day (can be in decimal): "))

# Source for info below: https://patient.info/news-and-features/coronavirus-how-quickly-do-covid-19-symptoms-develop-and-how-long-do-they-last
# Mean recovery rate and incubation period
days = 11.5  # infections lasts 11.5 days on average
gamma = 1/days
delta = 1/5  # COVID-19 has an average incubation period of 5 days.
# A grid of time points (in days) for 6 months
t = np.linspace(0, 183, 183)

# SEIR model differential equations setup
def deriv(y, t, N, beta, gamma, delta):
    S, E, I, R = y
    dSdt = -beta * I * S / N
    dEdt = beta * I * S / N - delta * E
    dIdt = delta * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SEIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta))
S, E, I, R = ret.T

# Data plotting
f, ax = plt.subplots(1,1,figsize=(10,4))
ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label='Exposed')
ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered + Removed')
ax.plot(t, S+E+I+R, 'c--', alpha=0.7, linewidth=2, label='Total Population = 918,702')

ax.set_xlabel('Time (days)')
ax.set_ylabel('Populations')

ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)

filename = ("images/plots/my_plot_%s.png" %time.time())
plt.savefig(filename)
print(filename)

# Code reference: https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4
# https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/
