import os

os.chdir("DIRECTORY_NAME")
current_path=os.getcwd()
counter=0

for dirpath,dirname,files in os.walk(current_path):
    for file in files:
        file_path=os.path.join(dirpath,file)
        suffix = ".jpg"
        os.rename(file_path, file_path+suffix)
        counter+=1

print("Files processed: %s"%(str(counter)))