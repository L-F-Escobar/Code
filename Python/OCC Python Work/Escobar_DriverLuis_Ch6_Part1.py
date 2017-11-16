#Part 1
purge = [1,3,56,23,-12,-124,14,-12,-666,900,-3244]

count = 0
for i in range(len(purge)):
    
    if (purge[i- count]) < 0:
        purge.pop(i - count)
        count = count + 1    
    else:
        continue


for i in range(len(purge)):
    print(purge[i])
print(len(purge))


###### Part 2 #####
values = []

#Read input from user
print('Please enter values, Q to quit: ')
userInput = input('')
while userInput.upper() != 'Q':
    values.append(float(userInput))
    userInput = input('Enter: ')

#Finds the largest & smallest values
largest = values[0]
smallest = values[0]
for i in range(1,len(values)):

    #Two seperate if statments because are conditions are
    #specific/narrow
    if values[i] > largest:
        largest = values[i]      
    if values[i] < smallest:
        smallest = values[i]

#Prints all values, marking the smallest & largest
for element in values:
    print(element, end="")
    #Lookings for our narrow conditions
    if element == largest:
        print(' <== largest value', end="")
    if element == smallest:
        print(' <== smallest value', end="")
    print()



### PART 3 ###
ONE_TEN = [1,2,3,4,5,6,7,8,9,10]

## main()
# @ param <none>
# @  return <none>
#
def main():
    prompt0 = 'The original data for all functions is : '
    prompt1 = 'After swapping first & last: '
    prompt2 = 'After replacing all even elements with zeros: '
    prompt3 = 'The second largest is: '
    prompt4 = 'Is the list in increasing order?: '
    yes = True
    
    #Printing the original list
    print()
    print('%-46s'%(prompt0), ONE_TEN)

    #Saving easy vairables to use.
    data = list(ONE_TEN)
    zeros = list(ONE_TEN)
    
    #Calling a func. to perform swap
    swapFirstLast(data)  
    print('%-46s'%(prompt1) , data)
    #Calling a func. to replace all even elements with 0's
    replaceAllEvenZero(zeros)
    print('%-46s'%(prompt2) , zeros)
    #Calling a func. to return the 2nd larest number in the list
    secLargest = secondLargest(zeros)
    print('%-46s'%(prompt3) , secLargest)  
    #Calling to see if the list is in increasing order
    yes = trueOrNot(zeros)
    print('%-46s'%(prompt4) , yes)

   
## swapFirstLast
# @param data: this is a list of ints. A copy of the origial
# @return <none>
#
def swapFirstLast(data):
    #Gets the length of elements
    lengthOf = len(data)
    #Saving a temp
    temp = data[0]
    data[0] = data[lengthOf - 1]
    data[lengthOf - 1] = temp

## replaceAllEvenZero
# @param zeros: a list of ints from main
# @return <none>
#
def replaceAllEvenZero(zeros):
    for i in range(len(zeros)):
        #Use mod to determine even or odd 1%2=1
        if (i%2 == 0):
            zeros[i] = 0

## secondLargest
# @param data: a list of ints from main
# @return secLargest: returns the second largest value in the list
#
def secondLargest(zeros):
    test = list(zeros)
    test.sort()
    #Gives the actaul length of the list
    lengthOf = len(test)
    #Simply subtract 2 from the actual length, once to account for
    #the 0 position & the other for the highest element
    secLargest = test[lengthOf - 2]

    return secLargest

## trueOrNot
# @param data: a list of ints from main
# @return: a bool value which tells the code if its sorted
#
def trueOrNot(data):
    #Save an exact copy
    test = list(data)
    #sort it
    test.sort()
    #Now test the two
    if test == data:
        yes = True
    else:
        yes = False
    #return the bool
    return yes

            
        
#Calling main
main()
















    
