# File:   Test05.py
# Vision: V1.1
# Author: pengwanyou
# Time: 2013.12.03
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
import sys

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device) 

# Get the current path
path = sys.path[0]
path = path.replace('\\','/')
path = path[path.rfind(":")-1:]

# Runs the component
easy_device.startActivity(component='cn.richinfo.thinkdrive/.ui.activities.NavigateActivity')

# sleep 2's
MonkeyRunner.sleep(5)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test5_001.png"
result.writeToFile(filepath,'png')

# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('Right drag Success!')

# sleep 3's
MonkeyRunner.sleep(3)
# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test5_002.png"
result.writeToFile(filepath,'png')

# Click Setting  
#easy_device.touch(By.id('id/rl_system_setting'), MonkeyDevice.DOWN_AND_UP)
#[0,766][576,872]
device.touch(200,800,'DOWN_AND_UP')
print('Click Setting Success!')

# sleep 3's
MonkeyRunner.sleep(3)
# Click Loginout button
#easy_device.touch(By.id('id/btn_loginout'), MonkeyDevice.DOWN_AND_UP)
#[16,1139][704,1218]
device.touch(296,1156,'DOWN_AND_UP')
print('Click Loginout button Success!')

# sleep 3's
MonkeyRunner.sleep(3)
# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test5_003.png"
result.writeToFile(filepath,'png')

# Click confirm
#easy_device.touch(By.id('id/common_confirm'), MonkeyDevice.DOWN_AND_UP)
#[389,721][594,786]
device.touch(491,753,'DOWN_AND_UP')

# sleep 3's
MonkeyRunner.sleep(3)
# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test5_004.png"
result.writeToFile(filepath,'png')
print('Loginout Success!')