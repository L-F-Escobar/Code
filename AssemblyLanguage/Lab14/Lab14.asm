; Program Description: Lab#14 – Arithmetic Expressions II .......
; Author: Luis Fernando Escobar-Driver
; Creation Date: 04-14-2016

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

szPrompt1 	BYTE 	"Enter first number:  ",0 
szPrompt2 	BYTE 	"Enter second number: ",0 
szPrompt3	BYTE	"Enter third number:  ",0
szLabel1 	BYTE 	"The result is: ",0 
Num1 		DWORD	?				; numbers to be added 
Num2 		DWORD 	?
Num3		DWORD	?
szString 	BYTE 	256 DUP (?) 			; input string for numbers 
Result 		BYTE 	256 DUP (0) 			; Result in string form 
szNewline 	BYTE 	cr, lf, 0 

sour		BYTE	"brown",0
destin		BYTE	"brine",0

.CODE 
_start: 

lea	esi,sour+4
lea	edi,destin+4
std
mov	ecx,3

rep	movsb


dtoa	Result,ecx
output	Result
output	destin
output	sour



INVOKE ExitProcess, 0 

;---------------------------------------------------------------------
GetNums PROC
;
; Inputs  :  Allows the user to input 3 integer values from the console
;
; Receives: <nothing>
; Returns : Num1, Num2 & Num3 variables with stored values 
;---------------------------------------------------------------------

output 	szPrompt1 			; prompt for first number
input 	szString,128			; input first number as ASCII
atod 	szString 			; convert to integer 
mov 	Num1, eax 			; and store in memory 
	
ret
	
GetNums	ENDP





PUBLIC _start 
END