# Import the following modules
import shutil
import datetime 
import time
import hashlib
import os
import sys

def fileNumeral(filename, numeral):
     parts = filename.split(".")
     whole = parts[0] + str(numeral) + '.' + parts[1]
     return whole

def calculate_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

# Function for performing the backup of the files and folders
def backup_files(src_file_name, 
                dst_file_name,
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
    if src_dir is None or not src_dir or src_dir.isspace():
        print('')
    else:
        src_file_name = src_dir + src_file_name

    last_hash = calculate_file_hash(src_file_name)

    #if the backup file name is not specified, use the source file name + '_bak'
    if dst_file_name is None or not dst_file_name or dst_file_name.isspace():
        dst_file_name += '_bak'    

    namelist = [dst_file_name]
    runcount = 0
    try:
        while True:
            print('runcount: ' + str(runcount))
            current_hash = calculate_file_hash(src_file_name)
            if current_hash != last_hash:
                print("File has changed! Backing up file.")
                #if this is the first run, we have only 1 file name
                if(runcount == 0):
                    print(src_file_name + ',  ' + namelist[0])
                    backup_files(src_file_name, namelist[0], dst_dir = dst_dir)
                #if the loop has run fewer times than the specified number of copies, add names to the namelist
                elif (0 < runcount < numCopies):
                    namelist.append(fileNumeral(dst_file_name, runcount))
                    for i in range(len(namelist)-1, 0, -1):
                        print(namelist[i] + ', ' + namelist[i-1])
                        backup_files(namelist[i-1], namelist[i], dst_dir)
                    backup_files(src_file_name, namelist[0], dst_dir = dst_dir)
                #all names are in the list; run the update for each file
                else:
                    #move current most recent saved version to second place
                    for i in range(len(namelist)-1, 0, -1):
                        print(namelist[i] + ', ' + namelist[i-1])
                        backup_files(namelist[i-1], namelist[i], dst_dir)
                    backup_files(src_file_name, namelist[0], dst_dir = dst_dir)
                
                last_hash = current_hash
                if (runcount < numCopies):
                    runcount += 1
            time.sleep(saveInterval*60) 
            
    except KeyboardInterrupt:
        print("\nAuto-saver stopped by user.")


# Call the function
codingPath = "C:/Users/kdc89/Documents/coding_work/"
codingFile = "namelist.py"
source_path = "C:/Users/kdc89/Pictures/ref_pics/studies/"

dest_path = source_path + "backup/"

autosave(codingFile, "namelist_backup.py", codingPath, dest_path, 3, 10)
