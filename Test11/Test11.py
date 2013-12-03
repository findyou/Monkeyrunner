# File:   Test11.py
# Vision: V1.0
# Author: pengwanyou
# Time: 2013.11.18
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
import time


# file path
c_filepath = "E:/JAVA/monkeyrunner/Test11/Test11_"

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
	result.writeToFile(c_filepath + c_time + ".png",'png')

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
# Upload file
# [413,997][493,1077] ->Center[453,1037]
device.touch(453,1037,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

# Twice top slide
device.drag((380,1000),(380,100),0.1,10)
MonkeyRunner.sleep(2)
device.drag((380,1000),(380,100),0.1,10)
MonkeyRunner.sleep(2)
device.drag((380,1000),(380,100),0.1,10)
MonkeyRunner.sleep(2)

# List the last file
# easy_device.touch(By.id('id/?'), MonkeyDevice.DOWN_AND_UP)
# [651,1079][700,1123]   [675,1101]
device.touch(675,1101,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

# Upload 
# easy_device.touch(By.id('id/?'), MonkeyDevice.DOWN_AND_UP)
# [582,1215][671,1264] [626,1239]
device.touch(626,1239,'DOWN_AND_UP')

# Upload path
# easy_device.touch(By.id('id/?'), MonkeyDevice.DOWN_AND_UP)
# [20,1210][533,1270]  [276,1240]
# device.touch(276,1240,'DOWN_AND_UP')

# Take Snapshot
take_Snapshot()

print('Upload File Success!')
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
