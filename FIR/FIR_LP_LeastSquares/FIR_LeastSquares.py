import numpy as np
from scipy.linalg import (hankel, toeplitz)
import plotly.graph_objects as go



class FIR_Filter():
    def __init__(self, fs, numtaps, bands, desired, weight=None):
        self.numtaps = numtaps

        self.numtaps = int(self.numtaps)
        if self.numtaps < 1:
            raise ValueError("numtaps must be >= 1")

        if self.numtaps % 2 == 0:    # make odd (Type 1)
            self.numtaps = self.numtaps + 1

        self.bands = bands
        self.desired = desired
        self.weight = weight
        self.fs = fs
        self.nyq = self.fs/2    # normalized Nyquist frequency (1Hz)
        self.computedCoeffs = 0
        self.coeffs = np.zeros(self.numtaps)


    def Impulse(self):
        if self.computedCoeffs == 1:
            return self.coeffs

        M = (self.numtaps-1) // 2

        self.bands = np.asarray(self.bands).flatten() / self.nyq    
        self.bands.shape = (-1, 2)

        self.desired = np.asarray(self.desired).flatten()
        self.desired.shape = (-1, 2)

        if self.weight is None:
            self.weight = np.ones(len(self.desired))
        self.weight = np.asarray(self.weight).flatten()

        n = np.arange(self.numtaps)[:, np.newaxis, np.newaxis]
        q = np.dot(np.diff(np.sinc(self.bands * n) * self.bands, axis=2)[:, :, 0], self.weight)

        Q1 = toeplitz(q[:M+1])
        Q2 = hankel(q[:M+1], q[M:])
        Q = Q1 + Q2

        n = n[:M + 1]
        m = (np.diff(self.desired, axis=1) / np.diff(self.bands, axis=1))
        c = self.desired[:, [0]] - self.bands[:, [0]] * m
        b = self.bands * (m*self.bands + c) * np.sinc(self.bands * n)

        b[0] -= m * self.bands * self.bands / 2.
        b[1:] += m * np.cos(n[1:] * np.pi * self.bands) / (np.pi * n[1:]) ** 2
        b = np.dot(np.diff(b, axis=2)[:, :, 0], self.weight)

        a = np.linalg.solve(Q, b)

        self.coeffs = np.hstack((a[:0:-1], 2 * a[0], a[1:]))
        self.computedCoeffs = 1
        return self.coeffs


    def PlotImpulse(self):
        if self.computedCoeffs == 0:
            self.Impulse()

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(y=self.coeffs,
                         mode='lines', name='h(n)',
                         line=dict(color='green', width=3)))
        fig1.update_layout(title='Impulse response of the generated filter',
                  xaxis_title='Sample',
                  yaxis_title='Value',
                  xaxis_type='linear',
                  xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
                  font=dict(family='Arial', size=14, color='black'),  # Customize font family and size
                  legend=dict(x=0.02, y=0.98),  # Position legend in top-left corner
                  plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
                  paper_bgcolor='rgb(240, 240, 240)',  # Set paper background color
                  margin=dict(l=50, r=50, t=50, b=50),  # Adjust margins
                  )
        fig1.show()
    
    
    def PlotAmplitudeLinear(self):
        if self.computedCoeffs == 0:
            self.Impulse()

        N = self.numtaps
        nfft = N * 4
        sampling = self.fs

        Hf = np.abs(np.fft.fft(self.coeffs, nfft))
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

    
    def PlotAmplitudeLogarithmic(self):
        if self.computedCoeffs == 0:
            self.Impulse()

        N = self.numtaps
        nfft = N*4
        sampling = self.fs    # 2 Hz
        Hf = np.abs(np.fft.fft(self.coeffs, nfft))
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


    def SaveCoeffs(self):
        if self.computedCoeffs == 0:
            self.Impulse()
        fileName = 'coefficients.csv'
        np.savetxt(fileName, self.coeffs, delimiter=',')

    def PrintCoeffs(self):
        if self.computedCoeffs == 0:
            self.Impulse()
        for i in self.coeffs:
            print(f"{i}, ")

    # (N-1)/2 * Fs --> x1000 for milliseconds
    def Delay(self):
        delay = (((self.numtaps - 1)/2) / self.fs) * 1000
        return delay

    # compute the amplitude response
    def Amplitude(self):
        if self.computedCoeffs == 0:
            self.Impulse()
        Hf = np.abs(np.fft.fft(self.coeffs, self.numtaps))   # amplitude response
        return Hf
    


######################################################################################
    
# create the filter class
Filter = FIR_Filter(2, 501, [0, 0.5, 0.55, 1], [1, 1, 0, 0], [1, 1])
Filter.PlotAmplitudeLinear()
Filter.PlotAmplitudeLogarithmic()
Filter.PlotImpulse()
Filter.PrintCoeffs()
Filter.SaveCoeffs()
