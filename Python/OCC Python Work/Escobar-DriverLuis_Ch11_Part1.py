#### Recurive function that finds the smallest element in a list
### @param data - a list of integers
### @return     - the smallest element in an integer list
###
##def smallest(data) :
##
##   if len(data) == 1 :
##      #Prints - When data == 1: 10
##      #This is the very first thing returned by the recursion
##      #Will print last 
##      print('When data == 1:',data[0])
##      return data[0]
##
##   #After the first return this print statement is executed 8 times.
##   #In python shell the first print display is actually the last recursion call
##   #This print statements last print statement is actually the second recursion call 
##   print('These are the calls','data[0]',data[0],'data[-1]',data[-1])
##
##   #Everything above this recursive call is printed 9 times, then the returns
##   #underneath are executed.
##   #          [start at element 0 : ending with one less then the stated]
##   smallestRest = smallest(data[0 : -1])#Recursive call
##
##   #Now the print statements are executed in order instead of in reverse as
##   #above the recursion call.
##   print()
##   print('Under recursive call:',smallestRest)
##
##   #Chceks if the smallest number saved is less than the next element in the list
##   if smallestRest > data[-1] :
##      print('In IF:',data[-1])
##      return data[-1]
##   #If not return the smallest number
##   else :
##      print('TESTING data[-1]',data[-1])
##      print('In ELSE:',smallestRest)
##      return smallestRest
##
##
##def main() :
##   # Demonstrate the smallest function.
##   #              [0],...                     ...,[8]
##   print(smallest([10, 12, 33,  8, 52, 49, 23, 14, 1]))
##   #             [-9],...                     ...,[-1]
##   print("Expected: 1")
##
### Call the main function.
##main()



##Recursive function that reverses a string by removing its last element & adding the string
# @param text: a string passed from main
# @return    : a reversed string
#
def reverse(text):
   #If the string is empty, simply return the empty string
    if text == "":
       return text
    else:
       #As is shown in Python Shell, this removes the last element in the string
       #and adds it to the rest of the string, then returns it. This executes till
       #there is no more text left to remove.
       print('text[-1]:',text[-1],'   text[:-1]:%-8s' %text[:-1], 'text:',text)

       #Concantinate the last element in the string with the string minus the last element
       return text[-1] + reverse(text[:-1])

def main() :
   # Demonstrate the reverse function. The last element is [-1]
   #          ([0],..,[5])
   r = reverse("Hello!")
   #         ([-6],.,[-1])
   print()
   print('Input:','Hello!')
   print('Results:',r)
   print("Expected: !olleH")

# Call the main function.
main()







