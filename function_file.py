import numpy as np
from scipy import stats
#Calculate mean
def func_mean(arr):
    return np.mean(arr)

#Calculate mode
def func_mode(arr):
    return stats.mode(arr)

#Calculate median
def func_median(arr):
    return np.median(arr)

#Calculate percentile
def func_percentile(arr, p):
    return np.percentile(arr, p)



