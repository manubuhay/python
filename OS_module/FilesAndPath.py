import os

print(os.getcwd())
path=os.getcwd()+"./top_dir"
path="."
os.chdir(path)

for dirpath,dirnames,filenames in os.walk(path):
    print("Current Path:",dirpath)
    print("Directories:",dirnames)
    print("Files:",filenames)
    print()

for x,y,z in os.walk(path):
    print("Current Path:",x)
    print("Directories:",y)
    print("Files:",z)
    print()

file_path=os.path.join(os.getcwd(),"new_file.txt")
print(file_path)

print(os.path.basename("/tmp/test.txt")) # Outpus "test.txt"
print(os.path.dirname("/tmp/test.txt")) # Outpus "/tmp"
print(os.path.split("/tmp/test.txt")) # Outputs tuple "('/tmp', 'test.txt')"
print(os.path.exists("/tmp/test.txt")) # Outputs boolean False
print(os.path.isdir("/tmp/test.txt")) # Outputs boolean False(not a directory)
print(os.path.isfile("/tmp/test.txt")) # Outputs boolean if file AND exists
print(os.path.splitext("/tmp/test.txt")) # Outputs "('/tmp/test', '.txt')"
print(dir(os.path)) # Prints all functions in OS module
