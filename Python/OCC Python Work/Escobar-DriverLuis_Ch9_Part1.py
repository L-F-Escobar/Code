###Ch09 Part 1 Section 1
##
#### Counter - Keeps track of how many times a user has clicked
###            a button.
##class Counter:
##    
##    ## Default Constructor
##    #
##    def __init__(self, initValue = 0):
##        #Private instance variables
##        self._value = initValue
##    
##    ## Advances the value of this counter by 1
##    #
##    def click(self):
##        self._value = self._value + 1
##
##    ## Gets the current avalue of this counter.
##    # @return : the current value
##    #
##    def getValue(self):
##        return self._value
##
##    ## Resets the value of this coutner to 0
##    #
##    def reset(self):
##        #Calling the default constructor to reset the values
##        self._value = 0
##        
##    ## Decrements the value by 1
##    #
##    def undo(self):
##        #If the undo button has not been clicked more
##        if (self._value)  > 0:
##            self._value = self._value - 1
##        #Else the undo button has been clicked more
##        else:
##            print('Nothing to undo!')
##
##       
###Creating a Counter object which can access all Counter methods
###Plus calling the default constructor
##tally = Counter()
##
###Object calling the reset method
##tally.reset()
##
###Object calling the click method twice
##tally.click()
##tally.click()
###Object calling the getValue method and saving the value
##result = tally.getValue()
##print("Result: ",result)
##
##tally.click()
##result = tally.getValue()
##print("Result: ",result)
##
##tally.undo()
##tally.undo()
##result = tally.getValue()
##print("Result: ",result)
##
##tally.undo()
##tally.undo()
##result = tally.getValue()
##print("Result: ",result)
##
##
###Ch09 Part 1 Section 2
##
#### Counter - Keeps track of how many times a user has clicked
###            a button.
##class Counter:
##    
##    ## Default Constructor
##    #
##    def __init__(self, initCount = 0):
##        #Private instance variables
##        self._count = initCount
##    
##    ## Advances the value of this counter by 1
##    #
##    def click(self):
##        if self._maximum > self._count:
##            self._count = self._count + 1
##        else:
##            print('Limit exceeded')
##
##    ## Gets the current avalue of this counter.
##    # @return : the current value
##    #
##    def getValue(self):
##        return self._count
##
##    ## Resets the value of this coutner to 0
##    #
##    def reset(self):
##        #Calling the default constructor to reset the values
##        self._count = 0
##        
##    ## Decrements the value by 1
##    #
##    def undo(self):
##        #If the undo button has not been clicked more
##        if (self._count)  > 0:
##            self._count = self._count - 1
##        #Else the undo button has been clicked more
##        else:
##            print('Nothing to undo!')
##
##    ## Set a maximum allowed limit of clicks allowed
##    #
##    def setLimit(self, maximum):
##        self._maximum = maximum
##
###Creating a Counter object with initial values of 0.
##tally = Counter()
###Setting the maximum allowed limit to 2
##tally.setLimit(2)
##
###2 clicks
##tally.click()
##tally.click()
##
###Printing value
##result = tally.getValue()
##print("Result: ",result)
##
###One more click 
##tally.click()
##result = tally.getValue()
##print("Result: ",result)

#Ch09 Part 1 Section 3
## SodaCan - Calculates the volume & surface area of a soda can
#
class SodaCan:
    #Class const. variable shared by all instances.
    PI = 3.14

    ##Default constructor with initial values
    #
    def __init__(self, initHeight = 0.0, initRadius = 0.0):
        #instance variable unique to each instance
        self._height = initHeight
        #instance variable unique to each instance
        self._radius = initRadius

    ## Receives the height & radius. Calcs the surface area of a can
    # @return : the surface area of the given specifics
    #
    def GetSurfaceArea(self):
        self.Surface = (3.14 * 2 * self._height * self._radius) + (3.14 * 2 * self._radius**2)
        return self.Surface

    ## Receieves the height & radius. Calcs the volume of a can
    # @return : the volume of the given specifics
    #
    def GetVolume(self):
        self._Volume = (self._radius**2 * self._height * 3.14)
        return self._Volume
    
#Calling the default constructor with specific values for the
#init.
can = SodaCan(2,4)

#Printing the values
print("The volume of the can is: ", can.GetVolume())
print("The surface area of the can is: ", can.GetSurfaceArea())


























