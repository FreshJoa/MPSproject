import numpy as np

class Sampler:
    def __init__(self):
        self.psi=None
        self.x=0

    def SetPsi(self,Psi):
        self.psi=Psi

    #Metropolis-Hastings acceptance test
    def Metropolis(self,step_size):
        xprime=self.x+(np.random.uniform()-0.5)*step_size
        if(self.psi.GetPsi(xprime)/self.psi.GetPsi(self.x)) > np.random.uniform():
            self.x=xprime

    def LocalEnergy(self):
        return -0.5 * (2.*self.psi.alpha + (2.*self.psi.alpha*self.x)**2.) + 0.5 * self.x**2
