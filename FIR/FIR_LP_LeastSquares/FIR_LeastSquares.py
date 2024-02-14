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
        elif A > 150 and A <= 165:
            self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.52)
        else:
            A = 170
            self.N = round((sampling / (self.fs - self.fp)) * (abs(A) / 22) * 1.7)
        
        if self.N % 2 == 0:
            self.N += 1

        self.M = (self.N - 1) // 2

        # normalize fp and fs
        self.fp = self.fp / (self.sampling / 2)
        self.fs = self.fs / (self.sampling / 2)

    def Impulse(self):
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
    
    def Length(self):
        return self.N
    
    # (N-1)/2 * Fs --> x1000 for milliseconds
    def Delay(self):
        delay = (((self.N - 1)/2) / self.sampling) * 1000
        return delay
    
    # compute the amplitude response
    def Amplitude(self):
        n_fft = self.N      # number of FFT points
        Hf = np.abs(np.fft.fft(self.Impulse(), n_fft))   # amplitude response
        return Hf

    def PlotImpulse(self):
        ht = self.Impulse()
        plt.figure(1, figsize=(10, 5))
        plt.plot(ht, label='h[n]')
        plt.xlabel('sample')
        plt.ylabel('amplitude')
        plt.title('Impulse response of the designed filter')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def PlotAmplitudeLinear(self):
        nfft = self.Length()
        Hf = np.abs(np.fft.fft(self.Impulse(), nfft))
        freq = np.fft.fftfreq(nfft, d=1/self.sampling)
        # Plot magnitude response in linear scale
        plt.figure(3, figsize=(10, 5))
        plt.plot(freq[:nfft//2], Hf[:nfft//2])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.title('Magnitude Response of the generated Filter (Linear Scale)')
        plt.grid(True)
        plt.show()

    def PlotAmplitudeLogarithmic(self):
        nfft = self.Length()*4
        Hf = np.abs(np.fft.fft(self.Impulse(), nfft))
        freq = np.fft.fftfreq(nfft, d=1/self.sampling)
        plt.figure(2, figsize=(10, 5))
        plt.plot(freq[:nfft//2], 20 * np.log10(Hf[:nfft//2]), marker='o')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (dB)')
        plt.title('Magnitude Response of the generated Filter (Logarithmic scale)')
        plt.grid(True)
        plt.show()

    def SaveCoeffs(self):
        fileName = 'coefficients.csv'
        np.savetxt(fileName, self.Impulse(), delimiter=',')

    def PrintCoeffs(self):
        for i in self.Impulse():
            print(f"{i}, ")

    # Calculate the Mean squared error between the desired
    # and the actual response, this can be used as a cost function
    def MSE(self):
        M = self.Length() // 2 + 1
        df = self.sampling / self.Length()
        actual = self.Amplitude()  # actual amplitude response

        if actual is None:
            raise ValueError("Amplitude response is None")
        actual = actual[:M]

        # create the ideal amplitude
        cutoff_index = int(np.round(self.cutoff / df))  # Ensure integer value
        ideal1 = np.ones(cutoff_index)
        ideal2 = np.zeros(M - cutoff_index)
        ideal = np.concatenate((ideal1, ideal2))
        # compute the MSE
        mse = np.mean((actual - ideal) ** 2)
        return mse

###################################################################################
###################################################################################


# USER CODE
# Filters params
sampling = 20000     # sampling frequency in Hz
cutoff = 5000        # cutoff frequency in Hz
df = 20            # transition band width in Hz
A = 200             # max dB attenuation

# create an instance of the filter
lowPass = LP_Filter(A, df, cutoff, sampling)


# lowPass class methods

mse = lowPass.MSE()
print(f"Error between ideal and actual filter = {mse}")

N = lowPass.Length()
print(f"Number of filter coefficients = {N}")

#d = lowPass.Delay()
#print(f"Delay of the filter = {d} milliseconds")

#h = lowPass.Impulse()
#Hf = lowPass.Amplitude()

#lowPass.PlotImpulse()
lowPass.PlotAmplitudeLogarithmic()
lowPass.PlotAmplitudeLinear()

#lowPass.PrintCoeffs()
#lowPass.SaveCoeffs()
