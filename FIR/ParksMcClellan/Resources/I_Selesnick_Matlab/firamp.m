function [A,w] = firamp(h,type,L)
% [A,w] = firamp(h,type,L)
% Amplitude response of a linear-phase FIR filters
% A : amplitude response
% w : frequency grid [0:L]*pi/L
% h : impulse response
% type : [1,2,3,4]
% L : frequency density (optional, default = 2^10)

h = h(:)';		% make h a row vector
N = length(h);		% length of h
if nargin < 3
	L = 2^10;	% grid size
end
H = fft(h,2*L);		% zero pad and fft
H = H(1:L+1);		% select [0,pi]
w = [0:L]*pi/L;		% frequency grid
M = (N-1)/2;		
if (type == 1)|(type == 2)
  H = exp(M*j*w).*H;	% Type I and II
else
  H = -j*exp(M*j*w).*H;	% Type III and IV
end
A = real(H);		% discard zero imaginary part


