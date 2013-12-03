# File:   Test06.py
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

# sleep 5's
MonkeyRunner.sleep(5)
# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
filepath = path + "/Test6_001.png"
result.writeToFile(filepath,'png')

# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('Rightdrag Success!')
# sleep 3's
MonkeyRunner.sleep(3)

# ======================================================================
# Click favorite 
# easy_device.touch(By.id('id/rl_my_favorite'), MonkeyDevice.DOWN_AND_UP)
# [0,330][576,436]
device.touch(200,380,'DOWN_AND_UP')
print('Click My_favorite Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('  ->Rightdrag Success!')
# sleep 3's
MonkeyRunner.sleep(3)

# ======================================================================
# Click rl_my_disk  
# easy_device.touch(By.id('id/rl_my_disk'), MonkeyDevice.DOWN_AND_UP)
# [0,221][576,327]
device.touch(200,280,'DOWN_AND_UP')
print('Click My_disk Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('  ->Rightdrag Success!')
# sleep 3's
MonkeyRunner.sleep(3)

# ======================================================================
# Click file_share 
# easy_device.touch(By.id('id/rl_file_share'), MonkeyDevice.DOWN_AND_UP)
# [0,439][576,545]
device.touch(200,500,'DOWN_AND_UP')
print('Click File_share Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('  ->Rightdrag Success!')
# sleep 3's
MonkeyRunner.sleep(3)

# ======================================================================
# Click photo_backup 
# easy_device.touch(By.id('id/rl_photo_backup'), MonkeyDevice.DOWN_AND_UP)
# [0,548][576,654]
device.touch(200,600,'DOWN_AND_UP')
print('Click Photo_backup Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('  ->Rightdrag Success!')
# sleep 3's
MonkeyRunner.sleep(3)

# ======================================================================
# Click file_trnasfer 
# easy_device.touch(By.id('id/rl_file_trnasfer'), MonkeyDevice.DOWN_AND_UP)
# [0,657][576,763]
device.touch(200,700,'DOWN_AND_UP')
print('Click File_trnasfer Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Right drag ->System menu
device.drag((100,750),(500,750),0.1,10)
print('  ->Right drag Success!')
# sleep 3's
MonkeyRunner.sleep(3)

# ======================================================================
# Click system_setting 
# easy_device.touch(By.id('id/rl_system_setting'), MonkeyDevice.DOWN_AND_UP)
# [0,766][576,872]
device.touch(200,800,'DOWN_AND_UP')
print('Click System_setting Success!')
# ======================================================================

# sleep 3's
MonkeyRunner.sleep(3)
# Press the Back Key
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
# sleep 3's
MonkeyRunner.sleep(3)
# Press the Back Key
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
# sleep 3's
MonkeyRunner.sleep(3)
# Click confirm
#easy_device.touch(By.id('id/common_confirm'), MonkeyDevice.DOWN_AND_UP)
#[389,721][594,786] [451,729][532,778]
device.touch(491,753,'DOWN_AND_UP')
print('Click Loginout app Success!')
