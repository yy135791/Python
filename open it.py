import os
import time

cmd = 'cd C:\Program Files\Google\Chrome\Application'
os.system(cmd)
cmd = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'
time.sleep(1)
print('成功打开9222端口浏览器，正在运行脚本')
os.system(cmd)
time.sleep(1)
print('已关闭！')

