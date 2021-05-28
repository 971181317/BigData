from matplotlib import pyplot as plt

# 绘制游戏登录平台折线图

# key为平台，value数组0为x，1为y
map = {}
# 从文件读取数据并保存  SNES,1999	1
with open("C:/Users/DXY/Desktop/大数据/Game/Platform/part-r-00000", "r") as f:
    for line in f:
        # 切割数据
        _l = line.split("\t")
        nameAneYear = _l[0].split(",")
        name = nameAneYear[0]
        if nameAneYear[1] == "N/A":
            continue
        year = int(nameAneYear[1])
        size = int(_l[1][:len(_l[1]) - 1])
        x = []
        y = []
        if name in map:
            x = map[name][0]
            y = map[name][1]
        x.append(year)
        y.append(size)
        map[name] = [x, y]

# 设置字体
plt.rcParams['font.family'] = ['SimHei']
plt.figure(figsize=(30, 15), dpi=300, facecolor='w')
# 修改y轴刻度
plt.yticks(range(0, 550, 100), fontsize=25)
plt.xticks(range(1980, 2020, 1), fontsize=15)

# 线条颜色值
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
colorIdx = 0
line = [":", "--", "-.", "-"]
lineIdx = 0

for name, value in map.items():
    # 颜色数组越界
    if colorIdx >= len(color):
        colorIdx = 0
    if lineIdx >= len(line):
        lineIdx = 0
    # 绘制
    plt.plot(value[0], value[1], label=name, color=color[colorIdx], linestyle=line[lineIdx])
    colorIdx += 1
    lineIdx += 1
# 左上角显示图例
plt.legend(loc='upper left', fontsize=15)

plt.title("1980-2016游戏登录平台折线图", fontsize=25)
plt.xlabel("年份", fontsize=25)
plt.ylabel("数量", fontsize=25)
plt.savefig('C:/Users/DXY/Desktop/大数据/Platform.png')
plt.show()
