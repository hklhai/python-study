# -*- coding: utf-8 -*-

"""
import os  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error   
"""
import tensorflow as tf
v = tf.Variable([1, 2])
c = tf.constant([3, 3])
sub = tf.subtract(v, c)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
