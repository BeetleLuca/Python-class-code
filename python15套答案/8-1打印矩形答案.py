a=int(input("请输入行数："))
b=int(input("请输入列数："))

for i in range(0,a):
#          或者(1,a+1)
    for j in range(0,b):
#          或者（1,b+1)
        print('*',end='')    #end=''表示接上一个输出项后输出，不换行
    print()
    
    
