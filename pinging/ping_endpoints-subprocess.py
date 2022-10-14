#Only use when Python version >= 3.8x
import subprocess
import os

def _subproc(ipurl)->None:
    if os.name == "nt":
        subprocess.run(["ping",ipurl],shell=True,text=True)
    # Else, it might be linux or mac (posix)
    else:
        # Omit 'shell=True' in LINUX/MAC systems
        subprocess.run(["ping",ipurl],text=True)

def main()->None:
    while True:
        mapping = {1: "IP1",2: "IP2",3: "www.google.com",4: "8.8.8.8"}
        print("####################################################")
        print("|| 1 - Ping Firewall                              ||")
        print("|| 2 - Ping Cloudkey                              ||")
        print("|| 3 - Ping Internet                              ||")
        print("|| 4 - Ping Internet(No DNS)                      ||")
        print("####################################################")
        opt=int(input("Which Option: "))
        if opt < 5:
            print("Pinging, please wait....")
            ipurl=mapping.get(opt,None)
            _subproc(ipurl)
        else:
            print("Invalid Option")
        print("\n")

main()