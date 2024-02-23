% Example (N=201 works)
sampling = 10000;
cutoff = 2500;
transition = 0.05;
N = 4003;  
Kp = 1; Ks = 2;  

wo = (cutoff*pi)/(sampling/2);
wp = wo - ((transition/2)*pi)/(sampling/2);
ws = wo + ((transition/2)*pi)/(sampling/2);

% wp = 0.30*pi;  ws = 0.34*pi; wo = 0.3*pi; % figures_01
% wp = 0.28*pi;  ws = 0.34*pi; wo = 0.3*pi; % figures_02
% wp = 0.27*pi;  ws = 0.34*pi; wo = 0.3*pi; % figures_03

L = 2000;
w = [0:L]*pi/L;
W = Kp*(w<=wp) + Ks*(w>=ws);
D = (w<=wo);
h = fircheb(N,D,W);

% plot the response
lpad = N*4;
f = 0:sampling/lpad:sampling-sampling/lpad;
H = fft(h, lpad);
plot(f(1:end/2), 20*log10(abs(H(1:end/2))))
grid on

