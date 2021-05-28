import operator

from matplotlib import pyplot as plt

# 绘制销量范围柱状图 筛选世界销量最多的十款游戏

x = ["0-50w", "50-100w", "100-500w", "500-1000w", "1000w+"]
y = [0, 0, 0, 0, 0]
sales = ""
# 从文件读取数据并保存
with open("C:/Users/DXY/Desktop/大数据/Game/Sales/part-r-00000", "r") as f:
    for line in f:
        # 切割数据
        _l = line.split("\t")
        # 匹配销量数据
        if _l[0] == "0.5":
            y[0] = int(_l[1][:len(_l[1]) - 1])
        elif _l[0] == "1":
            y[1] = int(_l[1][:len(_l[1]) - 1])
        elif _l[0] == "5":
            y[2] = int(_l[1][:len(_l[1]) - 1])
        elif _l[0] == "10":
            y[3] = int(_l[1][:len(_l[1]) - 1])
        elif _l[0] == "10+":
            y[4] = int(_l[1][:len(_l[1]) - 1])
        else:
            # 销量排行
            sales = _l[1][:len(_l[1]) - 1]

# 设置字体
plt.rcParams['font.family'] = ['SimHei']
plt.figure(figsize=(10, 5), dpi=300)

# 画条形图
plt.bar(range(len(x)), y, width=0.5, bottom=0)
# width:条形图宽度
# bottom y的最小值从什么时候开始

# 每个点标识
for a, b in zip(range(len(x)), y):
    plt.text(a, b + 1, b, ha='center', va='center', fontdict={"fontsize": 12})

# 修改x轴刻度
plt.xticks(range(len(x)), x, fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("销量", fontsize=15)
plt.ylabel("数量", fontsize=15)
plt.title("1980-2016年游戏销量数量分类柱状图", fontsize=20)
plt.savefig('C:/Users/DXY/Desktop/大数据/Sales.png')
plt.show()

# 处理排行数据
# 切割元素
eArr = sales.split(";")
eMap = {}
for e in eArr:
    if e == "":
        continue
    _e = e.split(",")
    eMap[_e[0]] = float(_e[1])
# 排序dict，然后取出前20个
sortedList = sorted(eMap.items(), key=operator.itemgetter(1), reverse=True)

x = []
y = []
for (k, v) in sortedList[0:20]:
    x.append(k)
    y.append(v)

# 设置字体
plt.figure(figsize=(20, 18), dpi=300)

# 画条形图
plt.bar(range(len(x)), y, width=0.5, bottom=0)
# width:条形图宽度
# bottom y的最小值从什么时候开始

# 每个点标识
for a, b in zip(range(len(x)), y):
    plt.text(a, b + 1, b, ha='center', va='center', fontdict={"fontsize": 9})

# 修改x轴刻度
plt.xticks(range(len(x)), x, rotation=70, fontsize=5)
plt.yticks(fontsize=10)
plt.xlabel("游戏名称", fontsize=20)
plt.ylabel("销量", fontsize=20)
plt.title("1980-2016年游戏销量top20", fontsize=20)
plt.savefig('C:/Users/DXY/Desktop/大数据/Top20.png')
plt.show()
