; Program Description: Lab#9 – Table Driven selection, .......
; Author: Luis Fernando Escobar-Driver
; Creation Date: 03-28-2016

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

Switch	BYTE 1				; lookup value 

	DWORD Addition			; address of procedure 
	EntrySize = ($ - Switch) 
	
	BYTE 2 
	DWORD Subtraction 
	
	BYTE 3 
	DWORD Multiplication 
	
	BYTE 4 
	DWORD Division 
	
NumberOfEntries = ($ - Switch) / EntrySize 


inputNum1	DWORD	?				;Number 1
inputNum2	DWORD	?				;Number 2
inputSelect	DWORD	?				;User input selection
InputString	BYTE	256 DUP (?)			;ASCII version of number
OutputString	BYTE	256 DUP (?)			;ASCII version of number

adding		BYTE	"Adding",cr,lf,0
subtract	BYTE	"Subracting",cr,lf,0
dividing	BYTE	"Dividing",cr,lf,0
multiplic	BYTE	"Multipling",cr,lf,0
InputPrompt1	BYTE	"Enter the first number: ",0	;Prompt
InputPrompt2	BYTE	"Enter the second number: ",0	;Prompt
szNewline 	BYTE 	cr, lf, 0 			;new line


table		BYTE "Select the operation to be performed",cr,lf,
		     "	1-Addition",cr,lf,
		     "	2-Subtraction",cr,lf,
		     "	3-Multiplication",cr,lf,
		     "	4-Division",cr,lf,
		     "Enter your selection: ",0
		     
tableSelect	BYTE	?				;User input selection
opResult	DWORD	?



.CODE 
_start: 
	
	;INPUT FIRST & SECOND NUMBER PROCESSES
	
	;Input for the first number
	output	InputPrompt1
	input	InputString,16		;input first number as ASCII
	atod	InputString		;convert to integer
	mov	inputNum1, eax		;and store in memory

	;Input for the second number
	output	InputPrompt2		
	input	InputString,16 		;input second number as ASCII
	atod	InputString 		;convert to integer
	mov	inputNum2, eax 		;and store in memory
	
	;Output the selection table
	output table
	
	;Saving the user selection from the table into inputSelect
	input	InputString,16		;input number as ASCII
	atod	InputString		;convert to integer
	mov	inputSelect, eax	;and store in memory

	
	
	
	
	
	

	mov ebx,OFFSET Switch		; point EBX to the table 
	mov ecx,NumberOfEntries		; loop counter 
	
	
L1: 	cmp al,[ebx]			; match found? 
	jne L2				; no: continue 
	call NEAR PTR [ebx + 1]		; yes: call the procedure 
	jmp L3				; and exit the loop 
	
	
L2:	add ebx,EntrySize		; point to next entry 
	loop L1				; repeat until ECX = 0 
	
	
L3: 	;End Program
	mov eax,opResult
	dtoa OutputString, eax
	output OutputString



INVOKE ExitProcess, 0 



;**********************************************
 Addition	PROC
;
; This procedure adds two integers 
;
;**********************************************	

output adding
mov edx,inputNum1
add edx,inputNum2
mov opResult,edx
	
	ret
	
Addition	ENDP




;**********************************************
 Subtraction	PROC
;
; This procedure subtracts two integers 
;
;**********************************************
output subtract
mov edx,inputNum1
sub edx,inputNum2
mov opResult,edx

	ret
		
Subtraction	ENDP



;**********************************************
 Multiplication	PROC
;
; This procedure multiplies two intergers 
;
;**********************************************
output multiplic
mov eax,inputNum1
mul inputNum2
mov opResult,eax

	ret
		
Multiplication	ENDP




;**********************************************
 Division	PROC
;
; This procedure divides two intergers  
;
;**********************************************

output dividing

mov edx,0
mov eax,inputNum2
div inputNum1
mov opResult,edx

	ret
		
Division	ENDP




PUBLIC _start 
END