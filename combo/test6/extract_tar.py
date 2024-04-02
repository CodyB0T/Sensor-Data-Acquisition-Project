import tarfile
import os
import subprocess


def get_path_for_WSL():
    # Get the current working directory
    current_directory = os.getcwd()
    # remove all /
    dir = current_directory.split("\\")
    # remove the c: drive part
    dir.pop(0)
    # remake the string with / inbetween
    directory = ""
    for x in dir:
        directory += x + "/"
    # add
    return f"/mnt/c/{directory}data/raw_data"


# Path to the tar archive
tar_file_path = "data/raw_data.tar"
extract_dir = "data/raw_data"

# Open the tar archive for reading
with tarfile.open(tar_file_path, "r") as tar:
    # Extract all files to the current directory
    tar.extractall(path=extract_dir)
    file_names = tar.getnames()

# Print the list of file names
for file_name in file_names:
    print(file_name)


# Path to the directory
directory_path = "data/raw_data"

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Print the list of file names
lzo_list = []
for file in files:
    if "lzo" in file:
        lzo_list.append(file)

print(lzo_list)


print(get_path_for_WSL())

import subprocess

# Commands to run in WSL
commands = f"wsl lzop -d {get_path_for_WSL()}/{lzo_list[0]} && wsl lzop -d {get_path_for_WSL()}/{lzo_list[1]}"
# print(commands)
# Run the commands in the WSL terminal
result = subprocess.run(commands, capture_output=True, text=True, shell=True)

# Print the output
# print(result.stdout)
print("done")
