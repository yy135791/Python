import subprocess
import time
import datetime
import os

def clear():os.system('cls')
def ceshi():
    cmd = 'cd C:\Program Files\Google\Chrome\Application&&python ceshi.py'
    child1 = subprocess.Popen(cmd, shell=True)
    # child1.wait()
    # cmd = 'python ceshi.py'
    # child2 = subprocess.Popen(cmd, shell=True)
def ceshi1():
    cmd = 'cd C:\Program Files\Google\Chrome\Application&&python ceshi1.py'
    child3 = subprocess.Popen('cmd.exe /C {}'.format(cmd), creationflags=subprocess.CREATE_NEW_CONSOLE)
    child3.wait()

i = 0

while True:
    now = datetime.datetime.now()
    time.sleep(1)
    i += 1
    print('已等待{}秒'.format(i))
    if i % 50 == 0:
        clear()
    if now.minute == 59 and now.second == 0:   # 每个小时第十分钟开始85次发帖
        ceshi()
        time.sleep(3)
        ceshi1()
        time.sleep(5)
