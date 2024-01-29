import numpy as np
from scipy.linalg import toeplitz
from scipy.linalg import hankel

# WEIGHTED LEAST SQUARE LOWPASS FILTER
A = 30  # stop band attenuation in dB
wp = 0.26 * np.pi  # pass-band
ws = 0.34 * np.pi  # stop band
fs = 2 * np.pi  # sampling frequency

# filter length estimation using the fred harris rule of thumb
if A <= 60:
    N = round((fs / (ws - wp)) * (abs(A) / 22) * 1.1)
elif A > 60 and A <= 80:
    N = round((fs / (ws - wp)) * (abs(A) / 22) * 1.25)
elif A > 80 and A <= 150:
    N = round((fs / (ws - wp)) * (abs(A) / 22) * 1.4)
elif A > 150:
    if A <= 160:
        N = round((fs / (ws - wp)) * (abs(A) / 22) * 1.52)
    else:
        A = 160
        N = round((fs / (ws - wp)) * (abs(A) / 22) * 1.6)

if N % 2 == 0:
    N += 1
M = (N - 1) // 2

# set band-edges and stop-band weighting
K = 5
# normalize band-edges for convenience
fp = wp / np.pi
fs = ws / np.pi

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
