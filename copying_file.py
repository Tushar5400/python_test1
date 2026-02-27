import os

# Taking Source file path as input from user

source_file_path = input("Enter Source file path:")

if(os.path.isfile(source_file_path)):
    # Extracting file name and extension
    src_file_with_ext = os.path.basename(source_file_path)
    src_file_name, src_file_ext = os.path.splitext(src_file_with_ext)

    print("file name:", src_file_name)
    print("file extension:", src_file_ext)

else:
    print("file not found")

# Taking Destination folder path as input from user

destination_folder_path = input("Enter Destination folder path:")
 
os.makedirs(destination_folder_path, exist_ok=True)
# joining destination folder path and source file 
new_file_path = os.path.join(destination_folder_path, src_file_name+src_file_ext)
# Reading source file
with open(source_file_path, "r") as src_file:
    data = src_file.read()
# creating new file and writing data
with open(new_file_path, "w") as new_file:
    new_file.write(data)

    print("file copied successfully")
    

        
        


