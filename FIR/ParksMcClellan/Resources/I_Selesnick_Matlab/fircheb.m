function [h,del] = fircheb(N,D,W)
% h = fircheb(N,D,W)
% weighted Chebyshev design of Type I FIR filters
%
%   h : length-N impulse response
%   N : length of filter (odd)
%   D : ideal response   (uniform grid)
%   W : weight function  (uniform grid)
%   need: length(D) == length(W)
%
% % Example
%   N = 31;  Kp = 1; Ks = 4;  
%   wp = 0.26*pi;  ws = 0.34*pi; wo = 0.3*pi;
%   L = 1000;
%   w = [0:L]*pi/L;
%   W = Kp*(w<=wp) + Ks*(w>=ws);
%   D = (w<=wo);
%   h = fircheb(N,D,W);

% subprograms: locmax.m, etap.m

W = W(:);
D = D(:);
L = length(W)-1;

SN = 1e-8;               % small number for stopping criteria, etc
M = (N-1)/2;
R = M + 2;               % R = size of reference set

% initialize reference set (approx equally spaced where W>0) 
f = find(W>SN);
k = f(round(linspace(1,length(f),R)));

w = [0:L]'*pi/L;
m = 0:M;
s = (-1).^(1:R)';        % signs

while 1
   % --------------- Solve Interpolation Problem ---------------------
   x = [cos(w(k)*m), s./W(k)] \ D(k);
   a = x(1:M+1);		% cosine coefficients
   del = x(M+2);		% delta
   h = [a(M+1:-1:2); 2*a(1); a(2:M+1)]/2;
   A = firamp(h,1,L)';
   err = (A-D).*W;		% weighted error

   % --------------- Update Reference Set ----------------------------
   newk = sort([locmax(err); locmax(-err)]);  
   errk = (A(newk)-D(newk)).*W(newk);         

   % remove frequencies where the weighted error is less than delta
   v = abs(errk) >= (abs(del)-SN);
   newk = newk(v);
   errk = errk(v);

   % ensure the alternation property
   v = etap(errk);	
   newk = newk(v);
   errk = errk(v);

   % if newk is too large, remove points until size is correct  
   while length(newk) > R
      if abs(errk(1)) < abs(errk(length(newk)))
         newk(1) = [];
      else
         newk(length(newk)) = [];
      end
   end

   % --------------- Check Convergence -------------------------------
   if (max(errk)-abs(del))/abs(del) < SN
      disp('I have converged.')
      break 
   end 
   k = newk;
end

del = abs(del);
h = [a(M+1:-1:2); 2*a(1); a(2:M+1)]/2;
