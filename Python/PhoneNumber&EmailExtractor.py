'''
Created on Mar 5, 2017

@author: Luis
'''
import pyperclip
import re

#findevery phone number and email address in a long web page or document

emailRegex = re.compile(r'''(
    ([.a-zA-Z0-9!#\$%\^&*]+)
    @
    (\w+\.\w+)
    )''', re.VERBOSE)
matchObject = emailRegex.search('L.DRIVER.escobar666!^@yahoo.com')
print(matchObject.group())

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (s|-|\.)?
    \d{3}
    (s|-|\.)?
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''', re.VERBOSE)
matchObject = phoneRegex.search('(714)-222-8402')
print(matchObject.group())
