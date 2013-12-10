# File:   filepath.py
# Vision: V1.0
# Author: Findyou
# Time: 2013.12.03
# 引入模块
import sys

# 获得路径
path = sys.path[0]
print(sys.path[0])

# 将\替换为/
path = path.replace('\\','/')

# 找到最后一个冒号位置
index = path.rfind(":")

# 分片
print(path[index-1:])


