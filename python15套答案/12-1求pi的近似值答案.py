sum,a,b,t=0.0,1,1.0,1.0   #给各参数依次赋值
while b<1000:
    sum=sum+t
    b=b+2
    a=-a
    t=a/b
pi = sum*4
print("pi的值是{:.20f}".format(pi))  # 输出20位浮点型数值
