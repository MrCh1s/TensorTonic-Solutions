import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype = float)
    p = np.array(p, dtype = float)
    if x.shape != p.shape:
        raise ValueError("Kích thước của các giá trị (x) và xác suất (p) phải giống nhau.")
    if not np.allclose(np.sum(p), 1.0, atol = 1e-6):
        raise ValueError("Tổng các xác suất phải bằng 1.")
    expected_value = np.sum(x * p)
    return expected_value
    pass
