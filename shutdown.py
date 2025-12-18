import os 
import platform 

def shutdown():
    s = platform.system()
    if s == "Linux" | s == "Darwin":
        os.system("sudo shutdown -h now")


shutdown() 

