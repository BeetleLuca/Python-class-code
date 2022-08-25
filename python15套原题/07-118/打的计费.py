
import __①__  # 引用math库
s = __②__(input("请输入你要去目的地距离出发点的公里数:"))
if __③__:        # 2公里（包括2公里）内
   cost = 5
else:
   cost = 5+math.ceil(s-2)*1.6
print("你的打的费用是", __④__, "元")
