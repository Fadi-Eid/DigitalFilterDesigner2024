function v = etap(E)
%
% v = etap(E);
% Ensuring The Alternation Property
% E : error vector
% v : index of original E

if size(E,1) > 1
   a = 1;
else
   a = 0;
end
j = 1;
xe = E(1);
xv = 1;
for k = 2:length(E)
   if sign(E(k)) == sign(xe)
      if abs(E(k)) > abs(xe)
         xe = E(k);
         xv = k;
      end
   else
      v(j) = xv;
      j = j + 1;
      xe = E(k);
      xv = k;
   end
end
v(j) = xv;
if a == 1
   v = v(:);
end

