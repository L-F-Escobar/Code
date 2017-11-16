; Program Description: Lab#2 –Multiplication - Loop, .......
; Author: Luis Fernando Escobar-Driver
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
num1	 	BYTE 	? 			; numbers to be added 
num2	 	BYTE 	? 
szString 	BYTE 	16 DUP (?) 		; input string for numbers 
szProd 		BYTE 	12 DUP (0) 		; product in string form 
szNewline 	BYTE 	cr, lf, 0 

.CODE 
_start: 

	output 	szPrompt1 			; prompt for first number
	input 	szString,16 			; input first number as ASCII
	atod 	szString 			; convert to integer 
	mov 	num1, al 			; and store in memory 
	output 	szPrompt2 			; repeat for second number 
	input 	szString,16 
	atod 	szString 
	mov 	num2, al 
	movzx	cx, num2			; set LCV
	dec	cx				; decrements the LCV
	mov	al, num1
looper:						; lopp label
	add 	al, num1			; add first number to itself
	loop	looper				; loops to previous line
	
	
	dtoa 	szProd, eax 			; convert to ASCII 
	output 	szLabel1 			; output label and results 
	output 	szProd 
	output 	szNewline 

INVOKE ExitProcess, 0 

PUBLIC _start 
END 