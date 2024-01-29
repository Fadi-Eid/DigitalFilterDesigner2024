# Weighted square error -> low-pass -> Numerical solution
# For reference see: LINEAR-PHASE FIR FILTER DESIGN BY LEAST SQUARES
# by I. Selesnick EL 713 Lecture Notes, page 11-15
# A straight line transition function gives poor results compared to
# the adjustable Kaiser window. A pth order spline will be implemented
# improves the response but is outperformed by the Kaiser.
# The numerical approach should be implemented (a = inv(Q).a) -> page 16
import numpy as np
import matplotlib.pyplot as plt
import math


