; Program Description: Assign4 – Implementing a Finite-State Machine
; Author: Luis Fernando Escobar-Driver
; Creation Date: 04-04-2016

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

szPrompt1 	BYTE 	"Enter a string: ",0 
szNewline 	BYTE 	cr, lf, 0 
inputStr 	BYTE 	255 DUP (?) 		
szEnd		BYTE	"!" ,0


Invalid	 	BYTE 	"Invalid termination ",0 
ValidTerm	Byte	"Valid termination " ,0
;test2		BYTE	"continue ",0
;test3		BYTE	"In State B ",0
;test4		BYTE	"IN STATE C ",0
;szSum		BYTE	16 DUP (0)

.CODE 
_start: 

output 	szPrompt1	;Outputing a prompt for a string
input	inputStr,255	;
mov	esi,0		;Moving 0 into esi 

StateA:			;STARTING STATE A------
call	GetNext		;Procedure to extract 1 bit from string.
call 	IsDigit		;Checking if the bit is valid.
jz	StateB		;If State A is valid, go to State B.
jmp	Quit		;If State A fails, Exit.



StateB:			;STARTING STATE B------
call	GetNext		;Procedure to extract 1 bit from string.
call 	IsLowerCase	;Checking if the bit is valid.
;output  test3
jz	StateB		;If the input is valid check for
			;another valid char by going back
			;into State B.

call	IsDigit		;If the next bit was not valid check
			;if it is a digit.
jz	StateC		;If it is a digit go to State C.
jmp	Quit		;Else, it was not a char or digit, 
			;therefore go to Quit.


StateC:			;STARTING STATE C------
;output  test4

call	GetNext		;Procedure to extract 1 bit from string.
call 	IsDigit		;Checking if the bit is a valid int.
jz	StateC		;If State A is valid, back into State C
			;to check if the next bit is also valid.

cmp	al, '!'
je	Valid		;If the next bit is equal to "!"
			;the valid finite state has been met
jmp	Quit		;Else jump to an invalid termination




Valid:			;Valid Termination.
call	GetNext		;Checking to see if there are more values
			;after the ! termination
call	IsDigit		;
jz	Quit		;
call	IsLowerCase	;
jz	Quit		;

output 	ValidTerm	;
jmp	EndThis		;Jump to the end

Quit: 			;Invalid Termination.
output	Invalid

EndThis:

	
INVOKE ExitProcess, 0 


;---------------------------------------------------------------------
GetNext PROC
;
; Inputs one bit at a time from inputStr into AL through [esi]
; Esi must be set to 0 for this procedure to work before the procedure 
; is first called.
;
; Receives: esi position
; Returns : 1 bit from inputStr in AL 
;---------------------------------------------------------------------
mov	al,inputStr[esi]	;Moving 1 bit of the string into AL

;mov	szSum,al		;TESTING
;output szSum			;TESTING

add	esi,TYPE inputStr	;For the next iteration

	ret
GetNext 	ENDP


;---------------------------------------------------------------------
IsDigit PROC
;
; Determines whether the character in AL is a valid decimal digit.
;
; Receives: AL = character
; Returns: ZF = 1 if AL contains a valid decimal digit; otherwise, ZF = 0.
;---------------------------------------------------------------------

    cmp   al,'0'
    jb    ID1           ; ZF = 0 when jump taken, jump is below 0

    cmp   al,'9'
    ja    ID1           ; ZF = 0 when jump taken, jump if above 9

    test  ax,0          ; set ZF = 1
ID1: ret

IsDigit ENDP


;---------------------------------------------------------------------
IsLowerCase PROC
;
; Determines whether the character in AL is a valid lower case letter.
;
; Receives: AL = character
; Returns: ZF = 1 if AL contains a valid decimal digit; otherwise, ZF = 0.
;---------------------------------------------------------------------

    cmp   al,'a'
    jb    LC1           ; ZF = 0 when jump taken, jump if below 'a'

    cmp   al,'z'
    ja    LC1           ; ZF = 0 when jump taken, jump if above 'z'

    test  ax,0          ; set ZF = 1
LC1: ret

IsLowerCase ENDP


PUBLIC _start 
END