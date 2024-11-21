# describe this module with a docstring

import numpy as np

def midpoint(fvals, dx):
    # Your `midpoint` docstring goes here.  Based on the in-class exercise
    # description and in your own words
    #    - explain what `fvals` is
    #    - explain what `dx` is

    # Check that `dx` is positive; if it is not, raise a ValueError

    # compute the midpoint-rule approximation to
    # an integral based on the values in `fvals`.

    # the summation sign in the formula on page 5 should suggest a loop;
    # alternatively, look up NumPy function np.sum and see if that can
    # make your code easier to read and understand.

    return ???

Submitty = True
if not Submitty:
    # The following computes the midpoint error for exp(x) for a range of dx
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
        x_lo = 0.0
        x_hi = 1.0
        dx   = (x_hi - x_lo) / (n-1)
        nodes = np.linspace(x_lo, x_hi, n)   # what does this do?
        mdpts = nodes[0:n-1] + dx/2.0        # what does this do?
        fvals = np.exp(mdpts)                # what does this do?
        integral = midpoint(fvals, dx)

        exact    = np.exp(1.0) - 1.0
        error    = integral - exact
        result_string  = "Error for " + '{:5d}'.format(n)
        result_string += " nodes = "  + '{:.10f}'.format(error)
        print(result_string)

# add a test that uses np.sin(2*pi*x)
# add a test that uses np.sqrt(x)
