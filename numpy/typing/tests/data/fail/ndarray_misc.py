"""
Tests for miscellaneous (non-magic) ``np.ndarray``/``np.generic`` methods.

More extensive tests are performed for the methods'
function-based counterpart in `../from_numeric.py`.

"""

from typing import Any
import numpy as np

f8: np.float64
AR_f8: np.ndarray[Any, np.dtype[np.float64]]
AR_M: np.ndarray[Any, np.dtype[np.datetime64]]
AR_b: np.ndarray[Any, np.dtype[np.bool_]]

f8.argpartition(0)  # E: has no attribute
f8.diagonal()  # E: has no attribute
f8.dot(1)  # E: has no attribute
f8.nonzero()  # E: has no attribute
f8.partition(0)  # E: has no attribute
f8.put(0, 2)  # E: has no attribute
f8.setfield(2, np.float64)  # E: has no attribute
f8.sort()  # E: has no attribute
f8.trace()  # E: has no attribute

AR_M.__int__()  # E: Invalid self argument
AR_M.__float__()  # E: Invalid self argument
AR_M.__complex__()  # E: Invalid self argument
AR_b.__index__()  # E: Invalid self argument
