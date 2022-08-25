m=int(input("请输入自然数m:"))
n=int(input("请输入自然数n:"))
i=1
if m<n:
    m,n=n,m  #两数交换（用大数翻倍）
s=m            #s的初始值较大数
while s%n!=0:
    i = i+1
    s =m*i
print(s)

