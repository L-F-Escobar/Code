####Function that reverses a string by removing its last element & adding the string
### @param text: a string passed from main
### @return    : a reversed string
###
##def reverse(text):
##    empty = ''
##
##    #Grabbing elements from the back of a string & concatenating 
##    #it with an empty string value
##    for i in range((len(text)-1), 0, -1):
##        #Concantinate the string
##        empty = empty + text[i]
##        
##    #Concatenate the last element
##    empty = empty + text[0]
##
##    #Return the string
##    return empty
##
##def main() :
##
##   r = reverse("Hello!")
##   print("Expected: !olleH")
##   print('Result:',r)
##
### Call the main function.
##main()





## Test whether a given text contains a string
# @param text: a text that is passed from main
# @param string: a sting that will be tested against the text
# @return : true or false if the string is in the text
#
def find(text,string):
    #Grab the char starting from element 1 to the last element
    newString = text[1: ]
    #print('ZZNew String AssignmentZZ:',newString)

    #If the newstring is smaller then the string return False
    if (len(newString)) < (len(string)):
        #print('IN FALSE IF:')
        return False 
    else:
        #Accumulate the first 3 element letters into string test
        test = newString[0] + newString [1] + newString[2]
        #print()
        #print('TESTING:',test)

        #Test for a match
        if test == string:
            #print('RETURNING TRUE')
            return True
        else:
            test = ""
            #print('ZUES IS GREAT')
            return find(newString,string)
def main() :
   # Demonstrate the find function.
   print(find("Mississippi", "sip"))
   print("Expected: True")

   print(find("Mississippi", "pip"))
   print("Expected: False")
# Call the main function.
main()


