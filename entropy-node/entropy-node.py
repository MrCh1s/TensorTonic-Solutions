import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    y = np.array(y, dtype = float)
    if len(y) == 0: return 0.0
    _, counts = np.unique(y, return_counts = True)
    props = counts / len(y)
    H = -np.sum(props * np.log2(props))
    return float(H)
    pass