# do you need to update your module docstring, or is what you wrote
# before sufficiently generic to include the new `trapazoidal` function?

import numpy as np

# cut and paste your `midpoint` function here

def trapezoidal(fvals, dx):
    # write a standard-conforming useful docstring for this function
    # based on the in-class exercise description and in your own words
    #    - explain what `fvals` is (this is different from midpoint!)
    #    - explain what `dx` is

    # Check that `dx` is positive; if it is not, raise a ValueError

    # implement the formula on Preliminaries page 14
    # Note that `fvals` is an array
    #   - with first element fvals[0]
    #   - and last element fvals[-1]
    # How can you write a slice of array `fvals` that includes
    # all of the points except the two end points?
    # Note that you can use np.sum on that slice if you want.

    return ???

# Cut and paste your `midpoint` testing here, except...
#    how does it need to change to test `trapezoidal`?

