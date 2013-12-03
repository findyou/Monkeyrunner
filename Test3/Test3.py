# File:   Test3.py
# Vision: V1.0
# Author: pengwanyou
# Time: 2013.11.11
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()

# Runs the component 
device.startActivity(component="cn.richinfo.thinkdrive/cn.richinfo.thinkdrive.ui.activities.NavigateActivity")
# Sleep 5's
MonkeyRunner.Sleep(5)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test3\\Test3_001.png','png')

# First Left Drag
device.drag((580,1053),(100,1053),0.1,10)
# Sleep 1's
MonkeyRunner.Sleep(1)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test3\\Test3_002.png','png')


# Second Left Drag
device.drag((580,1053),(100,1053),0.1,10)
# Sleep 1's
MonkeyRunner.Sleep(1)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test3\\Test3_003.png','png')