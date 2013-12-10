# File:   Takesnapshot.py
# Vision: V1.0
# Author: Findyou
# Monkeyrunner TakeSnapshot.py
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner
import sys

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()

# Get the current path
path = sys.path[0]
path = path.replace('\\','/')
path = path[path.rfind(":")-1:]

# Takes a screenshot 
result = device.takeSnapshot()

# Writes the screenshot to a file 
filepath = path + "/Test1_001.png"
result.writeToFile(filepath,'png')
print(r'Takesnapshot.png')