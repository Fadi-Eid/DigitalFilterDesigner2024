
% Main variables
fs = 2000;      % Sampling rate
Ts = 1/fs;      % Sampling period
N = length(h);  % filter length

% create the time vector
t = 0:Ts:(N-1)*Ts;

% plot the impulse response of the filter
subplot(3, 1, 1)
plot(t, h);
grid on

% compute the frequency response
H = fft(h);
% create the frequency vector
f = 0:fs/N:fs-fs/N;

% cut the response in half (0 to nyquist frequency)
f = f(1:(N-1)/2);
H = H(1:(N-1)/2);

% plot the linear amplitude response
subplot(3, 1, 2);
plot(f, abs(H));
ylim([-0.1, 1.1]);

grid on

% plot the logarithmic amplitude response
subplot(3, 1, 3);
plot(f, 20*log10(abs(H)));
ylim([-80, 10]);
grid on

% create a sine wave
t = 0:Ts:1;
x = sin(10*pi*t);
% filter the signal
x_filtered = conv(x, h);

figure;
plot(t, x);
legend('original')
hold on
plot(t, x_filtered(1:length(t)))
legend('filtered')
grid on
legend on
