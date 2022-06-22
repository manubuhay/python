import subprocess

p1=subprocess.run("dir", shell=True) # 'shell=True' binds it to OS system's shell environment
p1=subprocess.run(["netstat","-ano"]) # In LINUX make parameter an array/list instead of string to omit shell=True
p1=subprocess.run(["netstat","-ano"], capture_output=True)
print(p1.args)
print(p1.returncode)
print(p1.stdout) # Outputs are jumbled and displayed in bytes
print(p1.stdout.decode()) # Call decode function to display stdout properly

p2=subprocess.run(["netstat","-ano"], capture_output=True, text=True) # No need for decode function in line 9 
p2=subprocess.run(["netstat","-ano"], stdout=subprocess.PIPE, text=True) # 'capture_output=True' sets both stderr and stdout to subprocess.PIPE in the bg
print(p2.stdout) # Add 'text=True' as subprocess parameter, no need for decode function

with open("out_put.txt", "w") as f:
    p3=subprocess.run(["netstat","-ano"], stdout=f, text=True)

p4=subprocess.run(["dir","dne"], shell=True,capture_output=False,text=T # "check=True" captures entire error
print(p4.returncode)
print("Error is: ",p4.stderr)

p5=subprocess.run(["dir","dne"],shell=True,stderr=subprocess.DEVNULL) # 'stderr=subprocess.DEVNULL' ignores errors
print(p5.returncode)
print("Error is: ",p5.stderr)

#WINDOWS
pwin1=subprocess.run(["type","out_put.txt"],shell=True,capture_output=True,text=True)
#print(pwin1.stdout)
pwin2=subprocess.run(["findstr","443"],shell=True,capture_output=True,text=True,input=pwin1.stdout)
print(pwin2.stdout)

# #LINUX
# plin=subprocess.run(["cat","out_put.txt"],capture_output=True, text=True)
# #print(plin1.stdout)
# plin2=subprocess.run(["grep","443"],capture_output=True, text=True, input=plin1.stdout)
# print(plin2.stdout)