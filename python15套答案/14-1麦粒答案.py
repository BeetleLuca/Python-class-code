#开始
sum=669490000000*5000 #计算麦粒的总量
wheat = 1  # wheat为每个棋盘上放的麦子数，赋初值
count = 1  # count为棋盘的格数
while sum>0:
    sum=sum-wheat #计算放了麦粒后还剩的麦子数
    #输出每格棋盘上放的麦子数，以及还剩的麦子数
    print(f"第{count}格上的应放米粒数为{wheat}，还剩麦粒总数为{sum}")
    wheat = 2**count  # 计算每格棋盘上的麦粒
    count=count+1  # 棋格递增一

#输出我国2020年全国粮食产量可以放到棋盘的第几格
if sum==0:
    print("2020年我国全国粮食产量可以放满棋盘的",count-1,"格")
else:
    print("2020年我国全国粮食产量可以放满棋盘的", count-2, "格")
