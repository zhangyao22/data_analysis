from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows下使用matplotlib.rc可以修改设置中文字体
# mac，linux下使用matplotlib下的font_manager这只中文字体

# 中文字体名称不好记或者不清楚
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示坐标轴负号
# #有中文出现的情况，需要u'内容'

# font = {
#     'family' : 'SimHei',
#     'weight' : 'bold',
#     'size'   : '10'
# }
# matplotlib.rc('font', **font)

# 这个是多个操作系统通用的  C:\Windows\Fonts\simfang.ttf在windows下搜索字体，在查看字体的具体路径
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simfang.ttf')

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8), dpi=80)

xtick_lables = [ "10:{}".format(i) if i>9 else "10:0"+str(i) for i in range(60) ]

xtick_lables += [ "11点{}".format(i) if i>9 else "11:0"+str(i) for i in range(60) ]
# xtick_lables += [ "11:{}".format(i) for i in range(60) ]

# 当x轴字符串表示刻度，xtick_lables保持与list(x)一样的步长则会代替前面的刻度，rotation表示轴刻度旋转度数
# 中文字符在x周不显示，需要处理
plt.xticks(list(x)[::5], xtick_lables[::5], rotation=45, fontproperties=my_font)
plt.yticks(y)
plt.plot(x, y, label='温度', c="blue", linestyle="--", linewidth=2, alpha=0.5)
plt.plot(x, [i+1 for i in y], label="温度+", c="red")

# 添加轴描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位℃", fontproperties=my_font)
plt.title("10点到12点的气温变化情况", fontproperties=my_font)

#  添加网格,alpha透明度
# plt.grid(axis='x', color='b', linestyle='-')
plt.grid(linestyle='-')

# 添加图例,显示中文特殊的参数调用,图例显示位置，默认是best最合适的
plt.legend(prop=my_font, loc="upper left")
plt.xlim((1,50))
plt.show()