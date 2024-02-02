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
    
    def window(self):
        w = np.zeros(self.N)
        for n in range(0, self.N):
            num = self.beta * np.sqrt(1-((2*n)/(self.N-1)-1)**2)
            w[n] = self.zeroth_bessel(num)/self.zeroth_bessel(self.beta)

        return w
    

class LP_Filter(Kaiser):
    def __init__(self, attenuation, transition, cutoff, sampling):
        # check if the input is valid
        self.valid = 1
        if(attenuation<0):
            attenuation = abs(attenuation)
            print(f"Warning, attenuation value < 0. Will use {attenuation} instead")
        if(attenuation>150):
            self.valid = 0
            print(f"Attenuation value is too high")
        if((transition*2*np.pi)/sampling < 0.0001):
            self.valid = 0
            print(f"Transition band is too narrow")
        if(cutoff < 0 or cutoff >= sampling/2):
            self.valid = 0
            print(f"Cutoff frequency violation (Nyquist-Shannon). Cutoff should be < {sampling/2} Hz")
        if(sampling < 0):
            self.valid = 0
            print("Error: Sampling frequency should be a positive number")
        if(transition/2+cutoff >= sampling/2 or cutoff-transition/2 <= 0):
            self.valid = 0
            print("Transition band is too wide")

        self.cutoff = cutoff
        if(self.valid == 1):
            super().__init__(attenuation, transition, sampling)

    def impulse(self):
        if(self.valid==1):
            w = super().window()
            n = np.arange(self.N)
            cutoff = (self.cutoff*2*np.pi)/self.sampling
            h = (cutoff/np.pi) * np.sinc( (cutoff*(n - (self.N-1)/2)) / np.pi )
            return h*w
        else:
            return 0
    # (N-1)/2 * Fs --> x1000 for milliseconds
    def GroupDelay(self):
        if(self.valid==0):
            return 0
        return ((self.N-1)/2)/self.sampling * 1000
    
    def length(self):
        if(self.valid==0):
            return 0
        return self.N
    

###################################################################################
###################################################################################
# USER CODE

# user defined variables
sampling = 2000         # Sampling rate in samples/s or Hz
cutoff = 300            # Cutoff frequency in Hz
transition = 80         # Transition band width in Hz
attenuation = 72       # Attenuation in dB

lowPass = LP_Filter(attenuation, transition, cutoff, sampling)

h = lowPass.impulse()
w = lowPass.window()

for i in h:
    print(f"{i}, ")

print(f"Delay = {lowPass.GroupDelay()} ms")
print(f"Coefficients = {lowPass.length()}")

###################################################################################
###################################################################################

# VALIDATION code

# Plot impulse response
plt.figure(1, figsize=(10, 5))
plt.plot(h, label='h[n]', marker='o')
plt.plot(w, label='w[n]', marker='o')
plt.xlabel('sample')
plt.ylabel('amplitude')
plt.title('Impulse response of the designed filter')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Zero-padding and Compute frequency response
n_fft = 2048  # Increase the resolution of the frequency bins
frequencies = np.fft.fftfreq(n_fft, d=1/sampling)
magnitude_response = np.abs(np.fft.fft(h, n_fft))


# Plot magnitude response in dB
plt.figure(2, figsize=(10, 5))
plt.plot(frequencies[:n_fft//2], 20 * np.log10(magnitude_response[:n_fft//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Magnitude Response of the generated Filter (Logarithmic scale)')
plt.grid(True)
plt.show()

# Plot magnitude response in linear scale
plt.figure(3, figsize=(10, 5))
plt.plot(frequencies[:n_fft//2], magnitude_response[:n_fft//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Response of the generated Filter (Linear Scale)')
plt.grid(True)
plt.show()
