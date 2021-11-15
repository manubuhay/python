import os

# print(os.getcwd())
path=os.getcwd()+"./top_dir"
# path="."
# os.chdir(path)
print(path)
new_dir="random_name"
# Create directory in file system via variable name
# os.makedirs(os.path.join(path,f"{new_dir}","some_folder_below"))
some_path=os.path.join(path,f"{new_dir}","some_folder_below")
print(some_path)


# for dirpath,dirnames,filenames in os.walk(path):
#     print("Current Path:",dirpath)
#     print("Directories:",dirnames)
#     print("Files:",filenames)
#     print()

# for x,y,z in os.walk(path):
#     print("Current Path:",x)
#     print("Directories:",y)
#     print("Files:",z)
#     print()

# file_path=os.path.join(os.getcwd(),"new_file.txt")
# print(file_path)

# Outpus "test.txt"
# print(os.path.basename("/tmp/test.txt")) 

# Outpus "/tmp"
# print(os.path.dirname("/tmp/test.txt")) 

# Outputs tuple "('/tmp', 'test.txt')"
# print(os.path.split("/tmp/test.txt"))

# Outputs boolean False
# print(os.path.exists("/tmp/test.txt")) 

# Outputs boolean False(not a directory)
# print(os.path.isdir("/tmp/test.txt")) 

# Outputs boolean if file AND exists
# print(os.path.isfile("/tmp/test.txt")) 

# Outputs "('/tmp/test', '.txt')"
# print(os.path.splitext("/tmp/test.txt")) 

# Prints all functions in OS module
# print(dir(os.path)) 
