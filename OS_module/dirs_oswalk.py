import os

spath=os.getcwd()
print(os.listdir(spath))

# # Get everything split
# for root,dirs,files in os.walk(spath):
#     for file in files:
#         print("File = %s"%file)

#Roots
roots=next(os.walk(spath))[0]
print("Roots = %s"%roots)

#Dirs
dirs=next(os.walk(spath))[1]
print("Dirs = %s"%dirs)

#Files
files=next(os.walk(spath))[2]
print("Files = %s"%files)

# #Roots
# x=next(os.walk(spath))[0]
# print("Roots = %s"%x)

# #Dirs
# y=next(os.walk(spath))[1]
# print("Dirs = %s"%y)

# #Files
# z=next(os.walk(spath))[2]
# print("Files = %s"%z)