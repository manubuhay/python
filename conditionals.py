print("hello")
var1 = input("what is your name?")
if (var1 == 'manu' or var1 == "Manu"):
	print("True")
else:
	print("False")

print("\n")
print("Hello World")


########Temporary set
####PATH variable#####
#Append
#PATH=$PATH:/path/to/directory
#Prepend (add to first line, executes executable found on first line)
#PATH=/root:$PATH

########Permanent set
#edit .bashrc in your $HOME directory
#add the following lines
#export <variable>=</path/to/directory>
#e.g. "export ANDROID_HOME=/home/manu/bin"
#export PATH=$PATH:$<variable>
#e.g. "export PATH=$PATH:ANDROID_HOME"
#		Where "ANDROID_HOME" is the variable holding the path to directory of the binary/executable
#		In this example, it is APPENDING to the value of the PATH variable, means it is adding the value to the last part
