% WEIGHTED LEAST SQUARE LOWPASS FILTER
A = 62;        % stop band attenuation in dB
wp = 0.26*pi;   % pass-band
ws = 0.34*pi;   % stop band
fs = 2*pi;    % sampling frequency

% filter length estimation using the fred harris rule of thumb
if A <= 60
    N = round((fs/(ws-wp))*(abs(A)/22)*1.1);
end
if A > 60 && A <= 80
    N = round((fs/(ws-wp))*(abs(A)/22)*1.25);
end
if A > 80 && A <= 150
    N = round((fs/(ws-wp))*(abs(A)/22)*1.4);
end
if A > 150
    if A <= 160
        N = round((fs/(ws-wp))*(abs(A)/22)*1.52);
    else
        A = 160;
        N = round((fs/(ws-wp))*(abs(A)/22)*1.6);
    end
end



if mod(N, 2) == 0
    N = N+1;
end
M = (N-1)/2;
% set band-edges and stop-band weighting
K = 5;
% normalize band-edges for convenience
fp = wp/pi;
fs = ws/pi;
% construct q(k)
q = [fp+K*(1-fs), fp*sinc(fp*[1:2*M])-K*fs*sinc(fs*[1:2*M])];
% construct Q1, Q2, Q
Q1 = toeplitz(q([0:M]+1));
Q2 = hankel(q([0:M]+1),q([M:2*M]+1));
Q = (Q1 + Q2)/2;
% construct b
b = fp*sinc(fp*[0:M]');
% solve linear system to get a(n)
a = Q\b;
% form impulse response h(n)
h = [a(M+1:-1:2); 2*a(1); a(2:M+1)]/2;
