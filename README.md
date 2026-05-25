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
