import tensorflow as tf
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/core/ops/libcomplextf.so'
_complex_tf_lib = tf.load_op_library(path)
zero_out = _complex_tf_lib.zero_out
