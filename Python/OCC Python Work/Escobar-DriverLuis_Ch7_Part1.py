###Luis Fernando Escobar-Driver
###Chapter 7 Part 1 HW
##
#####PART 1 - Code carrying out specific tasks
##
###Opens an outfile. In this case it is created since it did not
###previously exist
##outFile = open("hello.txt","w")
###Save a string
##line = "Hello, World!"
###Storing that string into the outFile
##outFile.write(line)
###Close it
##outFile.close()
###Open the outfile with the purpose of READING from it, hence
###the r
##outFile = open("hello.txt","r")
###Save the message 
##msg = outFile.readline()
###Print the message
##print(msg)


#####PART 2 - Write an inFile into an outFile
###Opening an input & output file
##inFile  = open("input.txt","r")
##outFile = open('outFile.txt','w')
##
###Read the first line from the input file
##line = inFile.readline()
##count = 0
##
###While the line is not empty enter the while loop
##while line != "":
##    #Print into the output file
##    outFile.write("/* ")
##    outFile.write((str(count + 1)))
##    outFile.write(" */ ")
##    outFile.write(line)
##    #Read a new line from the input file
##    line  = inFile.readline()
##    #Inc counter
##    count = count + 1
##
###Closing the input & output files
##inFile.close()
##outFile.close()


###PART 3 - Prompt user for inFile, floating Pt data

#Asking user for input file name, then opening the file
inputFileName = input("Enter the file name to be opened: ")
inFile = open(inputFileName,"r")
outFile = open("Part3.txt","w")

#Used to sum the two columns
colOneSum = 0.0
colOneAvg = 0.0
colTwoSum = 0.0
colTwoAvg = 0.0
#Used as a divisor to get the average
count = 0
#Used to correctly sum the two columns
forCount = 0

#Grabs a line of data 
line = inFile.readline()

#wordList will split the line into its seperate components
#according to where black spaces are
wordList = line.split()

#While the file is not empty
while line != "":
    
    #This allows each seperate data piece split into wordList to be
    #handled individually
    for word in wordList:
        #The column numbers will fall into the proper summing
        #variables
        if forCount == 0:
            #Converting the string into a float
            colOneSum = colOneSum + float(word)
        else: #forCount == 1 for the second column number
            #Converting the string into a float
            colTwoSum = colTwoSum + float(word)

        forCount = forCount + 1

    #Grabs the next line from the input file
    line = inFile.readline()
    #Splits that line along empty spaces
    wordList = line.split()
    #Inc count to be used as a divisor 
    count = count + 1
    #Resetting the forCounter for the next iteration
    forCount = 0


colOneAvg = colOneSum / count
colTwoAvg = colTwoSum / count
print('The average of column one is: ',colOneAvg)
print('The average of column two is: ',colTwoAvg)

#Closing the input & output files
inFile.close()
outFile.close()




###PART 4 - Store Owner

#Used to sort the data properly
forCount = 0
#Accumulates the total amount of money that should be present
balance = 0.0
#Used to temporarily hold the dollar amount of the return/paid
tempValue = 0.0

#Asking user for the beginning & ending cash amounts.
cashBegin = float(input("Enter beginning cash: "))
cashEnd = float(input("Enter ending cash: "))

#Prompting & opening an infile 
inputFileName = input("Enter file name: ")
inFile = open(inputFileName,'r')

#Saving an entire line of the infile into variable line
line = inFile.readline()
#Breaking up variable line by white spaces
wordList = line.split()

#While line is not empty
while line != "":
    #Grabbing each indivdual word
    for word in wordList:

        #Save the invoice number
        if forCount == 0:
            invoice = word
            
        #Save the total amount
        elif forCount == 1:
            tempValue = float(word)
            
        #Determine if it has been paid or returned     
        else:#count == 2 :: Means that its PAID or RETURNED
            
            #If returned subtract from the balance
            if word == 'R':
                balance = balance - tempValue
                tempValue = 0.0
                
            #If paid add to the balance 
            else:#word == 'P'
                balance = balance + tempValue
                tempValue = 0.0

        #Used to sort out the data properly. 
        forCount = forCount + 1

    #Read in a new line
    line = inFile.readline()
    #Serperate the line by spaces
    wordList = line.split()
    #Reset the forCount
    forCount = 0

if cashEnd != balance:
    print('The closing balance didnt match!')
    print('Your end balance is: ', "%.2f" %cashEnd)
    print('According to the file, it should be: ', "%.2f" %balance)
else:
    print('The closing balance is correct!')
            
        
    




































