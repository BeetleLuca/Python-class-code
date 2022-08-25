#程序的功能是实现用户名和密码的登录验证
cnt=1  #输入错误次数
username=input("请输入用户名：")#输入用户名
pwd =input("请输入密码：")  # 请输入密码
if username == "user1" and pwd=="123456"  # 登录成功的条件
    print("你好", username, "登录成功")
elif username=="user1":#用户名正确
    while pwd!="123456" and cnt != 3:  # 密码错误，且错误次数不等于3
        print("密码错误，请重新输入正确的密码!你还有", 3-cnt, "次机会")
        pwd=input("请输入密码：")
        cnt = cnt+1  # 输入错误次数累加
        if username == "user1" and pwd == "123456":
             print("你好",username,"登录成功")
             break  # 登录成功则跳出while循环
else:
    print("用户名不存在！")
