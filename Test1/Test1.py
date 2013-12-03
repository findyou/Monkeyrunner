# File:   Test1.py
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
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test1\\Test1_001.png','png')

# remove apk
device.removePackage('cn.richinfo.thinkdrive')
print ('Uninstall Success!')

# sleep 5's
MonkeyRunner.sleep(5)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test1\\Test1_002.png','png')

# install apk
device.installPackage('E:\\JAVA\\monkeyrunner\\Test1\\ThinkDrive_new.apk')
print ('Install Success!')

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test1\\Test1_003.png','png')