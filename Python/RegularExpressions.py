####
###Checks to see if the parameter is a valid phone number
###
##def IsPhoneNumber(text):
##    
##    size = len(text)
##
##    if size != 12:
##        return False
##
##    for index in range(0, 3):
##        #.isdecimal checks a string value to see if its a number
##        if (text[index].isdecimal()) == False:
##            return False
##
##    if text[3] != '-':
##        return False
##    
##    for index in range(4, 7):
##        if (text[index].isdecimal()) == False:
##            #input('In False')
##            return False
##        
##    if text[7] != '-':
##        return False
##    
##    for index in range(8, 12):
##        if (text[index].isdecimal()) == False:
##            #input('In False')
##            return False
##        
##    return True
##
##def main():
##    
##    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
##    numberList = []
##
##    for index in range (len(message)):
##        chunk = message[index : index + 12]
##        
##        if IsPhoneNumber(chunk):
##            print('Phone number found: ' + chunk)
##            numberList.append(chunk)
##            
##    print('This is the list')
##    print(numberList)
##
##main()
        
        
#The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python to match the same text the previous
#isPhoneNumber() function did: a string of three numbers, a hyphen, three more numbers,
#another hyphen, and four numbers. Any other string would not match
#the \d\d\d-\d\d\d-\d\d \d\d regex.
#But regular expressions can be much more sophisticated. For example, adding a 3 in curly
#brackets ({3}) after a pattern is like saying, “Match this pattern three times.” So the
#slightly shorter regex \d{3}-\d{3}-\d{4} also matches the correct phone number format.


#Creating REGEX objects
import re

#Stores resulting regex object into phoneNumRegex - The r means raw string
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')#re.compiler(r'\d\d\d-\d\d\d-\d\d\d\d)

#Result of the search gets stored in match
match = phoneNumRegex.search('My number is 666-555-4242.')

print('Phone number found: ' + match.group())


#Say you want to separate the area code from the rest of the phone number. Adding
#parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d). Then
#you can use the group() match object method to grab the matching text from just
#one group.

#Notice the parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phoneNumRegex.search('My number is 415-555-4242.')
print(match.group(1))#415, Isolate the area code
print(match.group(2))#555-4242, Rest of number
print(match.group())#415-555-4242, Entire number
print(match.groups())#('415', '555-4242'), Retrieve all the groups at once


#
##The | character is called a pipe. You can use it anywhere you want to match one of
#many expressions. For example, the regular expression r'Batman|Tina Fey' will match
#either 'Batman' or 'Tina Fey'. When both Batman and Tina Fey occur in the searched
#string, the first occurrence of matching text will be returned as the Match object. 

#Creating a regex object 
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())#Batman

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())#Tina Fey

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())#Batmobile
print(mo.group(1))#mobile
