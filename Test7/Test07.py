# File:   Test07.py
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
	result.writeToFile(path + "/Test07_" + c_time + ".png",'png')

def right_drag():
	# Right drag ->System menu
	device.drag((100,750),(500,750),0.1,10)
	print('  Right drag Success!')
	# sleep 3's
	MonkeyRunner.sleep(3)

def system_back():
	# sleep 3's
	MonkeyRunner.sleep(3)
	# Press the Back Key
	device.press('KEYCODE_BACK',MonkeyDevice.DOWN_AND_UP)

# sleep 2's
MonkeyRunner.sleep(2)
take_Snapshot()
right_drag()

# ======================================================================
# Click favorite 
# easy_device.touch(By.id('id/rl_my_favorite'), MonkeyDevice.DOWN_AND_UP)
# [0,330][576,436]
device.touch(200,380,'DOWN_AND_UP')
print('Click My_favorite Success!')
# ======================================================================

# Take Snapshot and Right drag 
take_Snapshot()
right_drag()

# ======================================================================
# Click rl_my_disk  
# easy_device.touch(By.id('id/rl_my_disk'), MonkeyDevice.DOWN_AND_UP)
# [0,221][576,327]
device.touch(200,280,'DOWN_AND_UP')
print('Click My_disk Success!')
# ======================================================================

# Take Snapshot and Right drag 
take_Snapshot()
right_drag()

# ======================================================================
# Click file_share 
# easy_device.touch(By.id('id/rl_file_share'), MonkeyDevice.DOWN_AND_UP)
# [0,439][576,545]
device.touch(200,500,'DOWN_AND_UP')
print('Click File_share Success!')
# ======================================================================

# Take Snapshot and Right drag 
take_Snapshot()
right_drag()

# ======================================================================
# Click photo_backup 
# easy_device.touch(By.id('id/rl_photo_backup'), MonkeyDevice.DOWN_AND_UP)
# [0,548][576,654]
device.touch(200,600,'DOWN_AND_UP')
print('Click Photo_backup Success!')
# ======================================================================

# Take Snapshot and Right drag 
take_Snapshot()
right_drag()

# ======================================================================
# Click file_trnasfer 
# easy_device.touch(By.id('id/rl_file_trnasfer'), MonkeyDevice.DOWN_AND_UP)
# [0,657][576,763]
device.touch(200,700,'DOWN_AND_UP')
print('Click File_trnasfer Success!')
# ======================================================================

# Take Snapshot and Right drag 
take_Snapshot()
right_drag()

# ======================================================================
# Click system_setting 
# easy_device.touch(By.id('id/rl_system_setting'), MonkeyDevice.DOWN_AND_UP)
# [0,766][576,872]
device.touch(200,800,'DOWN_AND_UP')
print('Click System_setting Success!')
# ======================================================================

# Press twice the "Back" button
system_back()
system_back()

# sleep 3's
MonkeyRunner.sleep(3)
# Click confirm
#easy_device.touch(By.id('id/common_confirm'), MonkeyDevice.DOWN_AND_UP)
#[389,721][594,786] [451,729][532,778]
device.touch(491,753,'DOWN_AND_UP')
print('Click Loginout app Success!')