'''
Created on Mar 12, 2017

@author: Luis
'''

# #Windows uses '\' as root
# #Linxus & OS X uses '/' as root
# #Must handle both cases 
# #os.path.join() function is helpful to create strings for filenames. 
import os #To handle both cases !!!!
value = os.path.join('usr', 'bin', 'spam')
print(value)#usr\bin\spam
 
#Joins names from list of filenames to end of folders name
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('D:\\Files', filename))


##
#Get current working directory
#
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)#C:\Users\Luis\workspace\Files

#Would change working direct.
#changeDirectory = os.chdir('C:\\Windows\\System32')

##
#Absolute vs Relative pathse
#absolure - always begins with the root folder
#relative - relative to the programs current working dir.

##
#Make new folders 
#
os.makedirs('D:\\Files\\FromEclipse')#Works

#Will return a string of the abs. path of the argument.
path = 'D:\\Files\\FromEclipse'
absolutePath = os.path.abspath(path)

#Will return Triu if the argument is an abs. path 
print(os.path.isabs(path))#True
print(os.path.abspath('.'))

#will return a string of a relative path from the start path to path
os.path.relpath(path, start)

#Returns a string of everything that comes before the last 
#slash in the path argument
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))#('C:\\Windows\\System32', 'calc.exe')

##
#File sizes and folder contents
#

# Will return the size in bytes of the filein the parth argument
print(os.path.getsize('D:\\Files'))#0
#Will return a list of filename strings for each file in the
#path argument
print(os.listdir('D:\\Files'))#['FromEclipse']

#Get size in byes of all the files in the directory
totalSize = 0
for filename in os.listdir('D:\\BACKUP'):
    totalSize += os.path.getsize(os.path.join('D:\\BACKUP', filename))
print(totalSize)#8192

##
#Checking path validity
#Great to see if there exists a DVD player or a USB 
#

#Will return True if the file or folder in the argument exists
print(os.path.exists('D:\\BACKUP'))#True

#Will return True if the path argument exists & is a file
print(os.path.isfile('D:\\BACKUP'))#False

#Will return True if the path argument exists & is a folder
print(os.path.isdir('D:\\BACKUP'))#True

##
#File Reading/Writting
#the open() function returns a File object
#Plainttext files - only contain basic test chars
#Binary Files - all other file types
#

#Will open the file in read mode by default
fileObject = open('C:\\Users\\Luis\\workspace\\Files\\hello.txt')

#Will open the file in read mode by explicit argument call
fileObject = open('C:\\Users\\Luis\\workspace\\Files\\hello.txt', 'r')

fileObjectContent = fileObject.read()
print(fileObjectContent)#Reading from hello.txt - congratz

fileObject = open('C:\\Users\\Luis\\workspace\\Files\\readLines.txt', 'r')
fileObjectContent = fileObject.readlines()
print(fileObjectContent)#Returns a str list of all the lines with \n @ end
                        #EXCEPT no \n for the last line
                        
#Write mode will override existing file
#If file not present will create it by default
fileObject = open('C:\\Users\\Luis\\workspace\\Files\\fileFromEc.txt', 'w')
fileObject.write('Writting from eclipse into the file')
fileObject.close()

#Append mode will add to the existing file
fileObject = open('C:\\Users\\Luis\\workspace\\Files\\fileFromEc.txt', 'a')
fileObject.write('\nAppending from eclipse into the file')
fileObject.close()

#Read the file
fileObject = open('C:\\Users\\Luis\\workspace\\Files\\fileFromEc.txt', 'r')
content = fileObject.read()
print(content)#works

# TO SAVE DATA FROM MY PYTHON PROGRAMS ~~~~
#Savings variables in your pythin programs to binary shelf files, this way 
#I can restore data to variables from the hard drive.
#After running the code below I will see 3 new files; mydata.bak,
#mydata.dat & mydata.dir
#These files will contain the data I stored in my shelf

 
import shelve
shelfFileVariable = shelve.open('mydata')#Pass in a filename and store 
                                         #into variable
cats = ['Zophie', 'Pooka', 'Simon'] #Lists of cat names

#Key = Value | Dictionary functionality
shelfFileVariable['cats'] = cats #Can make changes to shelf value as if it
                                 #were a dictionary. We are storing the 
                                 #list of cat names as a value associated
                                 #with the key 'cats' (like a dict.)
shelfFileVariable.close()

shelfFile = shelve.open('mydata')
newCatListKeys = list(shelfFile.keys())#returns all the keys 
print(newCatListKeys)#['cats']

newCatListValues = list(shelfFile.values())
print(newCatListValues)#[['Zophie', 'Pooka', 'Simon']]

shelfFileVariable.close()


##
#pprint.pprint() -will "pretty print" the contents of a list or dictionary to the screen
#pprint.pformat() - will return this same text as a string instead of printing it
#pprint.pformat() will give you a string that you can write to a .py file
#this file will be my own module that I can import whenever I want to use 
#the variables stored on it
#
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObject = open('myCats.py', 'w')
fileObject.write('cats = ' + pprint.pformat(cats) + '\n')
fileObject.close()

import myCats
print(myCats.cats)#[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
print(myCats.cats[0]['name'])#Zophie








































