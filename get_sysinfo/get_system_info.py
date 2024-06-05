import subprocess
import os

if os.name == "nt":
    shell_value=True
    count = "-n"
    results = subprocess.run(["wmic", "bios", "get", "serialnumber"], shell=shell_value, capture_output=True, text=True)
    # print(results.stdout)
    output = "---------------------------\n %s\n ---------------------------\n"%(results.stdout)
    # print(type(results.stdout))
    file = open("system.txt","a")
    file.write(output)
    file.close()
else:
    print("Operating system is not Windows!")