# This code generates FIR filter coefficients of an Low pass
# filter using the windowed-sinc method

import math
import numpy as np
import matplotlib.pyplot as plt

PI = math.pi

# window function variables
RECTANGULAR = 0
BARLETT = 1
HANN = 2
HAMMING = 3
BLACKMAN = 4


# Define the window class
class Window:
    def __init__(self, attenuation, transition):
        self.attenuation = attenuation  # Peak approximation error in dB
        self.transition = transition    # Transition band width in rads/s

        # find the window type based on attenuation and the window length based on TBW
        if (abs(self.attenuation) <= 21):
            self.winFunc = RECTANGULAR    # Rectangular function
            self.L = math.ceil((1.8*PI)/self.transition)

        elif (abs(self.attenuation)>21 and abs(self.attenuation)<=26):
            self.winFunc = BARLETT    # Barlett function
            self.L = math.ceil((6.1*PI)/self.transition)

        elif (abs(self.attenuation)>26 and abs(self.attenuation)<=44):
            self.winFunc = HANN    # Hann function
            self.L = math.ceil((6.2*PI)/self.transition)

        elif (abs(self.attenuation)>44 and abs(self.attenuation)<=53):
            self.winFunc = HAMMING    # Hamming function
            self.L = math.ceil((6.6*PI)/self.transition)

        elif (abs(self.attenuation)>53 and abs(self.attenuation)<=74):
            self.winFunc = BLACKMAN    # Blackman function
            self.L = math.ceil((11*PI)/self.transition)

        if(self.valid == 1 and self.L % 2 == 0):    # in the window length is even, make it odd
            self.L = self.L + 1

        self.M = self.L - 1     # Filter order


    # window function according to the window type
    def window(self):
        if (self.winFunc == RECTANGULAR):
            # rectangular function definition
            W = np.ones(self.L, dtype=int)

        elif (self.winFunc == BARLETT):
            # Barlett function definition
            n = np.arange(self.L)
            W = 1 - np.abs((n - (self.M)/2) / ((self.L)/2))

        elif (self.winFunc == HANN):
            # Hann function definition
            n = np.arange(self.L)
            W = 0.5 - 0.5*np.cos((2*n*PI)/(self.M))

        elif (self.winFunc == HAMMING):
            # Hamming function definition
            n = np.arange(self.L)
            W = 0.54 - 0.46*np.cos((2*n*PI)/self.M)

        elif (self.winFunc == BLACKMAN):
            # Blackman function definition
            n = np.arange(self.L)
            W = 0.42 - 0.5*np.cos((2*n*PI)/self.M) + 0.08*np.cos((4*n*PI)/self.M)

        return W
    


# Define the filter class
class LP_Filter(Window):
    # The goal is to compute the impulse response of the filter
    def __init__(self, attenuation, transition, cutoff, sampling):   # cutoff is the cutoff frequency
        # Compute cutoff, attenuation and TBW from the constructor's params
        transition = (2*PI*transition)/sampling # convert to rads/sec
        self.cutoff = (2*PI*cutoff)/sampling    # convert to rads/sec
        self.length = 0
        self.sampling = sampling
        self.valid = 1

        if(transition>0 and cutoff>0 and sampling>0):
            if(self.cutoff > PI):       # Nyquist-Shannon Sampling theorem violated
                self.valid = 0
                print(f"Cutoff frequency canno exceed {sampling/2} Hz")

            elif(transition/2+self.cutoff >= PI or self.cutoff-transition/2 <= 0):  # Transisition band too large
                self.valid = 0
                print("Transition band too large")
            
            if(transition < 0.0001):
                self.valid = 0
                print("Transition band too narrow")

            if(attenuation > 74):       # Attenuation too high
                self.valid = 0
                print("Attenuation value is too high (Max = 74dB)")
        else:
            self.valid = 0
            print("Sampling, cutoff and transition must be > 0")

        if(self.valid == 1):
            super().__init__(abs(attenuation), transition)

    # define the method that returns the final impulse response
    def impulse(self):
        if(self.valid == 0):
            return 0        
    
        else:
            n = np.arange(self.L)
            h = (self.cutoff/PI) * np.sinc((self.cutoff*(n-self.L/2))/PI)
            h = h * super().window()
            self.length = self.L
            return h
        
    # define the function that computes the delay from the filter
    def delay(self):
        if(self.valid == 0):
            return 0
        else:
            return (self.M/2)/self.sampling
    


# user defined variables
sampling = 2000         # Sampling rate in samples/s or Hz
cutoff = 500            # Cutoff frequency in Hz
transition = 80         # Transition band width in Hz
attenuation = 50        # Attenuation in dB


lowPass = LP_Filter(attenuation, transition, cutoff, sampling)

h = lowPass.impulse()
w = lowPass.window()


# Plot the impulse response and the window function if valid
if(lowPass.valid == 1):

    # print the coefficients
    for i in h:
        print(f"{i}, ")
    
    # print the filter's length and group delay
    print(f"The number of coefficients is {lowPass.length}")
    print(f"The delay of this filter is {lowPass.delay()*1000} ms")

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
