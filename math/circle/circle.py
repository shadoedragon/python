# 这个程序用来计算圆的周长与面积
import math

print("你好，请输入要计算的最大半径，我们将从半径为1开始输出")
r = int(input())
i=1
print("半径   周长    面积")

while i <= r:
    print(i, 2*math.pi*i, math.pi*math.pow(i,2))
    i=i+1