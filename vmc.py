import numpy as np

class Sampler:
    def __init__(self):
        self.psi=None
        self.x=0

    def SetPsi(self,Psi):
        self.psi=Psi

    #Metropolis-Hastings acceptance test
    def Step(self,step_size):

        #Markov-Chain transitions
        #the particle is displaced by a uniform random quantity
        #in 0.5[-step_size,step_size]
        xprime=self.x+(np.random.uniform()-0.5)*step_size
        #we compute (Psi(xprime)/Psi(x))^2
        #in order to avoid overflow/underflow, we use the logarithm of the wave-function
        if(self.psi.GetPsi(xprime)/self.psi.GetPsi(self.x)) > np.random.uniform():
            self.x=xprime


    #Local energy (see script)
    def LocalEnergy(self):
        return -0.5 * (2.*self.psi.alpha + (2.*self.psi.alpha*self.x)**2.) + 0.5 * self.x**2
