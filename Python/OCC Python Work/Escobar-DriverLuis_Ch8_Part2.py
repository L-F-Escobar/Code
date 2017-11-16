###Ch08 Section 2 Part 1
##
###Dictionary   {key : value}
##gradeCounts = {'A': 8, 'D': 3, 'B': 15, 'F': 2, 'C': 6}
##
###Prints all the KEYS in dict. gradeCounts
##print('Printing Keys')
##for key in gradeCounts:
##    print(key)
##
###Prints all the VAULES in dict. gradeCounts
##print()
##print('Printing Values')
##for key in gradeCounts:
##    print(gradeCounts[key])
##
###Prints all the KEYS & VAULES in dict. gradeCounts
##print()
##print('Printing Keys & Values')
##for key in gradeCounts:
##    print(key, ' : ',gradeCounts[key])
##
##
##
##
###Ch08 Section 2 Part 2
##
##num = int(input("Please enter a positive integer < 1,000,000,000: "))
##
###Five dictionaries containing all the values that will be needed to convert
###any number less than 1,000,000,000 into their word counter part
###          {KEY : VALUE}
##first    = {1 : 'one', 2 : 'two', 3:'three', 4:'four', 5:'five', 6:'six',
##            7:'seven', 8:'eight', 9:'nine', 10:'ten', 0:'' , 11:'eleven',
##            12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
##            16:'sixteen', 17:'seventeen', 18:'eighteen',19:'nineteen'}
##
##tens     = {20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty',
##            70:'seventy', 80:'eighty', 90:'ninty', 00:''}
##
##hundred  = {1 : 'hundred', 0:''}
##
##thousand = {1 : 'thousand', 0:''}
##
##million  = {1 :'million', 0:''}
##
###Saving a string of the number
##numStr = str(num)
###Getting the length of the string
##count = len(numStr)
##
###Empty string for the word & creating a string/int lists
##word = ""
##numStrList = []
##numList    = []
##
#########################################################
###
### This series of if elif statements use 5 dictionaries 
### to convert a series of numbers into their english    
### translation. There is a visual diagram on the top
### of each statement block to better help understand
### the code. 
###
#########################################################
##
###IF the number is less then 20 go in here
##if num < 20 :
##    #Get the value from the first dictionary
##    word = word + (first[num])
##    
###ELIF the number is less then 100 go in here
##elif num < 100: #36        
##    
##    #Saves the first/second elements in numStr 
##    vassal = numStr[0]
##    vassal1 = numStr[1]    
##    #Mult by ten to make a key for the dictionary
##    num = int(vassal) * 10
##    num1 = int(vassal1)
##    #Retrieve values from the dict. tens/first with the specific keys
##    word = word + tens[num] + ' ' + first[num1]
##
###ELIF the number is less then 1000
##elif num < 1000: #418
##    
##    #Grabs the 1st/2nd/3rd elements from the numberString
##    vassal = numStr[0]  #4
##    vassal1 = numStr[1] #1
##    vassal2 = numStr[2] #8
##        
##    #Convert to ints
##    num = int(vassal)       #4
##    num1 = int(vassal1)     #1
##    num2 = int(vassal2)     #8
##
##    #Grab from dictinary first & hundred
##    word = word + first[num] + ' ' + hundred[1]
##    
##    #If the last 2 element together can be found in first go in here
##    #Must '+' two strings rather then 2 ints
##    if (int(vassal1 + vassal2)) in first:
##        #print('found' , vassal1 + vassal2)
##        word = word + ' ' + first[int(vassal1 + vassal2)]
##    #Else go in here
##    else:
##        #Grab values from dict. tens & first
##        word = word + ' ' + tens[num1 * 10] + ' ' + first[num2]
##
###ELIF the number is less then 1,000,000 go in here
##elif num < 1000000:#345,890 // three hundred fourty five thousand
##                   #           eight hundred ninty
##                   
##    for x in range (0,count):
##        #Dynamically saving the number into seperate elements plus
##        #x serves as a selector for the following IF-ELSE IF loops
##        numStrList.append(numStr[x])  #Saving each element as a string 
##        numList.append(int(numStr[x]))#Saving each element as an int
##
##    
##    #[0],[1] [2] [3]
##    #1,   2   3   4
##    if x == 3:
##        
##        word = word + first[numList[0]] + ' ' + thousand[1] + ' '
##        #    |
##        #IF 9012
##        if numList[1] != 0:
##            word = word + first[numList[1]] + ' ' + hundred[1]
##        #     ||        ||
##        #IF 1212 ELSE 1221
##        if (int(numStrList[2] + numStrList[2])) in first:
##            word = word + ' ' + first[int(numStrList[2] + numStrList[3])]    
##        else:
##            word = word + ' ' + tens[int(numStrList[2]) * 10] + ' ' 
##            word = word + first[int(numStrList[3])]
##        
##    #[0] [1],[2] [3] [4]
##    #1   2,   3   4   5
##    #6   7,   6   1   2
##    elif x == 4:
##        
##        #If the first 2 elements are in dict. first go in here 
##        if (int(numStrList[0] + numStrList[1])) in first:
##            word = word + first[int(numStrList[0] + numStrList[1])] + ' '
##            word = word + thousand[1] + ' '
##            #If the 2nd element is != 0 go in here
##            if numList[2] != 0:
##                word = word + first[numList[2]] + ' '
##                word = word + hundred[1] + ' '
##            #If element 3+4 are in dict. first go in here
##            if (int(numStrList[3] + numStrList[4])) in first:
##                word = word + first[int(numStrList[3] + numStrList[4])]
##            #Else go in here
##            else:
##                word = word + tens[numList[3]*10] + ' ' + first[numList[4]]
##                
##        #Else go in here
##        else:                                       
##            word = word + tens[numList[0] * 10] + ' ' + first[numList[1]] + ' '
##            word = word + thousand[1] + ' '
##            
##            #If the 2nd element is != 0 go in here
##            if numList[2] != 0:
##                word = word + first[numList[2]] + ' '
##                word = word + hundred[1] + ' '
##
##            #If element 3+4 are in dict. first go in here
##            if (int(numStrList[3] + numStrList[4])) in first:
##                word = word + first[int(numStrList[3] + numStrList[4])]
##            #Else go in here
##            else:
##                word = word + tens[numList[3]*10] + ' ' + first[numList[4]]
##
##        
##    #[0] [1] [2], [3] [4] [5]
##    #1    2   3,   4   5   6
##    elif x == 5:
##        #Grabbing the hundred thousand position
##        word = word + first[numList[0]] + ' ' + hundred[1] + ' '
##        
##        #Checking the dictioaries for matches
##        if (int(numStrList[1] + numStrList[2])) in first:
##            word = word + first[int(numStrList[1] + numStrList[2])] + ' '
##            word = word + thousand[1] + ' '
##        else:
##            word = word + tens[int(numStrList[1]) * 10] + ' '
##            word = word + first[int(numStrList[2])] + ' ' + thousand[1] + ' '
##            
##        #Grabbing the hundreds place
##        word = word + first[int(numStrList[3])] + ' ' + hundred[1] + ' '
##        
##        #Checking the proper dictionaries for matches
##        if (int(numStrList[4] + numStrList[5])) in first:
##            word = word + first[int(numStrList[4] + numStrList[5])] + ' '
##        else:
##            word = word + tens[int(numStrList[4]) * 10] + ' '
##            word = word + first[int(numStrList[5])]
##            
##elif num < 1000000000:#345,890,909
##    
##    for x in range (0,count):
##        #Dynamically saving the number into seperate elements plus
##        #x serves as a selector for the following IF-ELSE IF loops
##        numStrList.append(numStr[x])  #Saving each element as a string 
##        numList.append(int(numStr[x]))#Saving each element as an int
##
##    #Using this visual representation it is easy to read the code
##    #[0],[1] [2] [3],[4] [5] [6]
##    # 3,  4   5   8,  9   0   9
##    if x == 6:
##
##        word = word + first[numList[0]] + ' ' + million[1] + ' '                  
##
##        #IF [1] != 0 go in here
##        if numList[1] != 0:
##            word = word + first[numList[1]] + ' ' + hundred[1]
##
##        #IF ([2]+[3]) key is in the first dictionary go in here
##        if (int(numStrList[2] + numStrList[3])) in first:
##            word = word + ' ' + first[int(numStrList[2] + numStrList[3])]
##            word = word + ' ' + thousand[1]
##        #Else they must be in the tens & ones dictionary
##        else:
##            word = word + ' ' + tens[int(numStrList[2]) * 10] + ' ' 
##            word = word + first[int(numStrList[3])] + ' ' + thousand[1] + ' '
##
##        if numList[4] != 0:
##            word = word + first[int(numStrList[4])] + ' ' + hundred[1]
##            
##        #IF ([5]+[6]) key is in the first dictionary go in here
##        if (int(numStrList[5] + numStrList[6])) in first:
##            word = word + ' ' + first[int(numStrList[5] + numStrList[6])]
##        else:
##            word = word + ' ' + tens[int(numStrList[5]) * 10] + ' ' 
##            word = word + first[int(numStrList[6])]
##        
##    #[0] [1],[2] [3] [4],[5] [6] [7]
##    # 3   4,  5   8   9,  0   9   0
##    elif x == 7:
##        
##        #IF ([0]+[1]) key is in the first dictionary go in here
##        if (int(numStrList[0] + numStrList[1])) in first:
##            word = word + first[int(numStrList[0] + numStrList[1])]
##            word = word + ' ' + million[1] + ' '
##        else:#Else grab it in parts from other dictionaries
##            word = word + tens[numList[0] * 10] + ' ' + first[numList[1]] + ' '
##            word = word + million[1] + ' '
##
##        #So long as [2] is not zero go in here
##        if (int(numStrList[2])) != 0:
##            word= word + first[int(numStrList[2])] + ' ' + hundred[1] + ' '
##
##        #If key [3]+[4] exist in the first dictionary go in here
##        if (int(numStrList[3] + numStrList[4])) in first:
##           word = word + first[int(numStrList[3] + numStrList[4])] + ' '
##           word = word + thousand[1] + ' '
##        else:#Else grab the values seperately 
##            word = word + tens[int(numStrList[3]) * 10] + ' ' 
##            word = word + first[int(numStrList[4])] + ' ' + thousand[1] + ' '
##            
##        #So long as [5] is not equal to zero go in here
##        if (int(numStrList[5])) != 0:
##            word= word + first[int(numStrList[5])] + ' ' + hundred[1] + ' '
##
##        #If key [6]+[7] exist in the first dictionary go in here
##        if (int(numStrList[6] + numStrList[7])) in first:
##           word = word+ first[int(numStrList[6] + numStrList[7])] + ' '
##        else:
##            word = word + tens[int(numStrList[6]) * 10] + ' ' 
##            word = word + first[int(numStrList[7])] + ' '             
##
##        
##    #[0] [1] [2],[3] [4] [5],[6] [7] [8]
##    # 3   4   5,  8   9   0,  9   0   9
##    elif x == 8:
##
##        word = word + first[numList[0]] + ' ' + hundred[1] + ' '
##        
##        #If key [1]+[2] exist in the first dictionary go in here                    
##        if (int(numStrList[1] + numStrList[2])) in first:
##            word = word + first[int(numStrList[1] + numStrList[2])]
##            word = word + ' ' + million[1] + ' '
##        else:
##            word = word + tens[numList[1] * 10] + ' ' + first[numList[2]] + ' '
##            word = word + million[1] + ' '
##
##        #So long as [3] is not equal to zero go in here
##        if (int(numStrList[3])) != 0:
##            word= word + first[int(numStrList[3])] + ' ' + hundred[1] + ' '
##
##        #If key [4]+[5] exist in the first dictionary go in here
##        if (int(numStrList[4] + numStrList[5])) in first:
##           word = word + first[int(numStrList[4] + numStrList[5])] + ' '
##           word = word + thousand[1] + ' '
##        else:
##            word = word + tens[int(numStrList[4]) * 10] 
##            word = word + first[int(numStrList[5])] + ' ' + thousand[1] + ' '
##
##        #So long as [6] is not equal to zero go in here
##        if (int(numStrList[6])) != 0:
##            word= word + first[int(numStrList[6])] + ' ' + hundred[1] + ' '
##
##        #If key [7]+[8] exist in the first dictionary go in here
##        if (int(numStrList[7] + numStrList[8])) in first:
##           word = word + first[int(numStrList[7] + numStrList[8])] + ' '
##        else:
##            word = word + tens[int(numStrList[7]) * 10] + ' ' 
##            word = word + first[int(numStrList[8])] + ' ' 
##
##
##print('The translation is:',word)
##
##
##
##    
#Ch08 Part 2 Section 3

###Create an empty dictionary
##fileDict = {}
##revFileDict = {}
##
###Opening a file to read
##inFile  = open("input.txt","r")
###Read a line of that file, Set the LCV
##line = inFile.readline()
##
###Check the LCV
##while line != '':
##    #Split that line by :
##    a,b = line.split(':')
##    #Stripping from the left & right 
##    a = a.strip()
##    b = b.strip()
##    #Add   [key]=value
##    fileDict[a] = b
##    #Change the LCV, read another line 
##    line = inFile.readline()
##
###Flipping the dictionary around into a reverse dict., thus
###mapping each value to all of the keys it maps to
##for key, value in fileDict.items():
##     revFileDict.setdefault(value, set()).add(key)
##
###Now, you're just looking for the keys in the
###reverse dict. that have more than 1 value to their key
##for key in revFileDict:
##    if len(revFileDict[key]) > 1:
##        print('The word  "',key, '"  appears ', end='')
##        print(' times.',len(revFileDict[key]))
##
##print()
##print('The original dictionary values')
##print('-'*27)
##for key in fileDict:
##    print(fileDict[key])





#Ch08 Part 2 Section 4

#CountDup(fileName)
# @param  : main passes a string variable, the input file into this
#           function.
# @return : returns a dictionary of duplicate words from the open
#           file.
#
def CountDup(fileName):
    #Create an empty dictionary
    fileDict = {}
    revFileDict = {}
    duplicates = {}

    #Opening a file to read
    inFile  = open(fileName,'r')
    #Read a line of that file, Set the LCV
    line = inFile.readline()

    #Check the LCV
    while line != '':
        #Split that line by :
        a,b = line.split(':')
        #Stripping from the left & right 
        a = a.strip()
        b = b.strip()
        #Add   [key]=value
        fileDict[a] = b
        #Change the LCV, read another line 
        line = inFile.readline()

    #Flipping the dictionary around into a reverse dict., thus
    #mapping each value to all of the keys it maps to
    for key, value in fileDict.items():
         revFileDict.setdefault(value, set()).add(key)

    #Now, you're just looking for the keys in the
    #reverse dict. that have more than 1 value to their key
    for key in revFileDict:
        if len(revFileDict[key]) > 1:
            #Creating a dict of words that were dup or more
            duplicates[key] = len(revFileDict[key])
            
    inFile.close()
    #Return the dictionary of duplicate words
    return duplicates
    
#main()
# @param  : <none>
# @return : return a dictionary of input files as keys and
#           duplicate words in those files as the key values.
#
def main():
    #Empty dictionary and counter
    fileDict = {}
    count = 0
    
    #Get LCV
    name = input('Enter the file name(x to exit): ')

    #While the user does not wish to terminate the program
    while name != 'x' and name != 'X':

        #If the file has not already been read enter
        if name not in fileDict:
            #Pass the file name into the func. and save the
            #duplicate words as a value, with the file name as
            #the key
            fileDict[name] = CountDup(name) 
            count = 0
        #Else increment the counter
        else:
            print('That file as already been entered!')
            count = count + 1

        #If the user has entered the same file name twice
        if count == 2:
            count = 0
            print()
            print('You have entered the same file name more ', end='')
            print('then once!')
            print('The duplicates from file name', name,'are: ')
            print(fileDict[name])
            print()
        #Change LCV
        name = input('Enter the file name(x to exit): ')

        
    print('Total entries')
    print('-'*25)
    for key in fileDict:
        print(key,fileDict[key])
        
#Call main
main()





























