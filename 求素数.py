X=int(input("请输入大于1的正整数="))
for i in range(2,X+1):
    if X%i==0:
        break
if X%i==0:
    print("此数不是素数")
else:
    print("此数是素数")
