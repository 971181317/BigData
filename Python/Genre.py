from matplotlib import pyplot as plt

# 绘制游戏类型饼状图

labels = []
sizes = []
# 从文件读取数据并保存
with open("C:/Users/DXY/Desktop/大数据/Game/Genre/part-r-00000", "r") as f:
    for line in f:
        # 切割数据
        _l = line.split("\t")
        labels.append(_l[0])
        sizes.append(int(_l[1][:len(_l[1]) - 1]))

# 设置字体
plt.rcParams['font.family'] = ['SimHei']

plt.figure(figsize=(10, 10), dpi=300)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=150)
plt.title("1980-2016年游戏类型饼状图", fontsize=15)
plt.legend(loc="lower left", fontsize=8, borderaxespad=0.3)
plt.savefig('C:/Users/DXY/Desktop/大数据/Genre.png')
plt.show()
