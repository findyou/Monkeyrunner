# File:   Takesnapshot.py
# Vision: V1.0
# Author: pengwanyou
# Monkeyrunner E:\JAVA\monkeyrunner\TakeSnapshot.py
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner
import time

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()

# Get the current time
c_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

# Takes a screenshot 
result = device.takeSnapshot()

# Writes the screenshot to a file 
filepath = "E:/Takesnapshot_" + c_time + ".png"
result.writeToFile(filepath,'png')
print(r'Takesnapshot.png')