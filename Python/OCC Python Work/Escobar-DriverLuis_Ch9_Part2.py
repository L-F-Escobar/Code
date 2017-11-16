###Ch09 Part 2 Section 1
##
##class Student:
##    
##    ## Default Constructor
##    #
##    def __init__(self, initName ='', initScore = 0):
##        self._name   = initName
##        self._score  = initScore
##        self._count  = 0
##
##    ### SETTERS - MUTATORS ###
##        
##    ## Accumlates quiz scores while incrementing a counter
##    # @param : the score
##    #
##    def AddQuiz(self, score):
##        self._score = self._score + score
##        self._count = self._count + 1
##
##    ### GETTERS - ACCESSORS
##
##    ## Allows the user to get the total score
##    # @return : total score
##    #
##    def GetTotalScore(self):
##        return float(self._score)
##
##    ## Allows the user to get the average score
##    # @return : Average score
##    #
##    def GetAvgScore(self):
##        return float(self._score/self._count)
##    
##    ## Allows the user to get the name
##    # @return : name
##    #
##    def GetName(self):
##        return self._name
##        
##    
### Create a new student.
##s = Student("Bob")
##
### Add some quiz scores.
##s.AddQuiz(50)
##s.AddQuiz(90)
##s.AddQuiz(75)
##
### Show that the total and the average are computed correctly.
##print(s.GetName(), "had a total score of %.2f" % s.GetTotalScore())
##print("The average score was %.1f" % s.GetAvgScore())
##
##
##
##
###Ch09 Part 2 Section 2
##
##class Grade:
##    
##    ## Dictionary containing the value of the grades
##    #
##    gradeDictionary = {'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3,
##                       'C':2.0, 'C-':1.7, 'D+':1.4, 'D':1.0, 'D-':.7,  'F':0}
##    
##    ## Default constructor
##    # @param grade: string of grade value
##    #
##    def __init__(self, grade=''):
##        self._grade = grade.upper()
##    
##    ## Returns the value of the grade
##    # @return: the grade point
##    #
##    def GetGradePoint(self):
##        return Grade.gradeDictionary[self._grade]
##
##
##class Student:
##    
##    ## Default constructor
##    # @param name: the students name
##    #
##    def __init__(self, name=''):c 
##        self._name = name
##        self._totalScore = 0
##        self._count = 0
##
##    ### SETTERS / MUTATORS ###  
##
##    ## Adds the quiz score to the current score
##    # @param score: score of the quiz to be added
##    #
##    def AddQuiz(self, grade):
##        #Using the grade object to call a Grade class method within the Student class
##        self._totalScore = self._totalScore + grade.GetGradePoint()
##        self._count = self._count + 1
##
##    ### GETTERS / ACCESSORS ###
##    
##    ## Returns student's name
##    # @return: string
##    #
##    def GetName(self):
##        return self._name
##    
##    ## Returns the student's total score
##    # @return: the student's total score
##    #
##    def GetTotalScore(self):
##        return self._totalScore
##    
##    ## Returns the total score divided by the number of quizes
##    # @return average score
##    #
##    def GetAvgScore(self):
##        return (self._totalScore / self._count)
##    
##    
###Creating a new student.
##s = Student("Bob")
##
###Calling the student class with a Grade object element
###This object element can now be used to called any method in the Grades class
##s.AddQuiz(Grade("D"))
##s.AddQuiz(Grade("A-"))
##s.AddQuiz(Grade("B"))
##
###Showing that the total and the average are computed correctly.
##print(s.GetName(), "had a total of %.1f grade points." % s.GetTotalScore())
##print("The GPA was %.1f" % s.GetAvgScore())


#Ch09 Part 2 Section 3

class Address:

    ## Default contructor
    #
    def __init__(self,houseNum, streetNum, city, state,
                 postal, apartNum=''):
        self._houseNum  = houseNum
        self._streetNum = streetNum
        self._city      = city
        self._state     = state
        self._postal    = postal
        self._apartNum  = apartNum

    ### GETTERS / ACCESSORS ###
        
    ## Prints the address
    #
    def print(self):
        print(self._houseNum, self._streetNum)
        print(self._city, self._state, self._postal)

    ## Compares which postal code comes first
    # @param : other - an address class to be compared by the called class
    #
    def comeBefore(self, other):
        
        if (int(other._postal) < int(self._postal)):
            print('The address', other._houseNum, other._streetNum, 'comes before ', end="")
            print(self._houseNum, self._streetNum)
        else:
            print('The address', self._houseNum, self._streetNum, 'comes before ', end="")
            print(other._houseNum, other._streetNum)

# Construct two address 
a = Address(2500, "University Drive", "Irvine", "CA", "12345")
b = Address(1200, "College Blvd", "Irvine", "CA", "99102", "12")

#Call the print method
b.print()
print()
a.print()
print()

#Use a class and pass a class to compare each other 
a.comeBefore(b)






























