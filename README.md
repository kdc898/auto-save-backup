# auto-save-backup
A repository for a project to automatically back up digital art projects.

This will be a python script to automatically create a back-up of an in progress digital art project, specifically .clip files as I use Clip Studio Paint. 

Initial features: 
Take an existing file as an input. Save under a designated secondary file name every five minutes if there has been a change to the file in that time.

Further development:
Ensure compatibility with other file types such as .psd
Save older versions to other files as savepoints 
Create a GUI for ease of use

Status:
5/24/26: added initial Python program that saves a backup of a specified file while in that same folder. 
More testing is needed for backups of folders.
The program only works when in the same folder or it throws 'File does not exists!,            please give the complete path'. 

5/27/26: Added path in if/else statement for when user provided a file name and source directory but not a destination directory.
Changed default save location of backup to location of the existing file rather than the code's working directory. Issue of program only working if in same folder as file now fixed.

6/18/26: Added functionality to save only when there are changes to the watched file, and create iterative backups as savepoints for digital art. Currently set to 2 backup files without any option for variation.

6/25/26: Updated to make the number of iterative save copies variable. Added helper function to name backup files by adding a numeral before the file type extension. Time between save checks is now variable.
