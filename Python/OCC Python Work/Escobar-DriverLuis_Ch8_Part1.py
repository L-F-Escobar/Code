###Ch08 Section 1 Part 1
##
##from re import split
##
###readWords(str1)
### @param  : a string value from main
### @return : a set of unique letters from a string in main
###
##def readWords(str1):
##    
##    #Creating an empty set
##    wordSet = set()
##    #Splitting str1 into a list of seperate words : delimiter = white space
##    words = str1.split()
##
##    #One word at a time from the list of words
##    for word in words:
##        
##        #Split each word into parts by the "[...]" delimiter   
##        parts = split("[0-9.!?/']+",word)
##        #Convert the parts list into a string to traverse one letter at a time
##        parts = str(parts)
##        #Make all letters that may exist lower case
##        parts = parts.lower()
##        
##        #For each letter in the part
##        for letter in parts:
##            
##            #If the letter is >= 'a' add it to a set 
##            if letter >= 'a':
##                
##                wordSet.add(letter.lower())
##                
##    #Return the set            
##    return wordSet
##
###main()
### @param  : <none>
### @return : letters from a string converted into a set through a func. call
###
##def main():
##    
##    #Create an empty set
##    wordSet = set()
##    #Random string
##    stringOne = "Lucifer, show us the light; O Mighty-One, king of the sky!"
##    #Func. call and save return value into the empty set
##    wordSet = readWords(stringOne)
##    #Print
##    print(wordSet, end="")
##    print(': There are', len(wordSet), 'unique letters')
##    
###Function call 
##main()
##
##
##
###Ch08 Section 1 Part 2
###lettersInBoth(str1,str2)
### @param  : 2 static strings from main
### @return : 1 intersection set of the 2 passed strings converted into sets
###
##def lettersInBoth(str1, str2):
##    #Turning the strings into sets through a function call 
##    cast1 = letters(str1)
##    cast2 = letters(str2)
##
##    #Grabbing the intersection of the two sets
##    intersectionSet = cast1.intersection(cast2)
##    #Return the intersection set
##    return intersectionSet
##
###letters(str1)
### @param  : 1 string to be converted into a set
### @return : 1 set of the passed string
###
##def letters(str1):
##    #Converting a string into a set
##    castString = set(str1)
##    #Return the set
##    return castString
##
###main()
### @param  : <none>
### @return : the intersection of 2 sets
###
##def main():
##    #Creating 3 empty sets
##    cast1 = set()
##    cast2 = set()
##    intersectionCast = set()
##
##    #2 random static strings
##    string1 = 'abcDefghikznP'
##    string2 = 'abfDEfGHiKzNP'
##
##    #Function call to get the intersection of 2 strings
##    intersectionCast = lettersInBoth(string1,string2)
##    #Print result
##    print(intersectionCast)
##    
###Call main  
##main()
##
##
##
###Ch08 Section 1 Part 3
##
###notInEither(str1,str2)
### @param  : 2 static strings from main
### @return : 1 intersection set of the 2 passed strings converted into sets
###
##def notInEither(str1, str2):
##    
##    #Set with the letters of the alphabet
##    castAZ = {'a','b','c','d','e','f','g','h','i','j','k'
##              ,'l','m','n','o','p','q','r','s','t','u','v'
##              ,'w','x','y','z'}
##    #Turning both strings into sets of only the lower case
##    #strings.
##    cast1 = letters(str1)
##    cast2 = letters(str2)
##    #Forcing a union of both lower case sets 
##    unionCast = cast1.union(cast2)
##    #Difference between castAZ & unionCast
##    mainCast = (castAZ.difference(unionCast))    
##    
##    #Returning the lower case union set
##    return mainCast
##
##
###letters(str1)
### @param  : 1 string to be converted into a set
### @return : 1 set of the passed string
###
##def letters(str1):
##
##    lowerStr1 = ""
##    #For each letter in str1
##    for index in str1:
##        #If the letter is lower add it to a new string
##        if index.islower():
##            lowerStr1 = lowerStr1 + index
##    #Then convert the new lower string into a set
##    castString = set(lowerStr1)
##    
##    #Return the set
##    return castString
##
###main()
### @param  : <none>
### @return : the intersection of 2 sets
###
##def main():
##    #Creating 3 empty sets
##    cast1 = set()
##    cast2 = set()
##    neitherCast = set()
##
##    #2 random static strings
##    string1 = 'abcdefgABCDE'
##    string2 = 'hijklmnopqursHIJKL'
##
##    #Function call to get the intersection of 2 strings
##    neitherCast = notInEither(string1,string2)
##    #Print result
##    print(neitherCast)
##    
###Call main  
##main()
##
##
##
##
###Ch08 Section 1 Part 4
##
###nonLettersBoth(str1,str2)
### @param  : 2 static strings from main
### @return : 1 intersection set of the 2 passed strings converted into sets
###
##def nonLettersBoth(str1, str2):
##    
##    #Turning both strings into sets of only the lower case
##    #strings.
##    cast1 = letters(str1)
##    cast2 = letters(str2)
##    intersectionCast = {}
##    #contains all of the elements that are in both sets
##    intersectionFlag = cast1.intersection(cast2)
##    
##    #Returning the lower case union set
##    return intersectionFlag
##
##
###letters(str1)
### @param  : 1 string to be converted into a set
### @return : 1 set of the passed string
###
##def letters(str1):
##    #Make the string a list
##    vassel = list(str1)
##    strVassel = ""
##
##    #Checks if a letter
##    for letter in vassel:
##        if letter.isalpha():
##            continue
##        #If not a letter add to a new string
##        else:
##            strVassel = strVassel + letter
##            
##    #Make the new string a set
##    castString = set(strVassel)
##    
##    #Return the set
##    return castString
##
###main()
### @param  : <none>
### @return : the intersection of 2 sets
###
##def main():
##    #Creating 3 empty sets
##    cast1 = set()
##    cast2 = set()
##    intersectionFlag = set()
##
##    #2 random static strings
##    string1 = 'abcd&*efg'
##    string2 = 'hijkll&xr&$*'
##
##    #Function call to get the intersection of 2 strings
##    intersectionFlag = nonLettersBoth(string1,string2)
##    #Print result
##    print(intersectionFlag)
##    
###Call main  
##main()
##fibonacci = {}
##primes = {}
##both = {}
fibonacci = set([1, 1, 2, 3, 5, 8])
primes = set([2, 3, 5, 7, 11])
both = fibonacci.intersection(primes)
print(both)




































