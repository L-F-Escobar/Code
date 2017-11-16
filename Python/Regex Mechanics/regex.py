'''
Created on Mar 4, 2017

@author: Luis
'''
import re


##
# Quick Review
#
#| either or
#? matches zero or one of the proceding group
#* matches zero or more of the proceding group
#+ matches one or more of the proceding group
#{n} matches exactly n of the proceding group
#{n, } matches n or more of the proceding group
#{ ,m} matches 0 to m of the proceding group
#{n,m} matches at least n and at more m of the proceding group
#{n,m}? or *? or +? performs a nongreedy match of the proceding group
#^spam means the string must begin with spam
#spam$ means the string must end with spam
#. matches any character, except newlines characters
#\d \w \s match a digit, word, space
#\D \W \S match anything except
#[abc} matches any character between the brackets
#[^abc} anything that isnt between the brackets




phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
matchObject = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + matchObject.group())#Phone number found: 415-555-4242
 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My number is 415-555-4242.')
print(matchObject.group(1))#415
 
areaCode, mainNumber = matchObject.groups()
print(str(areaCode) + '-' + str(mainNumber))#415-555-4242
 
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(matchObject.group(1))#(415)
print(matchObject.group(2))#555-4242
 
 
 
#                        Groups with the Pipe '|'
heroRegex = re.compile (r'Batman|Tina Fey')
matchObject1 = heroRegex.search('Batman and Tina Fey.')
print(matchObject1.group())#Batman
 
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())#Batmobile
print(mo.group(1))#mobile
 
 
##
#The (wo)? part of the regular expression means that the pattern wo 
#is an optional group. Will match Zero or one instance.
#or one instance of wo in it. 
#
batRegex = re.compile(r'Bat(wo)?man')
matchObject1 = batRegex.search('The Adventures of Batman')
print(matchObject1.group())#Batman
 
matchObject2 = batRegex.search('The Adventures of Batwoman')
matchObject2.group()
print(matchObject2.group())#Batwoman
 
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
matchObject1 = phoneRegex.search('My number is 415-555-4242')
print(matchObject1.group())#415-555-4242
 
matchObject1 = phoneRegex.search('My number is 555-4242')
print(matchObject1.group())#555-4242
 
##
# * (asterisk) means "Match zero or more"
#
batRegex = re.compile(r'Bat(wo)*man')
matchObject1 = batRegex.search('The Adventures of Batman')
print(matchObject1.group())#Batman
 
matchObject2 = batRegex.search('The Adventures of Batwoman')
print(matchObject2.group())#Batwoman
  
matchObject3 = batRegex.search('The Adventures of Batwowowowoman')
print(matchObject3.group())#Batwowowowoman
 
##
# + means "Match one or more"
#
batRegex = re.compile(r'Bat(wo)+man')
matchObject1 = batRegex.search('The Adventures of Batwoman')
print(matchObject1.group())#Batwoman
 
matchObject2 = batRegex.search('The Adventures of Batwowowowoman')
print(matchObject2.group())#Batwowowowoman
 
matchObject3 = batRegex.search('The Adventures of Batman')
print(matchObject3 == None)#True
 
##
# (Ha){3} will only match 'HaHaHa'
# (Ha){3,5} will match 3,4, or 5 'Ha'
# (Ha){3, } will match 3 or more
# (Ha){ ,5} will match zero to 5
#
 
greedyHaRegex = re.compile(r'(Ha){3,5}')#Creating a regrex search Object
matchObject1 = greedyHaRegex.search('HaHaHaHaHa')#Method of a regrex search object
print(matchObject1.group())#HaHaHaHaHa
 
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
matchObject2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(matchObject2.group())#HaHaHa
 
##
# The FINDALL() method
# Will return the strings of every match, instead of just the first like
# .search method
#
searchObjectRegrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')# has no groups
matchObject = searchObjectRegrex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(matchObject.group())#415-555-9999
 
searchObjectRegrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchStrList = searchObjectRegrex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(matchStrList)#['415-555-9999', '212-555-0000']
 
searchObjectRegrex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')# has groups
matchStrList = searchObjectRegrex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(matchStrList)#[('415', '555', '9999'), ('212', '555', '0000')]
 
 
##
#        CHARACTER CLASSES
#
#\d - Any number 0-9
#\D - !\d Any character that is not a digit from 0-9
#\w - Any letter, #, or underscore char. (words essentially)
#\W - !\w not a letter, digit or underscore char
#\s - Any space, tab, or newline (space essentially)
#\S - Any char that is not space
 
xmasRegex = re.compile(r'\d+\s\w+')
matchStrList = xmasRegex.findall('12 drummers, 11 pipers, 10 lords,' + 
                                ' 9 ladies, 8 maids, 7 swans, 6 geese,' + 
                                ' 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(matchStrList)#['12 drummers', '11 pipers', '10 lords', '9 ladies', 
                   #'8 maids', '7 swans', '6 geese', '5 rings', '4 birds', 
                   #'3 hens', '2 doves', '1 partridge']
 
##
#Creating my own character classes
# use '[]'
#[a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
#[aeiouAEIOU] will match vowels
#[^aeiouAEIOU] will match all characters that are not vowels
vowelRegex = re.compile(r'[aeiouAEIOU]')
matchStrList = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(matchStrList)#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
 
# '^' will make negative character class
# placed just after the characters class openings bracket
#
consonantRegex = re.compile(r'[^aeiouAEIOU]')
matchStrList = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(matchStrList)#['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 
                   #'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 
                   #'D', '.']
 
##
# (^) - carrot
# start of a regex to indicate a match must occure at the beginning
# ($) - dollar side
# at end of regex to indicate the string must end with the regex
#
beginsWithHello = re.compile(r'^Hello')
matchObject1 = beginsWithHello.search('Hello world!')
print(matchObject1)#<_sre.SRE_Match object; span=(0, 5), match='Hello'>
print(matchObject1 == None)#False
matchObject1 = beginsWithHello.search('He said hello.')
print(matchObject1 == None)#True
 
endsWithNumber = re.compile(r'\d$')
matchObject1 = endsWithNumber.search('Your number is 42')
print(matchObject1 == None)#False
print(matchObject1)#<_sre.SRE_Match object; span=(16, 17), match='2'>
matchObject1 = endsWithNumber.search('Your number is forty two.')
print(matchObject1 == None)#True
 
#Must begin and end using ^ and $
wholeStringIsNum = re.compile(r'^\d+$')
matchObject1 = wholeStringIsNum.search('1234567890')
print(matchObject1.group())#1234567890
print(matchObject1)#<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
 
##
# .(dot) character or wildcard
# will match any character except for a newline
#
atRegex = re.compile(r'.at')
matchStrList = atRegex.findall('The cat in the hat sat on the flat mat. asdatfsv')
print(matchStrList)#['cat', 'hat', 'sat', 'lat', 'mat', 'dat']
 
##
# Dot-Star (.*)
# takes in everything except a new line
#
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
matchObject = nameRegex.search('First Name: Al Last Name: Sweigart')
print(matchObject.group())#First Name: Al Last Name: Sweigart
print(matchObject.group(1))#Al
print(matchObject.group(2))#Sweigart
 
#Greedy & nonGreedy
nongreedyRegex = re.compile(r'<.*?>')
matchObject = nongreedyRegex.search('<To serve man> for dinner.>')
print(matchObject.group())#<To serve man>
 
greedyRegex = re.compile(r'<.*>')
matchObject = greedyRegex.search('<To serve man> for dinner.>')
print(matchObject.group())#<To serve man> for dinner.>

##
# re.DOTALL
# second argument to re.compile()
#
noNewlineRegex = re.compile('.*')
matchObject = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(matchObject.group())#Serve the public trust.

test = re.DOTALL
newlineRegex = re.compile('.*', )
matchObject = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(matchObject.group())
#Serve the public trust.
#Protect the innocent.
#Uphold the law.


#from regex import nameRegex

##
#re.I or re.IGNORECASE
#doesnt matter whether letters are lower/uppercase
#
robocop = re.compile(r'robocop', re.I)
matchObject = robocop.search('RoBOcoP is part man, part machine, all cop.')
print(matchObject.group())#RoBOcoP

##
#sub() method
#substitue new text in place of the regex pattern
#returns a string
#
namesRegex = re.compile(r'Agent \w+')
matchStr = namesRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.')
print(matchStr)#CENSORED gave the secret document to CENSORED.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
matchStr = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol'
                               + ' that Agent Eve knew Agent Bob was a '
                               + ' double agent.')
print(matchStr)

##
#re.verbose
#
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
matchObject = phoneRegex.search('714-545-8971 ext. 666')
print(matchObject.group())#714-545-8971 ext. 666

##
#bitwise or operator
#allows me to use re.verbose re.ignore & re.compile together
#
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)





