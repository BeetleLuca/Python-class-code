#请删除序号及下划线，填写正确的代码，使程序完善。
height=float(input("请输入你的身高（米）："))
weight=float(input("请输入你的体重（千克）："))
BMI=weight/(height*height)
if BMI>=18.5 and BMI<=23.9:
    print("你的体重指数BMI为:",BMI,"符合标准！")
else:
    print("你的体重指数BMI为:",BMI,"不符合标准！")

