import matplotlib.pyplot as plt
import xlrd
import networkx as nx
import powerlaw
from scipy.optimize import curve_fit
import numpy as np


# https://vigges.net/qa/?qa=925442/ https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509
def plotting(degr_seq):
    something = power_law(degr_seq, 1, 1)

    fig = plt.figure("Degree of a random graph", figsize=(8, 8))

    pars, cov = curve_fit(
        f=power_law,
        xdata=degr_seq,
        ydata=something,
        p0=[0, 0],
        bounds=(-np.inf, np.inf),
    )
    stdevs = np.sqrt(np.diag(cov))
    print(*pars)
    ax = fig.add_subplot()
    plt.hist(degr_seq, bins=100)
    ax.plot(
        degr_seq, power_law(degr_seq, *pars), linestyle="--", linewidth=2, color="r"
    )
    plt.show()


def power_law(x, a, b):
    return a * np.power(x, b)


# plotting(degrees)

import numpy as np
from scipy.optimize import curve_fit


def powlaw(x, a, b):
    return a * np.power(x, b)


def linlaw(x, a, b):
    return a + x * b


def curve_fit_log(xdata, ydata):
    """Fit data to a power law with weights according to a log scale"""
    # Weights according to a log scale
    # Apply fscalex
    xdata_log = np.log10(xdata)
    # Apply fscaley
    ydata_log = np.log10(ydata)
    # Fit linear
    popt_log, pcov_log = curve_fit(linlaw, xdata_log, ydata_log)
    # print(popt_log, pcov_log)
    # Apply fscaley^-1 to fitted data
    ydatafit_log = np.power(10, linlaw(xdata_log, *popt_log))
    # There is no need to apply fscalex^-1 as original data is already available
    print(popt_log, pcov_log, ydatafit_log)
