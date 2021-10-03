import os
import subprocess

#data=os.system("dir")
#data=os.popen("dir").readline()
#data=os.popen("dir").readlines()
#print(data)

f1=open("out.txt","w")
f2=open("error.txt","w")

#out=subprocess.run("date", shell=True) #"shell=True" parameter must be added when OS is windows
out=subprocess.run("dir", shell=True,stdout=f1,stderr=f2)
#out=subprocess.run("date", shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(out)
