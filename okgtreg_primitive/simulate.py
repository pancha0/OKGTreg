__author__ = 'panc'

"""
Create synthetic data

Reference:
[1] "DR for Supervised Learning with RKHSs" Fukumizu 2004
[2] "Estimating Optimal Transformations for Multiple Regression and Correlation" Brieman 1986
"""

import numpy as np
from scipy.special import cbrt # which can takes cubic root of negative values

def SimData_Breiman1(n, sigma=1):
    """
    Breiman 1 model
    This is a 1-d model.

        y = exp(x^3 + \epsilon)
        \epsilon ~ N(0,1)
        x^3 ~ N(0,1)

    :param n: sample size
    :param sigma:
    :return:
    """
    epsilon = sigma * np.random.randn(n)
    x3 = np.random.randn(n)
    y = np.exp(x3 + epsilon)
    x = cbrt(x3)
    # Standard data structure is a matrix
    x = np.matrix(x).T
    y = np.matrix(y).T
    return y, x

def SimData_Wang04(n):
    """
    modelName: Wang0

        y=log(4+sin(4 * X1) + |X1| + X2^2 + X3^3 + X4 + 0.1*\epsilon)
        Xi ~ Unif(-1, 1)
        \epsilon ~ N(0, 1)

    This model can be found from: http://partofthething.com/ace/samples.html

    :param n:
    :return:
    """
    x = [np.array([np.random.random() * 2.0 - 1.0 for i in range(n)]) for _i in range(0, 5)]
    noise = np.random.standard_normal(n)
    y = np.log(4.0 + np.sin(4 * x[0]) + np.abs(x[1]) + x[2] ** 2 +
                x[3] ** 3 + x[4] + 0.1 * noise)
    # Transform data to matrices
    xm = np.column_stack(x)
    ym = np.matrix(y).T

    return ym, xm

def SimData_MultiplyNoise(n):
    """
    Y = X1 + X2 * eps
    :param n:
    :return:
    """
    x = np.random.normal(0, 1, 2*n).reshape((n,2))
    noise = np.random.standard_normal(n)
    y = x[:,0] + x[:,1] * noise
    return np.matrix(y).T, np.matrix(x)
