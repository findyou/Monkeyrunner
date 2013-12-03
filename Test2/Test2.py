# File:   Test2.py
# Vision: V1.0
# Author: pengwanyou
# Time: 2013.11.11
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test2\\Test2_001.png','png')

# Runs the component 
device.startActivity(component="cn.richinfo.thinkdrive/cn.richinfo.thinkdrive.ui.activities.NavigateActivity")

# Sleep 5's
MonkeyRunner.sleep(5)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test2\\Test2_002.png','png')