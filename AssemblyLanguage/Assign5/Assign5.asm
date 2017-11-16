; Program Description: Assign5 – Greatest Common Divisor
; Author: Luis Fernando Escobar-Driver
; Creation Date: 04-13-2016

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

validGCD	Byte	"The GCD is: " ,0
szPrompt1 	BYTE 	"Enter number one: ",0 
szPrompt2	BYTE 	"Enter number two: ",0
opPrompt 	BYTE 	"The GCD is: ",0
inputNum1	DWORD	?
inputNum2	DWORD	?
szNewline 	BYTE 	cr, lf, 0 
opResult	DWORD	?


.CODE 
_start: 


call 	GetInput	;Grabs 2 inputs from the user
call 	CheckZero	;Checks if either input is 0
jmp 	GCDProc		;Used to skip next lines of code if neither # is 0


;Only executed if either of the numbers are zero, else 
;it is skipped
outputGCD2:		;-------------------------
mov 	eax, inputNum2	;If in this procedure, num
dtoa 	opResult, eax	;one was a 0
output 	opPrompt	;
output 	opResult	;
jmp	endOfProgram	;	
			;


;Only executed if either of the numbers are zero, else 
;it is skipped
outputGCD1:		;-------------------------
mov 	eax, inputNum1	;If in this procedure, num
dtoa 	opResult, eax	;2 was a 0
output 	opPrompt	;
output 	opResult	;
jmp	endOfProgram	;
			;


;If neither number is 0 this will execute
GCDProc:		;-------------------------
mov	ebx,inputNum1	;Passing 2 integer numbers 
mov	ecx,inputNum2	;Passing 2 integer numbers
call 	GCD		;Then calling the procedure
			;


endBlock:		;-------------------------
output	validGCD	
output 	opResult	;Outputting the GCD 
output	szNewline

endOfProgram:
output 	szNewline



INVOKE ExitProcess, 0 


;---------------------------------------------------------------------
GetInput PROC
;
; Inputs  :  Allows the user to input 2 integer values from the console
;
; Receives: <nothing>
; Returns : ebx = inputNum1 && ecx = inputNum2
;---------------------------------------------------------------------
output	szPrompt1
input	inputNum1,32	
atod	inputNum1
mov	inputNum1,eax

output	szPrompt2
input	inputNum2,32	
atod	inputNum2
mov	inputNum2,eax

	ret
GetInput 	ENDP



;---------------------------------------------------------------------
CheckZero PROC
;
; Inputs  : Receives 2 integer values & checks if either of them are 0
;
; Receives: ebx = inputNum1 && ecx = inputNum2
; Returns : the GCD if one of the integers is 0
;---------------------------------------------------------------------

cmp 	inputNum1,0
jbe	outputGCD2

cmp	inputNum2, 0
jbe	outputGCD1


	ret
CheckZero 	ENDP



;---------------------------------------------------------------------
GCD PROC
;
; Inputs  : This procedure receives 2 integers and returns the GCD.
;
; Receives: ebx = inputNum1 && ecx = inputNum2
; Returns : opResult, the GCD
;---------------------------------------------------------------------


mov	eax,0		;Prep the reg for operations
	
cmp	ebx,0		;If num1 is negative 
jb	AbsNumOne	;Then get its absoluate value


continue:		;----------------------------
cmp	ecx,0		;If num2 is negative
jb	AbsNumTwo	;Then get its absolute value
			;
jmp	doWhile		;The numbers can't be negative
			;once this executes
			;


AbsNumOne:		;----------------------------
neg	ebx		;Get absolute value of num1
jmp	continue	;To check num2 for negativity

AbsNumTwo:		;Gets the absolute value of num2
neg	ecx


;Both numbers are already positive in this is procedure
doWhile:		;----------------------------
mov	edx,0		;n = 0
mov	eax,ebx		;eax = num1	
div	ecx		;Divides num1 by num2.
			;EDX = mod/n
			;EAX = remainder
mov	ebx,ecx		;x = y
mov	ecx,edx		;y = n

cmp	ecx,0		
ja	doWhile		;while(y > 0) jump back into the do-while
			;Else
						
dtoa	opResult,ebx	;Saving the GCD and passing it back into code
			;Returning x

	ret
GCD 	ENDP


PUBLIC _start 
END