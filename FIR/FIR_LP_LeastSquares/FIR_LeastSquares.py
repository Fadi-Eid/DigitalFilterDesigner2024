# non-iterative Optimal (in the least-squares sense) FIR filter design
# using the weighted least-squares method.
# A weighting factor (K) was used to give importance to the stop-band
# over the pass-band, ensuring high levels of attenuation (~160dB).

# References:
# New York University, Linear-phase FIR filter design by least squares

import numpy as np
from scipy.linalg import toeplitz
from scipy.linalg import hankel
import matplotlib.pyplot as plt


class LP_Filter():
    def __init__(self, attenuation, transition, cutoff, sampling):
        # check if the input is valid
        # pass-band and stop-band frequencies
        self.cutoff = cutoff
        self.transition = transition
        self.attenuation = attenuation
        self.sampling = sampling
        self.fp = (cutoff-df/2)
        self.fs = (cutoff+df/2)
        self.K = 3
        self.N = 0
        # filter length estimation using the Fred Harris rule of thumb
        A = attenuation
        if A <= 60:
            self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.1)
        elif A > 60 and A <= 80:
            self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.25)
        elif A > 80 and A <= 150:
            self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.4)
        elif A > 150:
            if A <= 160:
                self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.52)
            else:
                A = 165
                self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.6)
        
        if self.N % 2 == 0:
            self.N += 1
        self.M = (self.N - 1) // 2

        # normalize fp and fs
        self.fp = self.fp / (self.sampling / 2)
        self.fs = self.fs / (self.sampling / 2)

    def impulse(self):
        # construct q(k)
        x1 = np.array([self.fp + self.K * (1 - self.fs)])
        x2 = self.fp * np.sinc(self.fp * np.arange(1, 2 * self.M+1)) - self.K * self.fs * np.sinc(self.fs * np.arange(1, 2 * self.M + 1))
        q = np.concatenate((x1, x2))

        # construct Q1, Q2, Q
        Q1 = toeplitz(q[0:self.M+1])
        Q2 = hankel(q[:self.M + 1], q[self.M:2 * self.M + 1])
        Q = (Q1 + Q2) / 2

        # construct b
        b = self.fp * np.sinc(self.fp * np.arange(self.M + 1))

        # solve linear system to get a(n)
        a = np.linalg.solve(Q, b)

        # form impulse response h(n)
        h = np.concatenate([a[self.M:0:-1], 2 * a[0] * np.ones(1), a[1:self.M + 1]]) / 2

        return h
    
    def length(self):
        return self.N
    
    # (N-1)/2 * Fs --> x1000 for milliseconds
    def GroupDelay(self):
        delay = (((self.N - 1)/2) / self.sampling) * 1000
        return delay
    
    

###################################################################################
###################################################################################
# USER CODE
# Filters params
sampling = 2000     # sampling frequency in Hz
cutoff = 300        # cutoff frequency in Hz
df = 1             # transition band width in Hz
A = 59             # max dB attenuation


lowPass = LP_Filter(A, df, cutoff, sampling)
h = lowPass.impulse()


for i in h:
    print(f"{i}, ")

print(f"Number of coefficients = {lowPass.length()}")
print(f"Delay = {lowPass.GroupDelay()} ms")

###################################################################################
###################################################################################

# VALIDATION code

# Plot impulse response
plt.figure(1, figsize=(10, 5))
plt.plot(h, label='h[n]', marker='o')
plt.xlabel('sample')
plt.ylabel('amplitude')
plt.title('Impulse response of the designed filter')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Zero-padding and Compute frequency response
n_fft = (lowPass.length())*4  # Increase the resolution of the frequency bins
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
