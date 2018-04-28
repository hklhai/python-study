# -*- coding: utf-8 -*-
import tensorflow as tf

"""
import os  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error   
"""

v = tf.Variable([1, 2])
c = tf.constant([3, 3])
# 减法op
sub = tf.subtract(v, c)
# 加法op
add = tf.add(sub, v)

# 变量需要初始化操作
init = tf.global_variables_initializer()

# Session()后的括号不能省
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))
