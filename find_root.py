# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:19:31 2024

@author: banerm
"""
        
def bisection(func, xlow, xupp, xtol = 1e-7, ftol = 1e-12, maxiter = 100):
    """
    

    Parameters
    ----------
    func : TYPE
        DESCRIPTION.
    xlow : TYPE
        DESCRIPTION.
    xupp : TYPE
        DESCRIPTION.
    xtol : TYPE, optional
        DESCRIPTION. The default is 1e-7.
    ftol : TYPE, optional
        DESCRIPTION. The default is 1e-12.
    maxiter : TYPE, optional
        DESCRIPTION. The default is 100.

    Returns
    -------
    xmid : TYPE
        DESCRIPTION.

    """
    iter = 0  
    xmid = (1/2)*(xlow+xupp)
    while (abs(xupp - xlow) > xtol or abs(func(xmid)) > ftol) and iter < maxiter:
        iter += 1
      
        if (func(xlow)*func(xmid) < 0.0):
            xupp = xmid
        elif (func(xlow)*func(xmid) > 0.0):
            xlow = xmid
        else: #func(xlow)*func(xmid) == 0.0:
            break
        xmid = (1/2)*(xlow+xupp)
    return xmid


def newton(func, x0, ftol=1e-12, xtola=1e-7, maxiter=100):
    iter = 0
    f_k, df_k = func(x0)

    # Check if initial guess is already a root
    if abs(f_k) < ftol:
        return x0, iter

    delx = 1.0
    x_k = x0

    while (abs(delx) > xtola and abs(f_k) > ftol) and iter < maxiter:
        iter += 1

        try:
            if df_k == 0:
                raise ZeroDivisionError("Derivative is zero.")
            delx = -(f_k / df_k)  # Compute the change
        except ZeroDivisionError:
            return x_k, -iter  # Return current estimate and negative iteration count

        x_k += delx  
        f_k, df_k = func(x_k)  # Update function and derivative values

    return x_k, iter  # Return the root estimate and the number of iterations
