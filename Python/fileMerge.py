from datetime import datetime
import os

# Form the file name as a time stamp of the current time.
delta = datetime.now()
curr_time = delta.strftime("%Y-%m-%d-%H-%M-%S-%f")
merged_file_name = curr_time + '.txt'

# dir_path = root location
# file_name = name of the file
# file_dir = where the files are located.
dir_path, file_name = os.path.split(os.path.abspath(__file__))
file_dir = dir_path + r'\sec2Files'

# Get all the files within this file directory.
files_within_dir = os.listdir(file_dir)

# Open the new file
# Iterate through all the files within the directory.
# If the files end with a .txt
# Open the file & read the data, then write it to the new file.
with open(merged_file_name, 'w') as my_merged_file:
    for f in files_within_dir:
        if f.endswith('.txt'):
            data_url = open(file_dir + '\\' + f)
            data = data_url.read() + '\n'
            my_merged_file.write(str(data))
