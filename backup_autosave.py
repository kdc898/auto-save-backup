# Import the following modules
import shutil
import datetime 
import time
import hashlib
import os
import sys

def calculate_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

# Function for performing the backup of the files and folders
def backup_files(src_file_name, 
                dst_file_name=None,
                src_dir='', 
                dst_dir=''):
    src_path = ''
    try:
      
          # Extract the date and time
        date_format = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M_')

        # If user did not enter any source file then give the error message
        if not src_file_name:
            print("Please give the Source File Name")
            exit()

        # Make the source directory where we want to backup our files
        if not src_dir:
            src_path = src_file_name
        else:
            src_path = src_dir + src_file_name

        try:
          
            # If user provides all the inputs
            if src_file_name and dst_file_name and src_dir and dst_dir:
                src_path = src_dir+src_file_name
                dst_dir = dst_dir+dst_file_name
    
            # When User Enter Either 'None' or empty String ('') for dst_file_name
            elif dst_file_name is None or not dst_file_name:
                dst_file_name = src_file_name
                dst_dir = dst_dir+date_format+dst_file_name
                
            # When user Enter an empty string with one or more spaces (' ')
            elif dst_file_name.isspace():
                dst_file_name = src_file_name
                dst_dir = dst_dir+date_format+dst_file_name
                
            #if destination is not specified, save in the same directory as the source
            elif dst_dir is None or not dst_dir or dst_dir.isspace():
                if dst_file_name is None or not dst_file_name or dst_file_name.isspace():
                    dst_file_name = src_file_name
                    dst_dir = dst_dir+date_format+dst_file_name
                else:
                    dst_dir = src_dir + dst_file_name

            # When user Enter a name for the backup copy
            else:
                dst_dir = dst_dir+dst_file_name

            #copy the files from source to destination
            shutil.copy2(src_path, dst_dir)

            print("Backup Successful!")
            print("time: " + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M_'))

        except FileNotFoundError:
            print("File does not exists!,\
            please give the complete path")
    
    # When we need to backup the folders only...
    except PermissionError:  
        dst_dir = dst_dir+date_format+dst_file_name
        
        # Copy the whole folder from source to destination
        shutil.copytree(src_file_name, dst_dir)

def autosave(src_file_name, 
                dst_file_name=None,
                src_dir='', 
                dst_dir='', numCopies=1, saveInterval=300):
    last_hash = calculate_file_hash(src_file_name)
    #TODO: make this into a variable
    dst_file_2 = "Illustration34_bak2.clip"
    firstrun = True
    try:
        while True:
            current_hash = calculate_file_hash(src_file_name)
            if current_hash != last_hash:
                print("File has changed! Backing up file.")
                if firstrun:
                    print("First run!")
                    backup_files(src_file_name, dst_file_name, src_dir, dst_dir)
                else:
                    #move current most recent saved version to second place
                    backup_files(dst_file_name, dst_file_2, dst_dir, dst_dir)
                    backup_files(src_file_name, dst_file_name, src_dir, dst_dir)
                last_hash = current_hash
                firstrun = False
            time.sleep(saveInterval) 
            
    except KeyboardInterrupt:
        print("\nAuto-saver stopped by user.")

# Call the function
source_path = "C:/Users/kdc89/Pictures/ref_pics/studies/"
source_file = "C:/Users/kdc89/Pictures/ref_pics/studies/Illustration34.clip"
dest_path = source_path + "backup/"
#backup_files(source_file, "Illustration33_bak.png", None, dest_path)
autosave(source_file, "Illustration34_bak.clip", None, dest_path, 2, 10)
