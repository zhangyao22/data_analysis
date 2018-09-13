# _*_ coding: utf-8 _*_
__author__ = 'zhangyao'
__date__ = '2018/9/13 11:28'

# import matplotlib as plt
from matplotlib import pyplot as plt
import numpy as np


# https://blog.csdn.net/cymy001/article/details/78344316详解
x = np.linspace(-3, 3, 50)
y = 2*x + 1
plt.figure(figsize=(8, 5),)

plt.plot(x, y,)

# 获取坐标轴
ax = plt.gca()

# spines移动坐标轴
# 绘制的图片有四个边框,需要处理掉两个
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 移动下边边框线，相当于移动x轴
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 移动左边边框线，相当于移动y轴
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# 散点图放大当前点
plt.scatter([x0, ], [y0, ], s=50, color='r')

# 对图上的某个点加注解
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# 设置图片上的文字描述和注解
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 15, 'color': 'r'})

# 网格
plt.grid(True)

plt.show()