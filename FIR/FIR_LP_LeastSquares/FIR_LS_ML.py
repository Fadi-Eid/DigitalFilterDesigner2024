import numpy as np
from scipy.linalg import (hankel, toeplitz)
import plotly.graph_objects as go
import random

# This script generates a dataset to train an ML model

# weight must be positive
def firls(numtaps, bands, desired, weight=None, nyq=None, fs=None):
    nyq = 1 # Nyquist frequency assumed to be 1 (fs = 2)

    numtaps = int(numtaps)
    if numtaps < 1:
        raise ValueError("numtaps must be >= 1")

    if numtaps % 2 == 0:
        numtaps = numtaps + 1

    
    M = (numtaps-1) // 2

    bands = np.asarray(bands).flatten() / nyq    
    bands.shape = (-1, 2)

    desired = np.asarray(desired).flatten()
    desired.shape = (-1, 2)

    if weight is None:
        weight = np.ones(len(desired))
    weight = np.asarray(weight).flatten()

    n = np.arange(numtaps)[:, np.newaxis, np.newaxis]
    q = np.dot(np.diff(np.sinc(bands * n) * bands, axis=2)[:, :, 0], weight)

    Q1 = toeplitz(q[:M+1])
    Q2 = hankel(q[:M+1], q[M:])
    Q = Q1 + Q2

    n = n[:M + 1]
    m = (np.diff(desired, axis=1) / np.diff(bands, axis=1))
    c = desired[:, [0]] - bands[:, [0]] * m
    b = bands * (m*bands + c) * np.sinc(bands * n)

    b[0] -= m * bands * bands / 2.
    b[1:] += m * np.cos(n[1:] * np.pi * bands) / (np.pi * n[1:]) ** 2
    b = np.dot(np.diff(b, axis=2)[:, :, 0], weight)

    a = np.linalg.solve(Q, b)

    coeffs = np.hstack((a[:0:-1], 2 * a[0], a[1:]))
    return coeffs

def PlotAmplitudeLinear(coeff, N):
    nfft = N * 4
    sampling = 2
    Hf = np.abs(np.fft.fft(coeff, nfft))
    freq = np.fft.fftfreq(nfft, d=1/sampling)
    

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=freq[:nfft//2], y=Hf[:nfft//2],
                        mode='lines', name='H(f)',
                        line=dict(color='violet', width=3)))
    fig2.update_layout(title='Amplitude response of the generated filter',
                xaxis_title='Frequency (Hz)',
                yaxis_title='Amplitude (Gain)',
                xaxis_type='linear',
                xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
                font=dict(family='Arial', size=14, color='black'),  # Customize font family and size
                legend=dict(x=0.02, y=0.98),  # Position legend in top-left corner
                plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
                paper_bgcolor='rgb(240, 240, 240)',  # Set paper background color
                margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins
                )
    fig2.show()

def PlotAmplitudeLogarithmic(coeff, N):
    nfft = N*5
    sampling = 2    # 2 Hz
    Hf = np.abs(np.fft.fft(coeff, nfft))
    freq = np.fft.fftfreq(nfft, d=1/sampling)

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=freq[:nfft//2], y=20 * np.log10(Hf[:nfft//2]),
                        mode='lines', name='H(f)',
                        line=dict(color='red', width=3)))
    fig3.add_shape(type="line",
            x0=0, y0=0, x1=max(freq), y1=0,
            line=dict(color="black", width=0.7))
    
    fig3.update_layout(title='Amplitude response of the generated filter',
                xaxis_title='Frequency (Hz)',
                yaxis_title='Amplitude (dB)',
                xaxis_type='linear',
                xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
                font=dict(family='Arial', size=14, color='black'),  # Customize font family and size
                legend=dict(x=0.02, y=0.98),  # Position legend in top-left corner
                plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
                paper_bgcolor='rgb(240, 240, 240)',  # Set paper background color
                margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins
                )
    fig3.show()

def Amplitude(coeff, N):
        n_fft = N     # number of FFT points
        Hf = np.abs(np.fft.fft(coeff, n_fft))   # amplitude response
        return Hf

def Amplitude_padded(coeff, N, padd = 5):
        n_fft = N*5     # number of FFT points
        Hf = np.abs(np.fft.fft(coeff, n_fft))   # amplitude response
        return Hf

def MSE(coeff, N, cutoff):
        M = N // 2 + 1
        df = 2 / N

        actual = Amplitude(coeff, N)  # actual amplitude response

        if actual is None:
            raise ValueError("Amplitude response is None")
        actual = actual[:M]

        # create the ideal amplitude
        cutoff_index = int(np.round(cutoff / df))  # Ensure integer value
        ideal1 = np.ones(cutoff_index)
        ideal2 = np.zeros(M - cutoff_index)
        ideal = np.concatenate((ideal1, ideal2))
        # compute the MSE
        mse = np.mean((actual - ideal) ** 2)
        return mse

def transitionMSE(coeff, N, cutoff, df):
    # compute the mag. response of coeff
    padd = 5   # fft padding
    M = (N*padd) // 2 + 1 # half
    actual = Amplitude_padded(coeff, N, padd)
    # create the frequency axis vector
    actual = actual[:M]

    # find the index of the cutoff frequency
    cutoff_low_index = int(round((cutoff-df/2) * M))
    cutoff_high_index = int(round((cutoff+df/2) * M))
    actual = actual[cutoff_low_index:cutoff_high_index]

    # create the ideal transition
    ideal = np.linspace(1, 0, len(actual))

    mse = np.mean((actual - ideal) ** 2)
    return mse

def computeAttenuation(coeff, N, cutoff):
    nfft = N*5
    sampling = 2
    M = nfft // 2 + 1
    Hf = np.abs(np.fft.fft(coeff, nfft))
    y=20 * np.log10(Hf[:M])
    cutoff_index = int(round((cutoff) * M))
    mag = y[cutoff_index]
    while(True):
        cutoff_index = cutoff_index + 1
        if y[cutoff_index] < mag:
            mag = y[cutoff_index]
        else:
             return y[cutoff_index]
         




NFLTR = 0
count = 1
while(True):
    # create cutoff frequency
    cutoff = random.uniform(0.1, 0.9)
    #print("Cutoff:", cutoff)

    # generate a transition band  width
    while True:
        df = random.uniform(0.005, 0.15)
        if cutoff - df/2 > 0.05:
            break
        if cutoff + df/2 < 0.95:
            break
        cutoff = random.uniform(0.1, 0.9)

    #print("Transition band: ", df)

    

    # generate weights
    Kp = 1
    Ks = random.uniform(1, 5)

    # generate filter order
    N = random.randint(30, 8000)
    #print("Filter length: ", N)
    
    coeff = firls(numtaps=N, bands=[0, cutoff - df/2, cutoff + df/2, 1], desired=[1, 1, 0, 0], weight=[Kp, Ks])
    amp = Amplitude(coeff, N)


    # best transition MSE = 0.4
    if  np.max(amp) < 1.5 and transitionMSE(coeff, N, cutoff, df) < 0.025:
        NFLTR = NFLTR + 1
        ripple = np.max(amp)
        attenuation = computeAttenuation(coeff, N, cutoff)
        print(f"generated filter #{NFLTR} iteration {count}")       
        print("_____________________________________________________\n\n")
        with open('TrainingSet.txt', 'a') as file:
             file.write(f"{N}, {attenuation}, {abs(1-ripple)}, {df}, {Ks}\n")
             # Attenuation: Stop band attenuation in dB
             # N: Filter length
             # ripple: Pass-band gain
             # df: transition band width in Hz
             # Ks: stop-band weight (Kp=1)


    
    count = count + 1

    if NFLTR > 1000:
         break