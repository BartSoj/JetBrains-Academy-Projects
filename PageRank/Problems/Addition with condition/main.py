import numpy as np


def custom_sum(arg1, arg2):
    return arg1 + arg2 if isinstance(arg1, np.ndarray) and isinstance(arg2, np.ndarray) else \
        "One argument is a list" if type(arg1) != type(arg2) else "Both arguments are lists, not arrays"
