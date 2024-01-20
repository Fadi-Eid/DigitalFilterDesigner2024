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
        self.valid = 1      # 1 means that the filter can be calculated
        self.attenuation = attenuation  # Peak approximation error in dB
        self.transition = transition    # Transition band width in rads/s

        if(abs(self.attenuation) > 74):
            self.valid = 0  # Attenuation in too high, filter is invalid

        # find the window type based on attenuation and the window length based on TBW
        elif (abs(self.attenuation) <= 21):
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
        if(self.valid == 0):
            W = 0       # No valid window function for the required attenuation (too high)
        
        elif (self.winFunc == RECTANGULAR):
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
        super().__init__(attenuation, transition)

        if(self.cutoff > PI):       # Nyquist-Shannon Sampling theorem violated
            self.valid =0

    # define the method that returns the final impulse response
    def impulse(self):
        if(self.valid == 0):
            print("Attenuation value is too high")
            return 0
        elif(self.cutoff >= PI):
            print(f"Cutoff frequency is limited to {self.sampling/2} (Nyquist frequency)")
            self.valid = 0
            return 0
    
        else:
            n = np.arange(self.L)
            h = (self.cutoff/PI) * np.sinc((self.cutoff*(n-self.L/2))/PI)
            h = h * super().window()
            self.length = self.L
            return h
        
    # define the function that computes the delay from the filter
    def delay(self):
        return (self.M/2)/self.sampling
    


# user defined variables
sampling = 2000        # Sampling rate in samples/s or Hz
cutoff = 555           # Cutoff frequency in Hz
transition = 50        # Transition band width in Hz
attenuation = 30        # Attenuation in dB


lowPass = LP_Filter(attenuation, transition, cutoff, sampling)

h = lowPass.impulse()


# Plot the impulse response and the window function if valid
if(lowPass.valid == 1):

    # print the coefficients
    for i in h:
        print(f"{i}, ")
    
    # print the filter's length and group delay
    print(f"The number of coefficients is {lowPass.length}")
    print(f"The delay of this filter is {lowPass.delay()*1000} ms")

    # Plotting the generated impulse response
    plt.plot(h, label='h[n]', marker='o')

    # Plotting the chosen window function
    w = lowPass.window()
    plt.plot(w, label='w[n]', marker='o')

    # Add labels and title
    plt.xlabel('sample')
    plt.ylabel('amplitude')
    plt.title('Impulse response of the designed filter')

    # Add legend and grid
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

