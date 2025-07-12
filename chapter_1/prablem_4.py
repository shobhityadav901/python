import os 
# Function to get the list of files in a directory
directory_path = '/'
contents = os.listdir(directory_path) # Get the list of files and directories in the specified path 
for item in contents:
    print(item)
