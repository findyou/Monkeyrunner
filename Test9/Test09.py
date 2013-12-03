# File:   Test09.py
# Vision: V1.1
# Author: pengwanyou
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
	MonkeyRunner.sleep(3)
	c_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	# Takes a screenshot 
	result = device.takeSnapshot()
	# Writes the screenshot to a file 
	result.writeToFile(path + "/Test09_" +c_time + ".png",'png')

def system_back():
	# sleep 3's
	MonkeyRunner.sleep(3)
	# Press the Back Key
	device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)

# sleep 2's
MonkeyRunner.sleep(2)
take_Snapshot()

# ======================================================================
# Click Upload (+)
# easy_device.touch(By.id('id/control_hint'), MonkeyDevice.DOWN_AND_UP)
# [617,1077][710,1170]
device.touch(663,1123,'DOWN_AND_UP')
print('Click Upload Success!')
# ======================================================================

# Take Snapshot
take_Snapshot()

# ======================================================================
# Record
# [537,873][617,953]  [577,913]
device.touch(577,913,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

# Start recording
# [280,1109][439,1268] [359,1188]
# device.touch(326,232,'DOWN_AND_UP')
easy_device.touch(By.id('id/start'), MonkeyDevice.DOWN_AND_UP)

# Take Snapshot
take_Snapshot()

# Stop recording
# [280,1109][439,1268] [359,1188]
# device.touch(326,232,'DOWN_AND_UP')
easy_device.touch(By.id('id/stop'), MonkeyDevice.DOWN_AND_UP)

# Take Snapshot
take_Snapshot()

# Sava the recording
# easy_device.touch(By.id('id/save'), MonkeyDevice.DOWN_AND_UP)
# [80,567][640,621]  [360,594]
device.touch(360,594,'DOWN_AND_UP')

# Re-recording
# easy_device.touch(By.id('id/retry'), MonkeyDevice.DOWN_AND_UP)
# [80,682][640,736]  [360,709]
# device.touch(360,709,'DOWN_AND_UP')

# Cancel the recording
# easy_device.touch(By.id('id/cancel'), MonkeyDevice.DOWN_AND_UP)
# [80,797][640,851]  [360,824]
# device.touch(360,824,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

print('Upload recording Success!')
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