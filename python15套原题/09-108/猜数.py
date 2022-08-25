# 程序初始化，并随机产生一个0-99的整数作为秘密数，
import __①__  # 导入随机数模块
import math
secret=random.randint(0,99)
guess=0    
tries = __②__  # 尝试次数赋初值


#给定猜测次数n
n=6

# 打招呼
print('嗨，你好！今天我们来玩一个猜数游戏。')
print('这个数字在0－99之间，我给你6次机会。')

#得到玩家猜的数，并判断大小，最多允许n次
while tries<n and guess!=secret:
    __③__  # 尝试次数加1
    guess = int(input("请输入你猜的数："))
    if guess > secret:
        print("大了")
    elif guess < secret:
       print("小了")
    else:
        print("恭喜你,答对了！猜了", __④__, "次，")

#如果给出猜测的次数内没有猜对，则提示机会用完了，再来一次。
if tries == n and guess != __⑤__:
    print("机会用完了，再来一次！")





