import os

current_path=os.getcwd()

check_exist=input("Enter file to check:")
counter=0

for dirpath,dirname,files in os.walk(current_path):
    #  print(type(files))
    for file in files:
        # print(type(file))
        if file==check_exist:
            file_path=os.path.join(dirpath,file)
            print("Deleting:",file_path)
            os.remove(file_path)
            counter+=1

print(counter, "number of files found, then deleted.")
