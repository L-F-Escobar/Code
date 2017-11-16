'''
Created on Mar 14, 2017

@author: Luis
'''
#REMOVE AT END
#import shutil, os, send2trash, zipfile

##
#Allows to copy, move, rename & delete files in my Python program.
#
import shutil#Shell utilites
import os

##shutil.copy(source, destination)
#Provides function to copy files and entire folders.
#Will copy the file at the path source to the folder at the path dest. 
#arguments are strings. Returns a string of the path copied file.
#
os.chdir('D:\\')
returnValue = shutil.copy('D:\\Pictures\\undo.png', 'D:\\test')#Works
#The return value is the path of the newly copied file
print(returnValue)#D:\test\undo.png
 
##shutil.copytree(source, destination)
#Will copy an entire folder and every folder and file contained in it.
#Source will copy folder into destination folder
#DESTINATION folder cannot exist
#
os.chdir('D:\\')
returnVale = shutil.copytree('D:\\Pictures', 'D:\\test')#works
print(returnVale)#D:\test
  
##shutil.move(source, destination) - CUT/PASTE mechanism
#Will move the fole or folder at source to path at destination and will 
#return a string of the absolure path of the new location.
#IF dest. points to a folder, the source file gets moved into dest and 
#keeps its current filename.
#File cannot exist at dest, gives runtime error
#returnValue = shutil.move('D:\\Pictures\\zion1.jpg', 'D:\\test')
#print(returnValue)#D:\test\zion1.jpg
#BUT - of the a file with the same name already exists, IT WOULD HAVE 
#BEEN OVERWRITTEN - WARNING
#

### ~~~ Permanently delete - unsafe - caustion required - disk space f~~~
##
#
 
##os.unlink(path)
#Will delete file at path
#

##os.rmdir(path)
#Will delete folder at path
#Folder must be empty for deletion to occur
#

##shutil.rmtree(path) 
#Will remove the folder at path & all the files & folders within
#

#This is code that is used to FIRST check which files we are looking to
#delete. Notice the unlink(filename) is commented out.
import os
for filename in os.listdir():
    if filename.endswith('.py'):
        #os.unlink(filename)
        print(filename)
 
## send2trash module - safe deletes - allows to be recovered later
#
import send2trash
testFile = open('testFile.txt', 'a') # creates the file
testFile.write('Bacon is not a vegetable.')
testFile.close()
send2trash.send2trash('testFile.txt')#Will send file to the recycling bin
 
##os.walk()
#Will walk through a file directory
#Current working directory will not change.
#
#works - walks the entire directory of supplied string path
for folderName, subfolders, filenames in os.walk('D:\\Extra_Download'):
     
    #String of the current folders name
    print('The current folder is ' + folderName)
 
    #List of strings of the folders in the current folder
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    #List of strings of the files in the current folder
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
 
    print('')

##Zip Files
#Can create, open & read ZIP files.
import zipfile
os.chdir('D:\\')
ZipFileObject = zipfile.ZipFile('D:\\Extra_Download\\AutomateTest.zip')
print(ZipFileObject.namelist())#
singleFile = ZipFileObject.getinfo('automate_online-materials/vampire2.py')
print(singleFile.file_size)#247 Gets file size
print(singleFile.compress_size)#138 Gets compressed file size
print('Compressed file is %sx smaller!' % (round(singleFile.file_size / singleFile.compress_size, 2)))
#Compressed file is 1.79x smaller! - calculates how efficiently zip is 
#compressed by dividing the original file size by the compressed file
#size.
ZipFileObject.close()
 
##
#Extracting from ZIP files
#
##extractall()
#method for Zip File Objects that extracts all the files and folders from
#a ZIP filw into the current working directory
#IF folder passed to extractall method does not exist, it will be created.
import zipfile, os
os.chdir('D:\\Extra_Download')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('AutomateTest.zip')
exampleZip.extractall()#can pass a folder name to extract all, if it 
#doesnt exist, it will be created.
exampleZip.close()#Works.
os.chdir('C:\\Users\\Luis\\workspace\\Files')#BACK TO MY WORKING DIR.

##
#Creating and adding to ZIP files
#Must open a ZipFile Object in write mode
#
#import zipfile
newZipFileObject = zipfile.ZipFile('new.zip', 'w')#Create a ZIP file
newZipFileObject.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
#Compress it using a compression type parameter
newZipFileObject.close()
#will erase all existing contents of a ZIP file 
