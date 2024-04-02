import tarfile

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
