# File:   Test03.py
# Vision: V1.1
# Author: Findyou
# Time: 2013.12.03
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import sys

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()

# Get the current path
path = sys.path[0]
path = path.replace('\\','/')
path = path[path.rfind(":")-1:]

# Runs the component 
device.startActivity(component="cn.richinfo.thinkdrive/cn.richinfo.thinkdrive.ui.activities.NavigateActivity")
# Sleep 5's
MonkeyRunner.Sleep(5)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test3_001.png"
result.writeToFile(filepath,'png')

# First Left Drag
device.drag((580,1053),(100,1053),0.1,10)
# Sleep 1's
MonkeyRunner.Sleep(1)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test3_002.png"
result.writeToFile(filepath,'png')


# Second Left Drag
device.drag((580,1053),(100,1053),0.1,10)
# Sleep 1's
MonkeyRunner.Sleep(1)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test3_003.png"
result.writeToFile(filepath,'png')