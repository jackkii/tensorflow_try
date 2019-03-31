# Try_session.py
# ------------------------
# 使用会话来执行图中的op来提供数据和获得结果
# ------------------------
# Jackkii    2019/03/31

import tensorflow as tf
# 一般要加 import numpy as np
# 一般要加 import matplotlib.pyplot as plt

# 建立计算图只是建立静态计算模型，
# 增加的op, Tensor对象自动放在数据流图中
node1 = tf.constant(3.0, tf.float32, name="node1")
node2 = tf.constant(4.0, tf.float32, name="node2")
node3 = tf.add(node1, node2)
print(node3)

'''
# 使用会话来执行图中的op来提供数据和获得结果
sess = tf.Session()

# 显示运行结果
print(sess.run(node1))
print(sess.run(node2))
print(sess.run(node3))

# 关闭session
sess.close()
'''

# 也可将19行到27行换成
with tf.Session() as sess:
    print(sess.run(node3))

# 使用with代码自动完成关闭动作, 即通过上下文管理器来管理这个会话
# 当上下文退出时, 会话关闭, 资源释放完成

sess = tf.Session()
# 33行等价于(必须先指定会话，即sess = tf.Session())
with sess.as_default():
    print(node3.eval())

# 33，39行等价于(必须先指定会话，即sess = tf.Session())
print(node3.eval(session=sess))
