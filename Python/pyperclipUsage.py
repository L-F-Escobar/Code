#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

receive = pyperclip.paste()#Takes from clipboard 

#lines becomes a LIST [line1, line2, line3, etcetc]
lines = receive.split('\n')#split spits out lists

for index in range(len(lines)):
    lines[index] = '*' + lines[index]#Mod each line and save it

send = '\n'.join(lines)#Join all the index items together into a string
                       #seperated by \n
    
pyperclip.copy(send)#Sends to the clipboard



