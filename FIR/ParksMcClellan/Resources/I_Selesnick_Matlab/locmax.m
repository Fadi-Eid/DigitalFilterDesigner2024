function maxind = locmax(x)
% function maxind = locmax(x)
% finds indices of local maxima of data x

x = x(:);
n = length(x);
maxind = find(x > [x(1)-1;x(1:n-1)] & x > [x(2:n);x(n)-1]);

