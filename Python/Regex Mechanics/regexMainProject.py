'''
Created on Mar 5, 2017

@author: Luis
'''
import pyperclip
import re

entireText = pyperclip.paste()#Reads from clipboard
emails = []
phoneNumbers = []

emailRegex = re.compile(r'''(
    ([.a-zA-Z0-9!#\$%\^&*]+)
    @
    (\w+\.\w+)
    )''', re.VERBOSE)

phoneRegex = re.compile(r'''(
    (\+\d)?                         #Leading country code
    (\s|-|\.)?                       #Space
    (\d{3}|\(\d{3}\))?              #Area code
    (\s|-|\.)?                       #Space
    \d{3}                           #3 digits
    (\s|-|\.)?                       #Space
    \d{4}                           #4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    #Extension
    )''', re.VERBOSE)

lines = entireText.split('\n')

for singleLine in lines:
    print(singleLine)
    pause = input('START')
    
    try:
        emailMatchObject = emailRegex.search(singleLine)
        phoneNumberMatchstring = phoneRegex.findall(singleLine)
        
        
        if(emailMatchObject != None):
            emails.append(str(emailMatchObject.group()))
            
        if(phoneNumberMatchstring != ''):
            phoneNumbers.append(phoneNumberMatchstring)
            print('Phone number found')
            print(phoneNumberMatchstring)
            
    except AttributeError:
        print('No emails and/or phone numbers present in this line of text')
    except NameError:
        print('Name error')
        
    pause = input('END\n')
                  
##for singleEmail in emails:
##    print('Email: ' + singleEmail)
##    pause = input('Second For End\n\n')
print(emails)
print()

for singleNumber in phoneNumbers:
    print('Phone#: ' + str(singleNumber))
    pause = input('Second For End\n\n')
print(phoneNumbers)
