n=int(input("请输入一个整数："))
m=int(input("请输入一组数据的第一个数："))
min=m
max=m  
for i in range(1,n):
    t=int(input("请输入后续的数："))
    if  t<min:
         min=t  
    if  t>max:
        max=t  
print(max-min)  #输出极差的值

input("运行完毕，请按回车键退出...")
