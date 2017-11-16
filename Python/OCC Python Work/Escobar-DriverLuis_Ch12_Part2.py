###Part 1
#### Sorts a list, using merge sort.
### @param values: the list to sort
###
##def mergeSort(values):
##    if len(values) <= 1: return
##
##    mid = len(values) // 2
##    first = values[ :mid]
##    second = values[mid: ]
##    mergeSort(first)
##    mergeSort(second)
##    
##    mergeList(first,second,values)
##
##    
#### Merge two sorted lists into a third list
### @param first: the first sorted list
### @param second: the second sorted list
### @param values: the list into which to merge first & second
###
##def mergeList(first,second,values):
##    iFirst = 0   #Next element to consider in the first list
##    iSecond = 0  #Next element to consider in the second list 
##    j = 0        #Next open position in values
##
##    #As long as neither iFIrst not iSecond is past the end, move the
##    #smaller element into values
##    while iFirst < len(first) and iSecond < len(second):
##
##        ##WHAT WAS CHANGED IS HERE. INSTEAD OF first[iFirst] < second[iSecond],
##        #switch the boolean expression. Now if the first is greater then the
##        #second, add it FIRST. This will SELECT the larger value EVERY time.
##        #Originally it was selecting the small value and adding it to the front
##        #of the list. 
##        if first[iFirst] > second[iSecond]:
##            values[j] = first[iFirst]
##            iFirst = iFirst + 1
##        else:
##            values[j] = second[iSecond]
##            iSecond = iSecond + 1
##
##        j = j + 1
##
##    #NOTE that only one of the two loops below copies entries.
##        
##    #Copy any remaining entries of the first list
##    while iFirst < len(first):
##        values[j] = first[iFirst]
##        iFirst = iFirst + 1
##        j = j + 1
##
##    #Copy any remaining entries of the second list.
##    while iSecond < len(second):
##        values[j] = second[iSecond]
##        iSecond = iSecond + 1
##        j = j + 1
##
##
####
### This program demonstrates the merge sort algorithm by sorting a list
### of randomly assigned integers 
###
##
##from random import randint
##
##n = 12      #Get 12 integers
##values = [] #Empty list
##
###for(i=0, i<n, i++)
##for i in range(n):
##    values.append(randint(1,20))#Random range 1-20
##    
##print('Before the merge sort:',values)
##mergeSort(values)
##print('After the merge sort:',values)




###Part 2
##
##
###BINARY SEARCH : Locates a value in a sorted list by determining whether
###                the value occures in the first or second half. Then
###                reapting the search in one of the halves
##
#### Finds a value in a range of a sorted list, using the binary search algorithm
### @param values: the list in which to search
### @param low: the low index of the range
### @param high: the high index of range
### @param target: the value to find
### @param select: search for name or number
### @return the index at which the targer occures or 666 if not found
###
##def binarySearch(values,low,high,target,select):
##    if low <= high:
##        mid = (low + high)// 2
##
##        #This will look for names in the list
##        if select == 'L':
##            if values[mid][0] == target:
##                return mid
##            elif values[mid][0] < target:
##                return binarySearch(values, mid + 1, high, target,select)
##            else:
##                return binarySearch(values, low, mid - 1, target,select)
##
##        #This will look for numbers in the list
##        elif select == 'N':
##            if values[mid][1] == target:
##                return mid
##            elif values[mid][1] < target:
##                return binarySearch(values, mid + 1, high, target,select)
##            else:
##                return binarySearch(values, low, mid - 1, target,select)
##    else:
##        return 666
##
##    
#### Allows the user to make a valid choice selection
###
##def GetInfo():
##    select = input('L)ookup Name, Lookup N)umber or Q)uit?:').upper()
##
##    #Functions as a do-while loop to verify proper input
##    while select != 'L' and select != 'N' and select != 'Q':
##        select = input('L)ookup Name, Lookup N)umber or Q)uit?:').upper()
##
##    if select == 'Q':
##        return select, ''
##
##    if select == 'L':
##        target = input('Which name would you like to search for?:')
##    elif select == 'N':
##        target = input('Which number would you like to search for?:')
##
##    return select,target
##
#### Main program
###
##def main():
##    inFile = open('data.txt','r')
##    values = []
##
##    #Sorting the input file data and appending it to a list
##    for line in inFile:
##       line = line.strip()#Stip from right & left
##       a = line.split("|")#Split along the '|' sign
##       values.append(a)   #Dynamic adding to list
##
##    #Must close any opened file
##    inFile.close()
##
##    #Getting the high & low index values of the list
##    high = len(values) - 1
##    low = 0
##
##    #Getting the user choice and user target search
##    #Init the LCV
##    select, target = GetInfo()
##
##    #Checking the LCV
##    while select != 'Q':
##        #Call the binary search function and save its return value
##        isFound = binarySearch(values,low,high,target,select)
##
##        if isFound != 666:
##             print('Found at index position:',isFound, ', INFO: ' , end='')
##             print(values[isFound])
##        else:
##            print('Not Found')
##        print()
##        
##        #Changing the LCV
##        select, target = GetInfo()
##
##main()





#Part 3


#BINARY SEARCH : Locates a value in a sorted list by determining whether
#                the value occures in the first or second half. Then
#                reapting the search in one of the halves

## Finds a value in a range of a sorted list, using the binary search algorithm
# @param values: the list in which to search
# @param low: the low index of the range
# @param high: the high index of range
# @param target: the value to find
# @param select: search for name or number
# @return the index at which the targer occures or 666 if not found
#
def binarySearch(values,low,high,target,select):
    if low <= high:
        mid = (low + high)// 2

        #This will look for names in the list
        if select == 'L':
            if values[mid][0] == target:
                return mid,True
            elif values[mid][0] < target:
                return binarySearch(values, mid + 1, high, target,select)
            else:
                return binarySearch(values, low, mid - 1, target,select)

        #This will look for numbers in the list
        elif select == 'N':
            if values[mid][1] == target:
                return mid,True
            elif values[mid][1] < target:
                return binarySearch(values, mid + 1, high, target,select)
            else:
                return binarySearch(values, low, mid - 1, target,select)
    else:
        #Get the size of the list
        size = len(values)
        k = 0

        #This will give the index element number where the target is smaller
        #then the index element. Indicates that the target needs to be inserted
        #in that index element slot.
        if select == 'L':
            for i in range (size):
                if target > values[i][0]:
                    k = k + 1
        elif select == 'N':
            for i in range (size):
                if target > values[i][1]:
                    k = k + 1

        return k,False

    
## Allows the user to make a valid choice selection
#
def GetInfo():
    select = input('L)ookup Name, Lookup N)umber or Q)uit?:').upper()

    #Functions as a do-while loop to verify proper input
    while select != 'L' and select != 'N' and select != 'Q':
        select = input('L)ookup Name, Lookup N)umber or Q)uit?:').upper()

    if select == 'Q':
        return select, ''

    if select == 'L':
        target = input('Which name would you like to search for?:')
    elif select == 'N':
        target = input('Which number would you like to search for?:')

    return select,target

## Main program
#
def main():
    inFile = open('data.txt','r')
    values = []

    #Sorting the input file data and appending it to a list
    for line in inFile:
       line = line.strip()#Stip from right & left
       a = line.split("|")#Split along the '|' sign
       values.append(a)   #Dynamic adding to list

    #Must close any opened file
    inFile.close()

    #Getting the high & low index values of the list
    high = len(values) - 1
    low = 0

    #Getting the user choice and user target search
    #Init the LCV
    select, target = GetInfo()

    #Checking the LCV
    while select != 'Q':
        #Call the binary search function and save its return value
        index, isFound = binarySearch(values,low,high,target,select)

        if isFound != False:
             print('Found at index position:',index)
        else:
            print('Not Found, insert at index:', index, end='')
            print(' right before',values[index])
        print()
        
        #Changing the LCV
        select, target = GetInfo()

main()
































