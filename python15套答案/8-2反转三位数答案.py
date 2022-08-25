x=int(input("请输入一个任意三位整数："))
ge=x%10
shi=x//10%10
bai=x//100
y=ge*100+shi*10+bai
print(y)
