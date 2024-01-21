% Main variables
fs = 2000;      % Sampling rate
Ts = 1/fs;      % Sampling period
N = length(h);  % filter length
lpad = 2048;    % do not change

% create the time vector
t = 0:Ts:(N-1)*Ts;

% plot the impulse response of the filter
subplot(3, 1, 1)
stem(t, h, 'b', 'LineWidth', 1); % Blue stems for impulse response
grid on
xlabel('Time (s)');
ylabel('Amplitude');
title('Impulse Response of the Filter');

% compute the frequency response and the frequency axis
% Frequency axis
f = (0:lpad/2)*(fs/lpad);
% Frequency response
H = fft(h, lpad);
H = H(1:lpad/2+1);

% plot the frequency response (linear)
subplot(3, 1, 2)
plot(f, abs(H), 'r', 'LineWidth', 1); % Red line for linear frequency response
grid on
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Linear Frequency Response');
legend('Filter Response');
ylim([-0.1, 1.1]);

% plot the frequency response (logarithmic)
subplot(3, 1, 3)
plot(f, 20*log10(abs(H)), 'g', 'LineWidth', 1); % Green line for logarithmic frequency response
grid on
xlabel('Frequency (Hz)');
ylabel('Magnitude (dB)');
title('Logarithmic Frequency Response');
legend('Filter Response');
ylim([-140, 10]);