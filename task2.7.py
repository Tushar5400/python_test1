import os 
# Taking file name as input from user
file_path = input("Enter File Name:")

#Extracting file name and extension
file_name, file_extension = os.path.splitext(file_path)

#Destination folder
destination_folder = input("Enter Destination folder:")

#Create destination folder if doesn't exist
os.makedirs(destination_folder, exist_ok=True)


# joining destintion folder and file name 

new_file_path = os.path.join(destination_folder, file_name+file_extension)

#Create new file
with open(new_file_path, "w") as file:
    file.write("This is the new file created using python!")
    print("file created successfully at :", new_file_path)

