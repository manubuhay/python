import subprocess
import os

# p1=subprocess.check_output(["cat","./AIO9185260153_attlog.dat"]) #Parse first command for piping
# print(type(p1))
# p1=p1.decode("utf-8")
# # print(p1)

# p2=subprocess.Popen(["awk\ \'$1==\"78\" \{print$0}\'"],input=p1)
# # p2=p2.decode("utf-8")
# print(p2)

# ps = subprocess.Popen(("cat","./AIO9185260153_attlog.dat"), stdout=subprocess.PIPE)
# output = subprocess.check_output(("awk\ \'$1==\"78\" \{print$0}\'"), stdin=ps.stdout)
# ps.wait()
# print(output)

# cmd="""awk '$1=="%s" {print$0}'"""%(id)
# args = ["awk",r"$1==80" r'{OFS="\t"; print $0}'] #Static string values testing
# args = ["awk",r"$1==80 {print $0}"] #Static string values testing
# id="80" #Dynamic string based testing
# cond=r"$1==%80"
path=os.getcwd()
fpath=os.path.join(path,"Full_Biometric.dat")
id=str(input("Input ID: ")) #Input based testing
args = ["awk",r"$1==%s {print $1,$2,$3}"%(id)] #Display 1st 3 columns
# p1 = subprocess.run(["cat","./Full_Biometric.dat"],check=True,capture_output=True)
p1 = subprocess.run(["cat",fpath],check=True,capture_output=True)
# processNames = subprocess.run(["awk \'$1==\"78\" {print$0}\'"], input=ps.stdout, capture_output=True)
# processNames = subprocess.run([cmd], input=ps.stdout, capture_output=True)

p2 = subprocess.run(args,input=p1.stdout,capture_output=True)
# print(ps.stdout.decode('utf-8').strip())

print(p2.stdout.decode('utf-8').strip())