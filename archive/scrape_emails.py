# import required module
import os
from glob import iglob
# assign directory
directory = os.getcwd()
rootdir_glob = directory + '/**/*'
 
# iterate over files in
# that directory

# This will return absolute paths
file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]

for f in file_list:
    print(f) # Replace with desired operations

