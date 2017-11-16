'''
Created on Mar 14, 2017

@author: Luis
'''

import re, os, zipfile, random, shutil
from random import randint

#print(os.getcwd())
#pause = input()

##
#Regular expressions to capture EU/US date formates
#
EUDateRegex = re.compile('''(
                          ((0|1)?\d)     #DD
                          [-/.\s]        #Spacer
                          ((1|2|3)?\d)   #MM
                          [-/.\s]        #Spacer 
                          ((1|2)\d{3})   #YYYY
)''', re.VERBOSE)

USDateRegex = re.compile('''(
                          ((1|2|3)?\d)   #MM
                          [-/.\s]        #Spacer
                          ((0|1)?\d)     #DD
                          [-/.\s]        #Spacer 
                          ((1|2)\d{3})   #YYYY
)''', re.VERBOSE)
##

#Make a ZIP file - Dates.zip
ZipFileObject = zipfile.ZipFile('ImportFiles.zip', 'w')#Create a ZIP file
    
#Make 10 American stype dates
for index in range(10):
    
    #Ensure different type of files
    if(index < 3):
        endString = '.txt'
    elif(index < 7):
        endString = '.docx'
    else:
        endString = '.pdf'
    
    #Create random files to parse through. Will create valid & invalid dates.
    fileTitle = str(str(random.randint(0,1))            #MONTH
                    + str(random.randint(1,9)) + '.'    #MONTH
                    + str(random.randint(0,3))          #DAY
                    + str(random.randint(1,9)) + '.'    #DAY
                    + str(random.randint(1,2))          #YEAR
                    + (str(random.randint(0,9)) * 3)    #YEAR
                    + endString)
    #Create the file.
    fileObject = open(fileTitle, 'w') 
    
    #Write the new file into the zip using the files directory 
    ZipFileObject.write(fileObject.name, compress_type=zipfile.ZIP_DEFLATED)
    
    fileObject.close()
    
    #Delete the file by its directory.
    os.unlink(fileObject.name)
    
#Make 10 EU stype dates
for index in range(10):
    
    #Ensure different type of files
    if(index < 3):
        endString = '.txt'
    elif(index < 7):
        endString = '.docx'
    else:
        endString = '.pdf'
    
    #Create random files to parse through. Will create valid & invalid dates.
    fileTitle = str(str(random.randint(0,3))            #DAY
                    + str(random.randint(1,9)) + '.'    #DAY
                    + str(random.randint(0,1))          #MONTH
                    + str(random.randint(1,9)) + '.'    #MONTH
                    + str(random.randint(1,2))          #YEAR
                    + (str(random.randint(0,9)) * 3)    #YEAR
                    + endString)
    #Create the file.
    fileObject = open(fileTitle, 'w') 
    
    #Write the new file into the zip using the fileObject directory (.name)
    ZipFileObject.write(fileObject.name, compress_type=zipfile.ZIP_DEFLATED)
    
    fileObject.close()
    
    #Delete the file by its directory.
    os.unlink(fileObject.name)
    
ZipFileObject.close()


##
#DONE MAKING THE RANDOM FILES (PASSES AND FAILS BOTH)
##

##
#Code to open a zip file that already exists and extract all its content.
#works
#
ZipFileObject = zipfile.ZipFile('ImportFiles.zip', 'r')
print('opened')

#Extracts to the current working directory. Would extract to passed
#parameter diretory if given.
ZipFileObject.extractall()
print('extractall')

ZipFileObject.close()
print('closed')




index = 0


#Will cycle through all the files within the working directory
for filename in os.listdir():
    index += 1

    if filename.endswith('.docx'):
        osWalkPath = str(os.getcwd()) + '\\' + filename

        os.rename(filename, 'NewMode' + str(index) + '.txt')
        print('File name: ' + filename)
        print('osWalk name: ' + osWalkPath)
        print()
        


pause = input('LAST PART OF THE CODE')
for names in ZipFileObject.namelist():

    ##
    # Regex findall. Returns a list of strings with all matches
    # 
    EUmatchStrList = EUDateRegex.findall(names)

    #Use the names variable to change the name of the file.
    #Since the code is in this for loop, we know the name has meet the
    #regex requirements.
    for matches in EUmatchStrList:
        print('matches[0]: ' + matches[0])
        print('names: ' + names)
        day = str(matches[0])
        print('os.getcwd(): ' + os.getcwd())
        print()
        
##    print('matchStrList: ' + str(matchStrList))
##    print('names: ' + names)
##    print()
##
##    EUValidDay = int(str(names[0] + names[1]))
##    print('EUValid: ' + str(EUValidDay))
##
##    EUValidMonth = int(str(names[3] + names[4]))
##    print('EUValidMonth: ' + str(EUValidMonth))
##
##    EUValidYear = int(str(names[6] + names[7] + names[8] + names[9]))
##    print('EUValidYear: ' + str(EUValidYear))
##    print()
##    print()

print('ALL THE NAMES')
    





    
##os.walk(path)
#Will walk through a file directory
#Current working directory will not change.
#
#works - walks the entire directory of supplied string path
for folderName, subfolders, filenames in os.walk('C:\\Users\\Luis\\workspace\\Files'):
     
    #String of the current folders name
    print('The current folder is ' + folderName)
 
    #List of strings of the folders in the current folder
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    #List of strings of the files in the current folder
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
 
    print('')





# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.
































