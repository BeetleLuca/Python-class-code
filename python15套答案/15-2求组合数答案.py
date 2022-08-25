def fac(n):      #用递归的方法求n!
    if n == 0:
        return 1
    else:
        return n*fac(n-1)

n=int(input("请输入正整数n的值："))
m=int(input("请输入正整数m的值(m<=n)："))
c = fac(n)//(fac(m)*fac(n-m))
print(c)
