# File:   Test012.py
# Vision: V1.1
# Author: Findyou
# Time: 2013.12.03
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
import time,sys

# Get the current path
path = sys.path[0]
path = path.replace('\\','/')
path = path[path.rfind(":")-1:]

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device) 

# Runs the component
easy_device.startActivity(component='cn.richinfo.thinkdrive/.ui.activities.NavigateActivity')

def take_Snapshot():
	# sleep 3's
	# MonkeyRunner.sleep(3)
	c_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	# Takes a screenshot 
	result = device.takeSnapshot()
	# Writes the screenshot to a file 
	result.writeToFile(path + "/Test12_" + c_time + ".png",'png')

def system_back():
	# sleep 3's
	MonkeyRunner.sleep(3)
	# Press the Back Key
	device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)

# sleep 2's
MonkeyRunner.sleep(5)
take_Snapshot()

# ======================================================================
# Click Upload (+)
# easy_device.touch(By.id('id/control_hint'), MonkeyDevice.DOWN_AND_UP)
# [617,1077][710,1170]
device.touch(663,1123,'DOWN_AND_UP')
print('Click Upload Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Take Snapshot
take_Snapshot()

# ======================================================================
# New Folder
# [396,1086][476,1166] ->Center[436,1126]
device.touch(436,1126,'DOWN_AND_UP')

# sleep 3's
MonkeyRunner.sleep(3)
# Take Snapshot
take_Snapshot()

# Enter the folder name
# easy_device.touch(By.id('id/dialog_message ??'), MonkeyDevice.DOWN_AND_UP)
# [130,627][590,686] ->Center[360,656]
# device.touch(360,656,'DOWN_AND_UP')
# device.type("Fuck_you!")
# #Move the cursor to the last
# device.press('KEYCODE_MOVE_END',MonkeyDevice.DOWN_AND_UP)
# #Del something
# device.press('KEYCODE_DEL',MonkeyDevice.DOWN_AND_UP)

# Confirm New Folder
# easy_device.touch(By.id('id/dialog_button_ok??'), MonkeyDevice.DOWN_AND_UP)
# [389,726][594,791] ->Center[491,758]
device.touch(491,758,'DOWN_AND_UP')

# Cancel New Folder
# easy_device.touch(By.id('id/??'), MonkeyDevice.DOWN_AND_UP)
# [126,726][331,791]  ->Center[228,758]
# device.touch(228,758,'DOWN_AND_UP')

# sleep 1's
MonkeyRunner.sleep(1)
# Take Snapshot
take_Snapshot()

# sleep 1's
MonkeyRunner.sleep(4)
# Take Snapshot
take_Snapshot()

print('New Folder Success!')
# ======================================================================

# Press the "Back" button
system_back()

# sleep 3's
MonkeyRunner.sleep(3)
# Click confirm
#easy_device.touch(By.id('id/common_confirm'), MonkeyDevice.DOWN_AND_UP)
#[389,721][594,786] [451,729][532,778]
device.touch(491,753,'DOWN_AND_UP')
print('Click Loginout app Success!')
