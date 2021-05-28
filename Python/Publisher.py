from matplotlib import pyplot as plt

# 绘制发行公司发行游戏数量柱状图

x = []
y = []
# 从文件读取数据并保存
with open("C:/Users/DXY/Desktop/大数据/Game/Publisher/part-r-00000", "r") as f:
    for line in f:
        # 切割数据
        _l = line.split("\t")
        num = int(_l[1][:len(_l[1]) - 1])
        name = _l[0]
        if name == "N/A":
            continue
        # 小于10算其他公司
        if num > 100:
            x.append(name)
            y.append(num)

# 设置字体
plt.rcParams['font.family'] = ['SimHei']

plt.figure(figsize=(20, 20), dpi=300)

# 画条形图
plt.bar(range(len(x)), y, width=0.8, bottom=0)
# width:条形图宽度
# bottom y的最小值从什么时候开始

# 每个点标识
for a, b in zip(range(len(x)), y):
    plt.text(a, b + 1, b, ha='center', va='center', fontdict={"fontsize": 12})

# 修改x轴刻度, 替换数字变为公司名称，倾斜文字
plt.xticks(range(len(x)), x, rotation=70, fontsize=10)
plt.yticks(fontsize=20)

plt.title("1980-2016年电视游戏发行发行公司发行游戏数量柱状图", fontsize=25)
plt.xlabel("公司", fontsize=20)
plt.ylabel("发行数量", fontsize=20)
plt.savefig('C:/Users/DXY/Desktop/大数据/Publisher.png')
plt.show()
