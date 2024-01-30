import numpy as np
from scipy.linalg import toeplitz
from scipy.linalg import hankel
import matplotlib.pyplot as plt

# Filters params
sampling = 2000     # sampling frequency in Hz
cutoff = 300        # cutoff frequency in Hz
df = 20             # transition band width in Hz
A = 150             # max dB attenuation

# Weighting factor
K = 5


# pass-band and stop-band frequencies
fp = (cutoff-df/2)
fs = (cutoff+df/2)

# filter length estimation using the Fred Harris rule of thumb
if A <= 60:
    N = round((sampling / (fs - fp)) * (abs(A) / 22) * 1.1)
elif A > 60 and A <= 80:
    N = round((sampling / (fs - fp)) * (abs(A) / 22) * 1.25)
elif A > 80 and A <= 150:
    N = round((sampling / (fs - fp)) * (abs(A) / 22) * 1.4)
elif A > 150:
    if A <= 160:
        N = round((sampling / (fs - fp)) * (abs(A) / 22) * 1.52)
    else:
        A = 160
        N = round((sampling / (fs - fp)) * (abs(A) / 22) * 1.6)

if N % 2 == 0:
    N += 1
M = (N - 1) // 2

# normalize fp and fs
fp = fp / (sampling / 2)
fs = fs / (sampling / 2)

# construct q(k)
x1 = np.array([fp + K * (1 - fs)])
x2 = fp * np.sinc(fp * np.arange(1, 2 * M+1)) - K * fs * np.sinc(fs * np.arange(1, 2 * M + 1))
q = np.concatenate((x1, x2))

# construct Q1, Q2, Q
Q1 = toeplitz(q[0:M+1])
Q2 = hankel(q[:M + 1], q[M:2 * M + 1])
Q = (Q1 + Q2) / 2

# construct b
b = fp * np.sinc(fp * np.arange(M + 1))

# solve linear system to get a(n)
a = np.linalg.solve(Q, b)

# form impulse response h(n)
h = np.concatenate([a[M:0:-1], 2 * a[0] * np.ones(1), a[1:M + 1]]) / 2



for i in h:
    print(f"{i}, ")

print(f"Number of coefficients = {N}")


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
n_fft = 2048*2  # Increase the resolution of the frequency bins
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
