import numpy as np
from scipy.linalg import (hankel, toeplitz)
import mpmath as mp
import plotly.graph_objects as go

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
    nfft = N*4
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


N = 2211
coeff = firls(numtaps=N, bands=[0, 0.395, 0.405, 1], desired=[1, 1, 0, 0], weight=[1, 3])

PlotAmplitudeLogarithmic(coeff, N)
PlotAmplitudeLinear(coeff, N)