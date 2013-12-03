# File:   Test4.py
# Vision: V1.0
# Author: pengwanyou
# Time: 2013.11.11
# Imports the monkeyrunner modules used by this program 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By 

# Connects to the current device, returning a MonkeyDevice object 
device = MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device) 

# Runs the component
easy_device.startActivity(component='cn.richinfo.thinkdrive/.ui.activities.NavigateActivity')

# sleep 2's
MonkeyRunner.sleep(2)

# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test4\\Test4_001.png','png')

# Click username input box
easy_device.touch(By.id('id/edt_account'),MonkeyDevice.DOWN_AND_UP)        
# Input username
# Problem:   .
device.type('you@demo.cn')
#device.type('you@demo')
#device.type('.cn')
print('Input username: you@demo.cn')

# Click password input box     
easy_device.touch(By.id('id/edt_password'), MonkeyDevice.DOWN_AND_UP)
# Input password
device.type('123qwe')
print('Input password: 123qwe')
# Press the Back Key
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)

# sleep 2's
MonkeyRunner.sleep(2)
# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test4\\Test4_002.png','png')
  
# Click Login button
easy_device.touch(By.id('id/btn_login'), MonkeyDevice.DOWN_AND_UP)

# sleep 2's
MonkeyRunner.sleep(3)
# Takes a screenshot 
result = device.takeSnapshot()
# Writes the screenshot to a file 
result.writeToFile('E:\\JAVA\\monkeyrunner\\Test4\\Test4_003.png','png')
print('Login Success!')