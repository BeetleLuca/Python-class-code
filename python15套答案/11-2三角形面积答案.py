#请删除序号及下划线，填写正确的代码，使程序完善。
import math
a=float(input("请输入第一条边长："))
b=float(input("请输入第二条边长："))
c=float(input("请输入第三条边长："))
if(a+b>c)and(a+c>b)and(b+c>a):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(a,b,c,"能构成三角形！","三角形的面积为:",s)
else:
    print(a,b,c,"不能构成三角形！")
