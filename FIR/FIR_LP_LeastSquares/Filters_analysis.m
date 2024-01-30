% Main variables
fs = 2000;      % Sampling rate
Ts = 1/fs;      % Sampling period
N = length(h1);  % filter length
lpad = 2048;    % do not change

% create the time vector
t = 0:Ts:(N-1)*Ts;

% plot the impulse response of the filter
figure
stem(t, h1, 'b', 'LineWidth', 1); % Blue stems for impulse response
hold on
stem(t, h2, 'r', 'LineWidth', 1); % Blue stems for impulse response
hold off
grid on
legend('h1[n]', 'h2[n]');
xlabel('Time (s)');
ylabel('Amplitude');
title('Impulse Response of the Filter');

% compute the frequency response and the frequency axis
% Frequency axis
f = (0:lpad/2)*(fs/lpad);
% Frequency response
H1 = fft(h1, lpad);
H1 = H1(1:lpad/2+1);
H2 = fft(h2, lpad);
H2 = H2(1:lpad/2+1);

% plot the frequency response (linear)
figure
subplot(2, 1, 1)
plot(f, abs(H1)', 'b', 'LineWidth', 1);
hold on
plot(f, abs(H2)', 'r', 'LineWidth', 1);
hold off
grid on
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Linear Frequency Response');
ylim([-0.1, 1.1]);
legend('H1', 'H2');

% plot the frequency response (logarithmic)
subplot(2, 1, 2)
plot(f, 20*log10(abs(H1)), 'b', 'LineWidth', 1);
hold on
plot(f, 20*log10(abs(H2)), 'r', 'LineWidth', 1);
hold off
grid on
xlabel('Frequency (Hz)');
ylabel('Magnitude (dB)');
title('Logarithmic Frequency Response');
ylim([-140, 10]);
legend('H1', 'H2');