import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator   # for comparison
import time # to measure execution time

# Lagrange interpolation using the barycentric form
# reference: https://acme.byu.edu/00000179-afb2-d74f-a3ff-bfbb158d0001/polynomialinterpolation19-pdf
# reference: https://people.maths.ox.ac.uk/trefethen/barycentric.pdf

# say you have a set of data points (xi, yi) where i = 0, 1,...n (n+1 points)
# first you call the function weights(xi) and you store the output wi in your program
# having xi, yi and wi stored, you can call the lagrange(xi, yi, wi, x) which will evaluate
# and return y at the given x.
def func(x):
    d = 2 * np.sin(x) * np.cos(4*np.pi*x)
    return d

def weights(xi):
    n = len(xi)
    wi = np.ones(n)

    # compute the interpolation interval
    C = (np.max(xi) - np.min(xi)) / 4

    shuffle = np.random.permutation(n-1)
    for j in range(n):
        temp = (xi[j] - np.delete(xi, j)) / C
        temp = temp[shuffle] # Randomize order of product.
        wi[j] /= np.product(temp)

    return wi

def lagrange(xi, yi, wi, x):
    if np.isin(x, xi):
        index = np.where(xi == x)[0]
        return xi[index[0]]

    n = len(xi)
    den = 0     # denominator of p_x
    num = 0     # numerator of p_x
    for j in range(n):
        num = num + (wi[j] * yi[j])/ (x - xi[j]) 
        den = den + wi[j] / (x - xi[j])
    return num / den


# Example usage:

# data points to be interpolated
n = 400    # number of data point (polynomial degree = n - 1)
xi = np.linspace(0.001, 10, n)
yi = func(xi)

start_time = time.time()
# store the weights
wi = weights(xi)

# evaluate a set of x using the lagrange polynomial
N = 2000        # number of values to evaluate the approximation
p = np.zeros(N) # array that will store the approximated values
x = np.linspace(3, 6.2, N)    # set of points to evaluate p at

for i in range(N):
    p[i] = lagrange(xi, yi, wi, x[i])

end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time, "seconds")

P = BarycentricInterpolator(xi, yi)

# Plotting
plt.figure(figsize=(10, 6))  # Adjust the figure size if necessary

# Plot data points
plt.scatter(xi, yi, color='red', label='Data points')

# Plot my method interpolation
plt.plot(x, p+0.09, 'green', label='Direct implementation')

# Plot Scipy's method
plt.plot(x, P(x)-0.09, color='blue', label="Scipy's implementation")

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Interpolation Comparison')

# Add legend
plt.legend()

# Show plot
plt.ylim(-5, 5)
plt.grid(True)  # Optionally add grid
plt.show()

