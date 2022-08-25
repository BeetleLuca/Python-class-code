
#最适宜运动心率=（220-年龄-安静心率）×（60%~80%）+安静心率

import math
import random
import os
age=float(input('请输入年龄='))       #输入年龄
Hrest=float(input('请输入安静心率='))    #输入安静心率（HRrest）
high=int((220-age-Hrest)*0.8+Hrest)           #计算最适宜运动心率高值   
low=int((220-age-Hrest)*0.6+Hrest)            #计算最适宜运动心率低值 
print('最适宜的运动心率为:',low,'~',high,)                             #显示最适宜运动心率的范围
input("运行完毕，请按回车键退出...")
os._exit(0)
