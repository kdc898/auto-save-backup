# auto-save-backup
A repository for a python script to create iterative backups of a specified file.

# Initial features: 
``` python
autosave(codingFile, codingPath, backupName, dest_path, numBackups, timeInterval)
```
Takes file name, file path, backup file name, destination path, number of backup copies, and time interval as inputs. Checks the specified file after the given time interval. If there has been a change in the file in that time, it is saved under the backup file name. 

Iterative save: this program saves a specified number of backup copies. For example, if there are 3 backups, they would be backupName, backupName1, backupName2. File backupName is the most recent backup, while backupName2 is the oldest. This provides savepoints to return to. 

Further development:
Package project for install
Create a GUI for ease of use

Status:
5/24/26: added initial Python program that saves a backup of a specified file while in that same folder. 
More testing is needed for backups of folders.
The program only works when in the same folder or it throws 'File does not exists!,            please give the complete path'. 

5/27/26: Added path in if/else statement for when user provided a file name and source directory but not a destination directory.
Changed default save location of backup to location of the existing file rather than the code's working directory. Issue of program only working if in same folder as file now fixed.

6/18/26: Added functionality to save only when there are changes to the watched file, and create iterative backups as savepoints for digital art. Currently set to 2 backup files without any option for variation.

6/25/26: Updated to make the number of iterative save copies variable. Added helper function to name backup files by adding a numeral before the file type extension. Time between save checks is now variable.

7/1/26: Removed print statements 
