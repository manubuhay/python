import subprocess
import os

if os.name == "nt":
    results = subprocess.run(["wmic", "bios", "get", "serialnumber"], shell=True, capture_output=True, text=True)
    cmd = subprocess.run(["systeminfo.exe"], shell=True, capture_output=True, text=True)
    pipe1 = subprocess.run(["findstr","Manufacturer"],shell=True, capture_output=True, text=True, input=cmd.stdout)
    pipe2 = subprocess.run(["findstr","Model"], shell=True, capture_output=True, text=True, input=cmd.stdout)
    # print(results.stdout)
    owner=input("Owner: ")
    output = "---------------------------\n %s %s\n %s %s---------------------------\n"%(results.stdout, owner, pipe1.stdout, pipe2.stdout)
    # print(type(results.stdout))
    file = open("system.txt", "a")

    # From: https://stackoverflow.com/questions/7169845/using-python-how-can-i-access-a-shared-folder-on-windows-network
    # The syntax below is for accessing "system.txt" if it is in a network share
    # file = open("\\\\server_ip\\directory1\\directory2\\system.txt", "a")
    
    file.write(output)
    file.close()
else:
    print("Operating system is not Windows!")