# non-iterative Optimal (in the least-squares sense) FIR filter design
# using the weighted least-squares method.
# A weighting factor (K) was used to give importance to the stop-band
# over the pass-band, ensuring high levels of attenuation (~160dB).

# References:
# New York University, Linear-phase FIR filter design by least squares

import numpy as np
from scipy.linalg import toeplitz
from scipy.linalg import hankel
import plotly.graph_objects as go


class LP_Filter():
    def __init__(self, attenuation, transition, cutoff, sampling):
        self.cutoff = cutoff
        self.transition = transition
        self.attenuation = attenuation
        self.sampling = sampling
        self.fp = (cutoff-self.transition/2)
        self.fs = (cutoff+self.transition/2)
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
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(y=ht,
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
        nfft = self.Length()
        Hf = np.abs(np.fft.fft(self.Impulse(), nfft))
        freq = np.fft.fftfreq(nfft, d=1/self.sampling)

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
        nfft = self.Length()*4
        Hf = np.abs(np.fft.fft(self.Impulse(), nfft))
        freq = np.fft.fftfreq(nfft, d=1/self.sampling)

        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=freq[:nfft//2], y=20 * np.log10(Hf[:nfft//2]),
                         mode='lines', name='H(f)',
                         line=dict(color='red', width=3)))
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

    def SaveCoeffs(self, path):
        fileName = f"{path}/coefficients.csv"
        if fileName == "":
            np.savetxt("./coefficients.csv", self.Impulse(), delimiter=',')
        else:
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
