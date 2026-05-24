# Import the following modules
import shutil
import datetime 
import os
import sys

# TODO: change directory file path
#os.chdir(sys.path[0])  

# Function for performing the
# backup of the files and folders
def backup_files(src_file_name, 
                dst_file_name=None,
                src_dir='', 
                dst_dir=''):
    try:
      
          # Extract the date and time
        date_format = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M_')

        # Make the source directory where we wanna backup our files
        src_dir = src_dir+src_file_name

        # If user did not enter any source file then give the error message
        if not src_file_name:
            print("Please give atleast the Source File Name")
            exit()

        try:
          
            # If user provides all the inputs
            if src_file_name and dst_file_name and src_dir and dst_dir:
                src_dir = src_dir+src_file_name
                dst_dir = dst_dir+dst_file_name
    
            # When User Enter Either 'None' or empty String ('') for dst_file_name
            elif dst_file_name is None or not dst_file_name:
                dst_file_name = src_file_name
                dst_dir = dst_dir+date_format+dst_file_name
                
            # When user Enter an empty string with one or more spaces (' ')
            elif dst_file_name.isspace():
                dst_file_name = src_file_name
                dst_dir = dst_dir+date_format+dst_file_name
                
            # When user Enter a name for the backup copy
            else:
                dst_dir = dst_dir+date_format+dst_file_name

            #copy the files from source to destination
            shutil.copy2(src_dir, dst_dir)

            print("Backup Successful!")
        except FileNotFoundError:
            print("File does not exists!,\
            please give the complete path")
    
    # When we need to backup the folders only...
    except PermissionError:  
        dst_dir = dst_dir+date_format+dst_file_name
        
        # Copy the whole folder from source to destination
        shutil.copytree(src_file_name, dst_dir)

# Call the function
backup_files("Illustration34.clip")  
