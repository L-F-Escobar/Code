#Luis Fernando Escobar-Driver

#import sys



###PART 1 - command prompt
import sys

inFile = ""


#inFile  = open(sys.argv[1],"r")
outFile = open('outFile.txt','w')

if len(sys.argv) < 2:
    textName = input('Enter file name: ')
    file = open(textName,'r')
else:
    file = open(sys.argv[1])
    

#Read the first line from the input file
line = file.readline()
count = 0

#While the line is not empty enter the while loop
while line != "":
    #Print into the output file
    outFile.write(line)
    #Read a new line from the input file
    line  = file.readline()
    #Inc counter
    count = count + 1

#Closing the input & output files
file.close()
outFile.close(



###Ch07 Part 2
###How many valid entries were made
##validCounter = 0
###LCV for while loop
##counter = 0
###Total summation of valid inputs
##totalSum = 0.0
##fail = False
##
##while counter < 2:
##    #Functions as a sort of Do-While loop
##    try:
##        if counter == 0:
##            fNum = float(input("Enter a floating point value: "))
##        else:
##            fNum = float(input("Once more, enter a floating point value: "))
##
##    #Works as a sort of do-while loop when they input a value which isnt a float
##    except ValueError as exception:
##        fail = True
##        print("Error:",str(exception))
##
##    #Correction engine
##    if fail == False: #Valid input, reset counter to 0
##        totalSum = fNum + totalSum
##        validCounter = validCounter + 1
##        counter = 0
##        
##    else:#Invalid input
##        counter = counter + 1
##        fail = False
##
##print('This is the totalSum: %.2f ' %totalSum)





###Ch07 Part 3
##
#### main()
### @param  : <none> 
### @return : 2 text files seperated by gender
###
##def main():
##    count = 0
##    
##    #inFile will hold the babynames
##    inFile = open("babynames.txt","r")
##    oFileBoy = open("boynames.txt","w")
##    oFileGirl = open("girlnames.txt","w")
##
##    #Grabbing an entire line
##    line = inFile.readline()
##
##    #wordList will split the line into its seperate components
##    #according to where black spaces are
##    wordList = line.split()
##
##    #While the file is not empty
##    while line != "":
##
##        for word in wordList:
##
##            #First word, Second word, etc
##            #Writting simaltaneously into their own files
##            if count == 0:
##                rank = word
##                oFileBoy.write(rank)
##                
##            elif count == 1:
##                boyName = word
##                oFileBoy.write("%15s" %boyName)
##                
##            elif count == 2:
##                boyCount = word
##                oFileBoy.write("%10s" %boyCount)
##                oFileBoy.write('\n')
##                
##            elif count == 3:
##                girlName = word
##                oFileGirl.write(rank)
##                oFileGirl.write("%15s" %girlName)
##                
##            else:
##                girlCount = word
##                oFileGirl.write("%10s" %girlCount)
##                oFileGirl.write('\n')
##                
##            count = count + 1
##
##        #Reset the count for the next line
##        count = 0
##        #Read in next line
##        line = inFile.readline()
##        #Seperate the words by blank spaces
##        wordList = line.split()
##
##
##    #Close all the files
##    inFile.close()
##    oFileBoy.close()
##    oFileGirl.close()
##
###Call main
##main()





#Ch07 Part 4

#LCV for errrors   
valid = True
#LCV for main while loop
count = 0
#LCV for shifting through words in a wordList
wordCount = 0
#Sums
dinnerSum = 0.0
lodgingSum = 0.0


while count < 4:

    try :
        if count == 0:           
            filename = input("Enter filename: ")
            infile = open(filename, "r")
            #Reading in a line
            line = infile.readline()
            #Splitting the line by ;
            wordList = line.split(';')
        else:
            line = infile.readline()
            wordList = line.split(';')
            
    except IOError :
        print("Error: file not found.")
        valid = False
    except ValueError as exception :
        print("Error:", str(exception))
        valid = False

    #If false, there was an error, Else continue
    if valid == False:
        valid = True
    else:
        #Inc for valid entry
        count = count + 1

        for word in wordList:
            #The [2] item is the price, if it was dinner enter the if
            if wordCount == 2 and "Dinner" in wordList:
                dinnerSum = dinnerSum + float(word)
            elif wordCount == 2 and "Lodging" in wordList:
                lodgingSum = lodgingSum + float(word)
            #Looping the word via the wordCount for the 2nd element, the price
            wordCount = wordCount + 1
        #After exiting the for loop, set wordCount back to 0 
        wordCount = 0
        
print('lodgingSum %.2f' %lodgingSum)
print('fdinnerSum %.2f' %dinnerSum)






        














