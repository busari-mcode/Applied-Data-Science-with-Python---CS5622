import numpy as np

np.random.seed(12)
ary6 = np.random.rand(4, 5)

min_indices = np.argmin(ary6, axis=0).astype(np.int64)
print(repr(min_indices))
