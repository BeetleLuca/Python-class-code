op=1  #op保存分数项前的符号，取值为1或-1
pi=3  
for i in range(2, 101,2):
    pi = pi + op*4/(i*(i+1)*(i+2))  # 循环迭代求pi的近似值
    op = - op  # 分数项前的符号系数变成原来的相反数

print(pi)
