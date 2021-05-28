from matplotlib import pyplot as plt

# 绘制年份增长折线图

x = range(1980, 2017, 1)
y = []
# 从文件读取数据并保存
with open("C:/Users/DXY/Desktop/大数据/Game/YearOfRelease/part-r-00000", "r") as f:
    for line in f:
        # 切割数据
        _l = line.split("\t")
        _y = int(_l[1][:len(_l[1]) - 1])
        _x = _l[0]
        if int(_x) > 2016:
            break
        y.append(_y)

# 设置字体
plt.rcParams['font.family'] = ['SimHei']

plt.figure(figsize=(15, 8), dpi=300, facecolor='w')
# 修改y轴刻度
plt.yticks(range(0, 1600, 100), fontsize=20)
plt.xticks(fontsize=20)

# 每个点标识
for a, b in zip(x, y):
    plt.text(a, b + 5, b, ha='center', va='center', fontdict={"fontsize": 10})

plt.title("1980-2016年主机游戏发行数", fontsize=20)
plt.xlabel("年份", fontsize=20)
plt.ylabel("数量", fontsize=20)
plt.plot(x, y)
plt.savefig('C:/Users/DXY/Desktop/大数据/YearOfRelease.png')
plt.show()
