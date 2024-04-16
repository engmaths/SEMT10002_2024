"""
The code below now works correctly; the fixes that are needed
can be found below in the doc strings.  The code still uses
global variables. Can you modify the code to eliminate the
use of global variables?
"""

from math import *

# Define the parameters in the problem
alpha = 10

"""
The original value of mu is incorrect. We comment out the
incorrect value and add the correct comment below.
"""
# mu = 1.5
mu = 1

a = 1
b = 3

N = 10

"""
The original code also defined dx here. This turns dx into a
global variable so it can be used in the integral function below.
However, when N is updated in the for loop below, the value of
dx is not updated. Therefore, defining dx as a global variable
here was incorrect. We comment this code out and define dx
in the integrate function below
"""
# dx = (b - a) / N

# Define the mathematical function to compute the area of
def f(x):

    """
    By defining mu and alpha in the main body of the Python code,
    there are global variables so they do not need to be
    redefined as global variables here. So we comment out the
    code in the original file.
    """

    # global mu, alpha
    # alpha = 10
    # mu = 1.0
    
    # return the value of the function
    return alpha * exp(-mu * x)


# Define and print exact value of the area for comparison
A_exact = alpha / mu * (exp(-mu * a) - exp(-mu * b))
print('The exact area is', A_exact)


# Define a Python function to approximate the area using
# the trapezium rule
def integrate(N):

    dx = (b - a) / N

    # initialise the area under the curve
    A = 1/2 * (f(a) + f(b)) * dx

    # compute the sum in the formula
    for i in range(1, N):
        x_i = a + i * dx
        A += f(x_i) * dx
        
    # return the result
    return A


# Use a loop to compute the integrals for different
# values of N (number of trapezoids)

N_list = [2**n for n in range(2, 7)]
A_list = []

for n, N in enumerate(N_list):
    A_list.append(integrate(N))
    print('The area when N =', N, 'is:', A_list[n])

