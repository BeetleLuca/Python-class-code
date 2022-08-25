#天天向上
dayup=1                 #设置dayup为能力值，factor为能力变化幅度 
factor=0.01
for i in range(__①__):
    dayup = __②__ * (1+factor)
print("天天向上的能力值：%.2f" % dayup)

#五上二下
dayup=1
for i in range(__③__):
    if __④__ in [6, 0]:  # 判断是否为休息日，是则能力下降；否则能力上升。
        dayup = dayup*(1-factor)
    else:
        dayup = dayup*(__⑤__)
print("向上5天向下2天的能力值：%.2f" % dayup)  # 打印结果
