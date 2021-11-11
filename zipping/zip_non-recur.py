from zipfile import ZipFile
import os

def get_all_file_paths(directory):
    # Initialize empty file paths list
    file_paths=[]
    # Crawl through directories and subdirectories
    for root,directories,files in os.walk(directory):
        for filename in files:
            # Join the 2 strings in order to form the full file path
            filepath=os.path.join(root,filename)
            file_paths.append(filepath)
    # Return all file paths
    return file_paths

def main():
    # Path to folder that needs to be zipped
    directory="./images"
    # directory=os.getcwd()
    # Calling function to get all file paths in the directory
    file_paths=get_all_file_paths(directory)
    # Printing the list of all files to be zipped
    print("Following files will be zipped in this program: ")
    for file_name in file_paths:
        print(file_name)
    # Writing files to a zipfile
    with ZipFile("my_files.zip", 'w') as zip:
        # Writing each file 1 by 1
        for file in file_paths:
            zip.write(file)
    print("All files zipped successfully!")

# Call main function
if __name__=="__main__":
    main()
