# File:   Test01.py
# Vision: V1.1
# Author: pengwanyou
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

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test1_001.png"
result.writeToFile(filepath,'png')

# remove apk
device.removePackage('cn.richinfo.thinkdrive')
print ('Uninstall Success!')

# sleep 5's
MonkeyRunner.sleep(5)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test1_002.png"
result.writeToFile(filepath,'png')

# install apk
device.installPackage(path + '/ThinkDrive_new.apk')
print ('Install Success!')

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test1_003.png"
result.writeToFile(filepath,'png')
