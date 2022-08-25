
s = 3
time = float(input("请输入车辆通行时间（用秒计时）："))
v = s*3600/time
if v<=60:
   print("正常行驶,祝你一路顺风！")
else:
   print("你的车速为",round(v,1),"千米/时")
   print("你已超速，请安全驾驶")
