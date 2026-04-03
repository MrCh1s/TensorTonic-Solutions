import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pass
    x = np.array(x)

    pmf = np.where(x, p, 1 - p)
    mean = float(p)
    var = float(p * (1 - p))
    return pmf, mean, var
    