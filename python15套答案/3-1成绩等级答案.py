#此程序功能是实现输出成绩等级。
pscore=int(input("请输入平时成绩:"))#输入平时成绩
qscore= int(input("请输入期末成绩:"))     #请输入期末成绩
score=  0.3*pscore+0.7*qscore     #计算总成绩
if score>100 or score<0:
    print("你的成绩输入有误")
elif score>=90:  # 优秀等级的条件
    print("优秀")
elif score>=75:
   print("良好")  # 输出相应等级
elif score >= 60:
    print("合格")

else:
    print("不合格")
