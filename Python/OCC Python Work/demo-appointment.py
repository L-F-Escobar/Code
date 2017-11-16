def main() :
   # Load the list of appointments.
   appList = loadAppointments("data.txt")

   choice = input("A)dd, L)ist or Q)uit? ").upper()
   while choice != "Q" :
      if choice == "L" :
         listAppointments(appList) 
      if choice == "A" :
         addAppointment(appList)

      choice = input("A)dd, L)ist or Q)uit? ").upper()

   # Save all of the appointments.
   print("Saving appointments to data.txt")
   
   outf = open("data.txt", "w")
   for app in appList :
      app.save(outf)
   outf.close()


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
      appList.append(Onetime(day, month, year, desc))
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
      if app.occursOn(day, month, year) :
         app.printappt()


## Load the appointments from the file whose name is provied.
#  @param fname the name of the file to load
#
def loadAppointments(fname) :
   # Try to open the file.  If that fails, return an empty list of appointments.
   try :
      inf = open(fname, "r")
   except :
      return []

   # Load all of the appointments from the file, saving them in the list retval.
   retval = []
   for line in inf :
      line = line.strip()
      parts = line.split("|")
      if parts[0] == "O" :
         retval.append(Onetime(int(parts[1]), int(parts[2]), int(parts[3]), parts[4]))
      elif parts[0] == "D" :
         retval.append(Daily(int(parts[1]), int(parts[2]), int(parts[3]), parts[4]))
      elif parts[0] == "M" :
         retval.append(Monthly(int(parts[1]), int(parts[2]), int(parts[3]), parts[4]))

   # Close the data file.
   inf.close()

   # Return the list of appointments.
   return retval


# Call the main function.
main()
