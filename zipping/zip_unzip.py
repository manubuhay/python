import zipfile
import os

# Zip files in folder x to testzip.zip
folder_tobe_zipped="./to_zip"
with zipfile.ZipFile("testzip.zip",'w',zipfile.ZIP_DEFLATED) as newzip:
    for dirpath,dirnames,files in os.walk(folder_tobe_zipped):
        for file in files:
            newzip.write(os.path.join(dirpath,file))

# Unzip files from testzip.zip to new_unzipped
folder_tobe_unzipped="./unzipped"
with zipfile.ZipFile("testzip.zip",'r') as zip_ref:
    zip_ref.extractall(folder_tobe_unzipped)