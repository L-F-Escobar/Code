#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
import sys#, pyperclip - same
import pyperclip#Can send text to and receive text from your computer’s clipboard

if len(sys.argv) < 2:#Triggers if user types PWM into cmd line
    print('Usage: python PWM.py [account] - copy account password')
    sys.exit()

#If this triggers the user has typed in at least one argument PWM odin    
account = sys.argv[1] #First cmd line argument is the account name

print(account)#Will print out the first ARGUMENT
print(sys.argv[1])#Same thing as the above code of line. argv[1] means 1st agru
print(len(sys.argv))#Will pring out every variable input into the cmd line

if account in PASSWORDS:#looking for the key
    pyperclip.copy(PASSWORDS[account])#Copies 
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
