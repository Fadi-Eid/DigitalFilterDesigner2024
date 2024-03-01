% Desired filter length
  N = 203;
  % pass-band and stop-band weights
  Kp = 1; Ks = 2;
  % band-edges and cutoff frequency
  wp = 0.3*pi;  ws = 0.4*pi; wo = 0.35*pi;
  % grid size to discretize the frequency axis
  L = 2000;
  % discretize the frequency axis (0 to pi)
  w = [0:L]*pi/L;
  % compute the weight function
  W = Kp*(w<=wp) + Ks*(w>=ws);
  % select the desired response
  D = (w<=wo);
  % call the function to compute filter's coefficients
  h = fircheb(N,D,W);