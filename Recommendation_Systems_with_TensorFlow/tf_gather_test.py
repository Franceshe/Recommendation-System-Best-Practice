import os
import numpy as np
#import tensorflow.compat.v1 as tf
import tensorflow as tf

print(tf.__version__)
# solve bug: https://stackoverflow.com/questions/64450037/tensorflow-binary-is-optimized-to-use-the-following-cpu-instructions-in-performa
# Just disables the warning, doesn't enable AVX/FMA

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Collecting elements from a tensor of rank 2
# data is [[0, 1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 10, 11],
#          [12 13 14 15 16 17],
#          [18 19 20 21 22 23],
#          [24, 25, 26, 27, 28, 29]]
data = np.reshape(np.arange(30), [5, 6])
x = tf.constant(data)
result = tf.gather_nd(x, [1, 2])
print(result)
