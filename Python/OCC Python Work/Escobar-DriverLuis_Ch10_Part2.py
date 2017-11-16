#### A question with a text & an answer (only handles strings)(SUPERCLASS)
###
##class Question:
##    ## Constructs a question with an empty question & answer strings
##    #
##    def __init__(self):
##        self._text = ''
##        self._answer = ''
##        
##    ## Sets the question text.
##    # @param questionText the text of this
##    #
##    def setText(self,questionText):
##        self._text = questionText
##
##    ## Sets the answer for this question
##    # @param correctReponse the answer
##    #
##    def setAnswer(self,correctResponse):
##        self._answer = correctResponse
##
##    ## Checks a given response for correctness
##    # @param response the response to check
##    # @return True if the response was correct, False otherwise
##    #
##    def checkAnswer(self,response):
##        return response.upper() == self._answer.upper()
##
##    ## Displays this question
##    #
##    def display(self):
##        print(self._text)
##
#### Allows the code to ask a fill in question from a string with a question & answer
###
##class FillInQuestion(Question):
##    def __init__(self):
##        #Calling the default contructor of class Question
##        super().__init__()
##
##    ## Displays this question - Overriding Question display
##    #
##    def display(self):
##        question = ''
##        answer   = ''
##
##        #Stripping th right _ off the string
##        self._text = self._text.rstrip('_')
##        
##        #Splitting the string by _ 
##        question,answer = self._text.split('_')
##        question = question + '_'*7
##
##        #Now that the answer & question have been isolated & modified,
##        #we can call the superclass methods to properply set the question
##        #and answer. Then call the superclass display.
##        super().setAnswer(answer)
##        super().setText(question)       
##        super().display()
##
### Create the question and expected answer.
##q = FillInQuestion()
##q.setText("The inventor of Python was _Guido van Rossum_")
##
### Display the question and obtain user's response.
##q.display()
##response = input("Your answer: ")
##print(q.checkAnswer(response))




#Part 2 Section 2

## Appointment - SuperClass
#
class Appointment:

    ##Default Constructor
    # @param day, month, year, description : values which define an appointment
    #
    def __init__(self, day, month, year, description):
        self._day = day
        self._month = month
        self._year = year
        self._description = description


## OneTime - SubClass for appointments that are one time
#
class OneTime(Appointment):
    ##Default Constructor
    # @param day, month, year, description : values which define an appointment
    #
    def init (self, day, month, year, disc):
        super().__init__(self, day, month, year, disc)

    ## Saves the appointment to an out file
    # @param file : a file to write into
    #
    def save(self, file):
        writeStr = "O" + "|" + str(self._day) + "|" + str(self._month) + "|"
        writeStr = writeStr + str(self._year) + "|" + self._description + "\n"
        file.write(writeStr)
        
    ## Checks whether the appt. occurs on the passed date
    # @param year, month, day : values which define the day,year & month
    # @return : True if conditions are met
    #
    def occursOn(self,day, month, year):
        if (self._month == month) and (self._day == day) and (self._year == year):
            return True

    ## Displays the contents of the appointment list
    #
    def printappt(self):
        print('An appointment already is scheduled for that time!')
        print('Day:',self._day,'Month:',self._month, end='')
        print(' Year:',self._year,'Description:',self._description)


## Daily - SubClass for appoints that are daily
#
class Daily(Appointment):
    ##Default Constructor
    # @param day, month, year, description : values which define an appointment
    #
    def init (self, day, month, year, disc):
        super().__init__(self, day, month, year, disc)

    ## Saves the appointment to an out file
    # @param file : a file to write into
    #
    def save(self, file):
        writeStr = "D" + "|" + str(self._day) + "|" + str(self._month) + "|"
        writeStr = writeStr + str(self._year) + "|" + self._description + "\n"
        file.write(writeStr)

    ## Checks whether the appt. occurs on the passed date
    # @param year, month, day : values which define the day,year & month
    # @return : True if conditions are met
    #
    def occursOn(self,day, month, year):
        if (self._month == month) and (self._day == day) and (self._year == year):
            return True

    ## Displays the contents of the appointment list
    #
    def printappt(self):
        print('An appointment already is scheduled for that time!')
        print('Day:',self._day,'Month:',self._month, end='')
        print(' Year:',self._year,'Description:',self._description)


## Monthly - SubClass for appoints that are monthly
#
class Monthly(Appointment):
    ##Default Constructor
    # @param day, month, year, description : values which define an appointment
    #
    def init (self, day, month, year, disc):
        super().__init__(self, day, month, year, disc)

    ## Saves the appointment to an out file
    # @param file : a file to write into
    #
    def save(self, file):
        writeStr = "M" + "|" + str(self._day) + "|" + str(self._month) + "|"
        writeStr = writeStr + str(self._year) + "|" + self._description + "\n"
        file.write(writeStr)

    ## Checks whether the appt. occurs on the passed date
    # @param year, month, day : values which define the day,year & month
    # @return : True if conditions are met
    #
    def occursOn(self,day, month, year):
        if (self._month == month) and (self._day == day) and (self._year == year):
            return True

    ## Displays the contents of the appointment list
    #
    def printappt(self):
        print('An appointment already is scheduled for that time!')
        print('Day:',self._day,'Month:',self._month, end='')
        print(' Year:',self._year,'Description:',self._description)

## main
#
def main() :
   # Loading an object list of appointments from a function call  
   appList = loadAppointments("data.txt")

   choice = input("A)dd, L)ist or Q)uit? ").upper()
   
   while choice != "Q" :
      if choice == "L" :
         listAppointments(appList) 
      if choice == "A" :
         addAppointment(appList)

      choice = input("A)dd, L)ist or Q)uit? ").upper()

   # Save all of the appointments.
   print("Saving appointments to outData.txt")
   
   outFile = open("outData.txt", "w")
   
   for app in appList :
      app.save(outFile)
   outFile.close()
   

## Prompt the user for the information for an appointment and add it to the
#  list of appointments.
#  @param appList the list of appointments
#
def addAppointment(appList) :
    
   print("Adding a new appointment: ")
   day = int(input("  Day? "))
   month = int(input("  Month? "))
   year = int(input("  Year? "))
   desc = input("  Description? ")
   app_type = input("O)netime, D)aily or M)onthly? ").upper()

   if app_type == "O" :
      appList.append(OneTime(day, month, year, desc))
   elif app_type == "D" :
      appList.append(Daily(day, month, year, desc))
   elif app_type == "M" :
      appList.append(Monthly(day, month, year, desc))
   else :
      print("That wasn't a valid appointment type.")


## Ask the user for the day, month and year, then list all appointments on
#  the provided date.
#  @param appList the list of appointments to search
#
def listAppointments(appList) :
    
   # Read a date from the user and display all of its appointments.
   day = int(input("Enter the day: "))
   month = int(input("Enter the month: "))
   year = int(input("Enter the year: "))

   # Find all of the appointments on the entered date.
   for app in appList :
      if app.occursOn(day, month, year):
          app.printappt()


## Load the appointments from the file whose name is provied.
#  @param fname the name of the file to load
#
def loadAppointments(fname) :
    
   # Try to open the file.  If that fails, return an empty list of appointments.
   try :
      inFile = open(fname, "r")
   except :
      return []

   # Load all of the appointments from the file, saving them in the list retval.
   retval = []
   
   for line in inFile :
      line = line.strip()
      parts = line.split("|")
      
      if parts[0] == "O" :
         retval.append(OneTime(int(parts[1]), int(parts[2]), int(parts[3]), parts[4]))
      elif parts[0] == "D" :
         retval.append(Daily(int(parts[1]), int(parts[2]), int(parts[3]), parts[4]))
      elif parts[0] == "M" :
         retval.append(Monthly(int(parts[1]), int(parts[2]), int(parts[3]), parts[4]))
      line = line.strip()

   # Close the data file.
   inFile.close()

   # Return the list of appointments.
   return retval


# Call the main function.
main()


















