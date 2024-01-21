# References:
# http://ijmcr.com/wp-content/uploads/2015/03/Paper6220-224.pdf
# https://tomroelandts.com/articles/how-to-create-a-configurable-filter-using-a-kaiser-window

import math
import numpy as np
import matplotlib.pyplot as plt


class Kaiser:
    def __init__(self, attenuation, transition, sampling): # attenuation(dB), transition(Hz)
        self.attenuation = attenuation
        self.transition = transition
        self.sampling = sampling

        # Compute beta
        if(self.attenuation < 21):
            self.beta = 0
        elif(21 <= self.attenuation and self.attenuation <= 50):
            self.beta = 0.5842*((self.attenuation-21)**0.4)
            self.beta = self.beta + 0.07886*(attenuation-21)
        elif(self.attenuation > 50):
            self.beta = 0.1102*(attenuation-8.7)

        # compute window length
        df = transition/self.sampling # normalized transition band widths
        if(attenuation > 21):
            self.N = (self.attenuation-7.95)/(14.36*df)+1
        else:
            self.N = 0.9222/df + 1

        # increase N to the next odd value
        self.N = round(self.N)
        if(self.N % 2 == 0):    # even
            self.N = self.N + 1
        else:                   # odd
            self.N = self.N +2

    # method to compute I(x) --> zeroth-order modified Bessel function of the first kind
    def zeroth_bessel(self, x):
        I = 1
        L = math.ceil(x)+1
        for k in range(1, L):
            I = I + (((x/2)**k)/np.math.factorial(k))**2
        return I
    
    def kaiser_window(self):
        w = np.zeros(self.N)
        for n in range(0, self.N):
            num = self.beta * np.sqrt(1-((2*n)/(self.N-1)-1)**2)
            w[n] = self.zeroth_bessel(num)/self.zeroth_bessel(self.beta)

        return w
    

class LP_Filter(Kaiser):
    def __init__(self, attenuation, transition, cutoff, sampling):
        self.cutoff = cutoff
        super().__init__(attenuation, transition, sampling)

    def impulse(self):
        w = super().kaiser_window()
        n = np.arange(self.N)
        cutoff = (self.cutoff*2*np.pi)/self.sampling
        h = (cutoff/np.pi) * np.sinc((cutoff*(n-(self.N-1)/2))/np.pi)
        return h*w
    
    def delay(self):
        return ((self.N-1)/2)/self.sampling
    
    def length(self):
        return self.N
    


sampling = 2000
attenuation = 30
cutoff = 500
transition = 50

lowPass = LP_Filter(attenuation, transition, cutoff, sampling)

h = lowPass.impulse()
w = lowPass.kaiser_window()

for i in h:
    print(f"{i}, ")

print(f"Delay = {lowPass.delay()}")
print(f"Coefficients = {lowPass.length()}")

plt.plot(h, label='h[n]', marker='o')
plt.plot(w, label='w[n]', marker='o')

# Add labels and title
plt.xlabel('sample')
plt.ylabel('amplitude')
plt.title('Impulse response of the designed filter')

# Add legend and grid
plt.legend()
plt.grid(True)
plt.show()
