% filter length
N = 105;
M = (N-1)/2;
p = 3;      % order of the spline
% set parameters
wp = 0.27*pi;
ws = 0.32*pi;
wo = (ws+wp)/2;
Del = (ws-wp)/p;
fo = wo/pi;
Df = Del/pi;
% form impulse response h(n)
n = 0:N-1;
h1 = fo * sinc(fo*(M-n)) .* (sinc(Df*(M-n)).^p);
h1 = h1';