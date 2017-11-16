###PART 1
##
#### Sorts a list using SELECTION SORT
### @param values: the list to sort
###
##def selectionSort(values):
##    for i in range(len(values)):
##        print('values1:',values)
##        print('i:',i)
##        
##        minPos = minimumPosition(values,i)
##        
##        print('minPos:',minPos)
##        
##        temp = values[minPos]
##
##        print('temp:',temp)
##        
##        values[minPos] = values[i]
##
##        print('values2:',values)
##        
##        values[i] = temp
##
##        print('values3:',values)
##        print()
##        print()
##
#### Finds the smallest element in a tail range of the list
### @param value: the list to sort
### @param start: the first position in values to compare
### @return values[start]...values[len(values)-1]
###
##def minimumPosition(values,start):
##    minPos = start
##
##    for i in range(start + 1, len(values)):
##        if values[i] < values[minPos]:
##            minPos = i
##    return minPos
##
##
##def main():
##    values = [4,   7 ,  11   ,4   ,9   ,5   ,11   ,7   ,3   ,5]
##
##    selectionSort(values)
##    print(values)
##    
##main()





###PART 2
### The mergeSort function sorts a list, using the merge sort algorithm
###
##
#### Sorts a list, using merge sort.
### @param values: the list to sort
###
##def mergeSort(values):
##    if len(values) <= 1: return 
##
##    mid = len(values) // 2
##    
##    print('Mid:',mid)
##    
##    first = values[ :mid]
##    
##    print('First:',first)
##    
##    second = values[mid: ]
##    
##    print('Second:',second)
##    
##    mergeSort(first)
##    mergeSort(second)
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
##        if first[iFirst] < second[iSecond]:
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
##    print('END merged:',values)
##    print()
##    print()
##
##
##def main():
##    values = [5,   11   ,7   ,3   ,5   ,4   ,7   ,11   ,4   ,9]
##
##    mergeSort(values)
##    print(values)
##    
##main()





#PART 3

## Sorts a list using SELECTION SORT
# @param values: the list to sort
#
def selectionSort(values):
    #Progressively going through the list, 1 element at a time
    for i in range(len(values)):
        
        #Call maximumPosition and save the value into minPos
        #This will return the index position of the largest element
        maxPos = maximumPosition(values,i)

        #Save the value of the element at the maximum position
        temp = values[maxPos]

        #Write the element value at index i into the index which is occupied
        #by the maximum value
        values[maxPos] = values[i]

        #Write the maximum value into index i
        values[i] = temp

## Finds the largest element in a list
# @param value: the list to sort
# @param start: the first position in values to compare
# @return maxPos: the index of the largest element value
#
def maximumPosition(values,start):
    maxPos = start

    #Find the largest element value in the list
    for i in range(start + 1, len(values)):
        if values[i] > values[maxPos]:
            maxPos = i
            
    #Return the largest values index
    return maxPos


def main():
    values = [4,   7 ,  11   ,4   ,9   ,5   ,11   ,7   ,3   ,5]

    selectionSort(values)
    print(values)
    
main()




























