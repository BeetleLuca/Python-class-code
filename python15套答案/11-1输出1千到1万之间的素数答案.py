#输出1000-10000之间的素数
 
def isPrime(n):   #定义函数isPime判断参数n是否为素数，是返回True，否则返回False
      if n <= 1:  #小于等于1的数不是素数
        return False
      for i in range(2, int(n**0.5) + 1):  # i的范围2到n的平方根取整，平方根用n的0.5次方计算
          if n%i==0:  # 如果i是n的因数，则返回False
            return False
      return True                      

for x in range(1000,10001):
    if isPrime(x):  # 调用函数进行判断x是否为素数
        print(x)
