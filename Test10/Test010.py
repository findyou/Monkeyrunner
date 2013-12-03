# File:   Test010.py
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
	result.writeToFile(path + "/Test010_" + c_time + ".png",'png')

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
# Photograph
# [463,923][543,1003]  ->Center[503,963]
device.touch(503,963,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

# Take a photograph
# easy_device.touch(By.id('id/button_capture'), MonkeyDevice.DOWN_AND_UP)
# [280,1109][439,1268]   [359,1188]
device.touch(359,1188,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()
print('Photographs success!')

# Upload Photograph
# easy_device.touch(By.id('id/button_upload'), MonkeyDevice.DOWN_AND_UP)
# [280,1109][439,1268]   [359,1188]
device.touch(359,1188,'DOWN_AND_UP')

# Re-Photograph
# easy_device.touch(By.id('id/button_retry'), MonkeyDevice.DOWN_AND_UP)
# [74,1158][194,1218]   [134,1188] 
# device.touch(134,1188,'DOWN_AND_UP')

# Cancel the Photograph
# easy_device.touch(By.id('id/button_cancel'), MonkeyDevice.DOWN_AND_UP)
# [525,1158][645,1218]  [585,1188]
# device.touch(585,1199,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

print('Upload Photograph Success!')
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