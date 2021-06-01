import numpy as np

class State:
    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, x):
        return np.exp(self.alpha*x**2.)

    def GetPsi(self, x):
        return np.exp(self.alpha*x**2.)

    def DerLog(self, x):
        return x**2.

