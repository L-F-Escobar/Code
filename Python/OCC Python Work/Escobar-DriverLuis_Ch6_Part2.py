#PART ONE

## equals
# @param a,b : int lists are being passed into the function
# @return : whether the lists are the same or not
#
def equals(a,b):
    #If list a is the same as list b
    if a == b:
        print('In same order')
    else:
        print('Not in the same order')

## main
# @param : <none>
# @return: <none>
def main():
    #Setting up 2 int lists
    listOne = [1,2,3]
    listTwo = [1,3,3]
    #Calling the func. equals with the 2 int lists
    equals(listOne,listTwo)
#calling main
main()


##PART TWO
## AddToList
# @param <none>
# @return <none>
#
def AddToList():
    #Setting a counter
    count = 0
    #creating an empty list
    intList = []

    value = int(input('Enter any value, -999 to exit: '))
    
    while (count < 10) and (value != -999) :

        #If value has already been entered simply pick a new #
        if value in intList:
            print('\nValue is already present in the list!')
            print('Pick a new number')
        #Else add and increment the counter
        else:
            intList.append(value)
            count = count + 1
        #If the counter is 10 there is no need to asked for input
        if count == 10:
            continue
        else:
            value = int(input('Enter any value, -999 to exit: '))

    for i in range(len(intList)):
        print(i,intList[i])

def main():
    #Function call
    AddToList()
main()


##PART THREE

##ReverseList
# @param a : a list of ints is being passed
# @return : a print statement with the reversed llist
#
def ReverseList(a):
    a.reverse()
    print('Reverse:  ', a)

## main
# @param <none>
# @return <none
#
def main():
    #List of ints
    intList = [1,4,16,9,7,4,9,11]
    print('Original: ', intList)
    ReverseList(intList)  
main()


## PART 4 ##

## alternating
# @param a: a list of ints from main
# @return : a printing of the total value of the alternating
#
def alternating(a):
    total = 0
    #For loop for the size of a  
    for i in range(len(a)):
        #If even add
        if (i%2) == 0:
            total = total + a[i]
        #If odd, subtract
        else:#(i%2)== 1:
            total = total - a[i]
    print('The alternating total is: ',total)

## main
# @parma <none>
# return <none>
#
def main():
    #A list of ints
    intList = [1,4,16,9,7,4,9,11]
    #Func. call 
    alternating(intList)
#Calling main
main()












### PART FOUR
