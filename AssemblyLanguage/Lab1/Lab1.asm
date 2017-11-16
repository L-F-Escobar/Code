; Program Description: Lab#1 –Add Numbers, .......
; Author:
; Creation Date:

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

szPrompt1 	BYTE 	"Enter first number: ",0 
szPrompt2 	BYTE 	"Enter second number: ",0 
szLabel1 	BYTE 	"The sum is: ",0 
dwNumber1 	DWORD 	? 			; numbers to be added 
dwNumber2 	DWORD 	? 
szString 	BYTE 	16 DUP (?) 		; input string for numbers 
szSum 		BYTE 	12 DUP (0) 		; sum in string form 
szNewline 	BYTE 	cr, lf, 0 

.CODE 
_start: 

	output 	szPrompt1 			; prompt for first number
	input 	szString,16 			; input first number as ASCII
	atod 	szString 			; convert to integer 
	mov 	dwNumber1, eax 			; and store in memory 
	output 	szPrompt2 			; repeat for second number 
	input 	szString,16 
	atod 	szString 
	mov 	dwNumber2, eax 
	mov 	eax, dwNumber1 
	add 	eax, dwNumber2 			; add second number to first number 
	dtoa 	szSum, eax 			; convert to ASCII 
	output 	szLabel1 			; output label and results 
	output 	szSum 
	output 	szNewline 

INVOKE ExitProcess, 0 

PUBLIC _start 
END