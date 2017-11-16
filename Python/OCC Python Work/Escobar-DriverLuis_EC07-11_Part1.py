### PART 1
##
##lineCount = 0
##wordCount = 0
##charCount = 0
##valid = True
##line = 'default'
##
###While the text document is not empty
##while line != '':
##
##    #Try to open a text file
##    try :
##        if lineCount == 0:           
##            fileName = input("Enter filename: ")
##            inFile = open(fileName, "r")
##            #Reading in a line
##            line = inFile.readline()
##            #Splitting the line by ;
##            wordList = line.split()
##        else:
##            line = inFile.readline()
##            wordList = line.split()
##            
##    except IOError :
##        print("Error: file not found.")
##        valid = False
##    except ValueError as exception :
##        print("Error:", str(exception))
##        valid = False
##
##    #If false, there was an error, Else continue
##    if valid == False:
##        valid = True
##    else:
##        #Inc for valid entry
##        lineCount = lineCount + 1 #Gets the total valid lines
##        wordCount = wordCount + len(wordList)#Total valid words
##
##        for word in wordList:
##            charCount = charCount + len(word)#Total valid characters
##            
###The code only needs to dec the line count because the other previous
###incs where adds based on the length of the string. An empty string
###will have a length of zero, therefore the totals were not affected.
##lineCount = lineCount - 1
##print()
##print('Character Count:' ,charCount)
##print('Word Count     :' ,wordCount)
##
##print('Line Count     :' ,lineCount)
##
##        
### PART 2
##
#### A Student, can add, remove, modify or print a dictionary
###
##class student():
##
##    ##Default constructer
##    # @param grade: a grade the user can pass
##    # @param name: a name the user can pass
##    #
##    def __init__(self, grade='' ,name=''):
##        self._grade = grade
##        self._name = name
##        self._HolyBook = {}#HERE IS THE PRIVATE DICTIONARY
##
##    ##Adds a student to the dictionary
##    #
##    def Add(self):
##        self._name = input('Enter the student name: ')
##        self._grade = input('Enter the student grade: ')
##        self._HolyBook[self._name] = self._grade
##
##    #Removes a student from the dictionary
##    #
##    def Remove(self):
##        smiteDown = input('Who would you like to remove: ')
##
##        if smiteDown in self._HolyBook:
##            print('Removing...')
##            self._HolyBook.pop(smiteDown)
##        else:
##            print(smiteDown, 'is not in the dictionary')
##
##    ##Modifys a student in the dictionary
##    def Modify(self):
##        mod = input('Enter student name to modify: ')
##
##        if mod in self._HolyBook:
##            newMod = input('Enter the new grade: ')
##            self._HolyBook[mod] = newMod
##            print('Modifying...')
##        else:
##            print(mod,'not in the dictionary')
##
##    ##Print the entire dictionary in a sorted manner
##    # @return: a printed-sorted dictionary
##    #
##    def Print(self):
##        print('Printing...')
##        for key in sorted(self._HolyBook):
##            print('%-12s %s' %(key, self._HolyBook[key]))
##            
####Allows the user to select a choice fom a list of choices
### @return: the user choice
###
##def GetAction():
##    action = input('A)dd student, R)emove student, M)odify student, P)rint student, E)xit: ')
##    action = action.upper()
##    return action
##
####Main program
###
##def main():
##
##    #Creating a student class
##    package = student()
##    
##    #Call GetAction function to get the user selection
##    #Init LCV
##    action = GetAction()
##
##    #Check LCV
##    while action != 'E':
##        
##        if action == 'A':
##            package.Add()
##            
##        elif action == 'R':
##            package.Remove()
##
##        elif action == 'M':
##            package.Modify()
##            
##        elif action == 'P':
##            package.Print()
##
##        #Change LCV
##        print()
##        action = action = GetAction()
###Calling the main program
##main()
##
##
##
##
###Part 3
##
####Creating a voting machine class
###
##class VotingMachine():
##
##    #Default constructor
##    #
##    def __init__(self):
##        self._countDem = 0
##        self._countGOP = 0
##
##    ##Allows a vote to be cast for a democrat
##    #
##    def voteDemocrat(self):
##        self._countDem = self._countDem + 1
##
##    ##Allows a vote to be cast for a Republican
##    #
##    def voteRepublican(self):
##        self._countGOP = self._countGOP + 1
##
##    ##Allows the code to return the total votes for a Democrat
##    # @return: total democratic vote count
##    #
##    def getTalliesD(self):
##        return self._countDem
##
##    #Allows the code to return the total vote count for a republican
##    # @return: total vote count for a republican
##    #
##    def getTalliesR(self):
##        return self._countGOP
##
###Main Program
###
##def main():
##
##    # Create a new voting machine.
##    vm = VotingMachine()
##
##    # Cast 7 votes.
##    vm.voteDemocrat()
##    vm.voteDemocrat()
##    vm.voteRepublican()
##    vm.voteDemocrat()
##    vm.voteRepublican()
##    vm.voteDemocrat()
##    vm.voteRepublican()
##
##    # Show the vote tallies.
##    print("Democrats:", vm.getTalliesD(), "Republicans:", vm.getTalliesR())
##
##main()




#Part 4


## A question with a text & an answer (only handles strings)(SUPERCLASS)
#
class Question:
    ## Constructs a question with an empty question & answer strings
    #
    def __init__(self):
        self._text = ''
        self._answer = ''
        
    ## Sets the question text.
    # @param questionText the text of this
    #
    def setText(self,questionText):
        self._text = questionText

    ## Sets the answer for this question
    # @param correctReponse the answer
    #
    def setAnswer(self,correctResponse):
        self._answer = correctResponse

    ## Checks a given response for correctness
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    #
    def checkAnswer(self,response):
        return response.upper() == self._answer.upper()

    ## Displays this question
    #
    def display(self):
        print(self._text)

##Allows the code to have multiple correct answers
#
class MultiChoiceQuestion(Question):
    ##Calling the default contructor of class Question
    #
    def __init__(self):
        super().__init__()

    ##Calling the super class set text
    # @param: the text of the question
    #
    def setText(self, questionText):
        super().setText(questionText)

    ##Calling the super class set answer
    # @param: the correct answer to the question
    #
    def setAnswer(self, correctResponse):
        super().setAnswer(correctResponse)

    #Calling the super class check answer
    # @param: the user presonse
    # @return: true or false
    #
    def checkAnswer(self, response):
        return super().checkAnswer(response)

##
#  This program shows a simple quiz with one question.
#

# Create the question and expected answer.
q = MultiChoiceQuestion()
q.setText("Of Apple, Tomato, Carrot, Cucumber and Celery, list all that are fruit.")
q.setAnswer("Apple Tomato")      

# Display the question and obtain user's response.
q.display()
response = input("Your answer(s) seperated by spaces: ")
print(q.checkAnswer(response))



















































