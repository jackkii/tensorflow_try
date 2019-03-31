# Try_scatter.py
# ------------------------
# 画散点图初体验
# ------------------------
# Jackkii    2019/03/31

import tensorflow as tf
# 一般要加 import numpy as np
import matplotlib.pyplot as plt

# 在浏览器中显示matplotlib图像（jupyter中要加）
# %matplotlib inline

# 定义2*20随机数矩阵
a = tf.random_normal([2, 20])

# 启动一个tensorflow会话
sess = tf.Session()

# 在sess会话里执行a， 结果放在out中
out = sess.run(a)
x, y = out

# 用pyplot创建一系列散点
plt.scatter(x, y)
plt.show()
# 若在jupyter中则不需show()(也可用),可换成12行
