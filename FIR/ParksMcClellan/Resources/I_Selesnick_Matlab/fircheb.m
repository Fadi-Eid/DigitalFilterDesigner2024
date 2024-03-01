function [h,del] = fircheb(N,D,W)
% subprograms: locmax.m, etap.m

% convert the arguments to column vector regardless of the shape
W = W(:);
D = D(:);
% get the grid size - 1 --> (0 -> L) = grid size
L = length(W)-1;

SN = 1e-8;               % small number for stopping criteria, etc
M = (N-1)/2;
R = M + 2;               % R = size of reference set

% initialize reference set (approx equally spaced where W>0) 
f = find(W>SN); % find the indices of W where W > 0
% initial reference set (indices)
k = f(round(linspace(1,length(f),R)));

w = [0:L]'*pi/L;
m = 0:M;
s = (-1).^(1:R)';        % signs

while 1
   % --------------- Solve Interpolation Problem ---------------------
   x = [cos(w(k)*m), s./W(k)] \ D(k);
   a = x(1:M+1);		% cosine coefficients
   del = x(M+2);		% delta
   % get the impulse response from the a(n)
   h = [a(M+1:-1:2); 2*a(1); a(2:M+1)]/2;
   % generated amplitude response
   A = firamp(h,1,L)';
   plot(w, A)
   hold on
   plot(w, D)
   hold off
   % compute the error function
   err = (A-D).*W;		% weighted error2
   figure
   plot(w, err)

   % --------------- Update Reference Set ----------------------------
   % find the extremas
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
