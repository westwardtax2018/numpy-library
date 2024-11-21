# statements to copy and paste into ICE11_1

if __name__ == "__main__":   # if run from command prompt
    # get temperature, `T`, from command line and compute
    import sys
    T = float(sys.argv[1])   # convert string to float
    mu = calc_viscosity(T)   # compute viscosity
    print(mu)                # output value to screen
