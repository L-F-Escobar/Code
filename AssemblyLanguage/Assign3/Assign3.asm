; Program Description: Assign3 – Assembly Division/Procedure, .......
; Author: Luis Fernando Escobar-Driver
; Creation Date: 03-02-2016

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

szPrompt1 	BYTE 	"Enter number one: ",0 
szQuotient 	BYTE 	"The quotient is: ",0 
szPrompt2	BYTE	"Enter number two: ",0
szNewline 	BYTE 	cr, lf, 0 
num1		DWORD	?
num2		DWORD	?
remain		DWORD	?
quout		DWORD	?
szString 	BYTE 	16 DUP (?) 		; input string for numbers 
szProd 		BYTE 	12 DUP (0) 		; product in string form 

.CODE 
_start: 

	call validNum		; Calling func. to prompt/check for valid inputs

	mov eax,edx		; moving num1 into eax
	mov ecx,ebx		; moving num2 into the loop counter
	mov ebx,0

	call firstPro		; Division by subtraction 
	call roundOff		; Rounding off the remainder
	
	call secondPro		; Division by assmebly div
	
INVOKE ExitProcess, 0 



;**********************************************************
 validNum	PROC
;
; User input must be within range of 1-200
; This function functions as a do-while loop
;
;
;**********************************************************	

L1:
	output 	szPrompt1 			; prompt for first number
	input 	szString,16 			; input first number as ASCII
	atod 	szString 			; convert to integer 
	mov 	num1, eax 			; and store in memory 	
	mov 	edx, num1			; storing num1 in edx

	cmp 	edx,200				; jump back to L1 if input is above 200
	ja L1					; the actual jump
	
	cmp	edx, 1				; jump back to L1 if input is below 1
	jb L1					; the actual jump
	
	output szNewline

L2:
	output 	szPrompt2 			; prompt for first number
	input 	szString,16 			; input first number as ASCII
	atod 	szString 			; convert to integer 
	mov 	num2, eax 			; and store in memory 
	mov 	ebx,num2			; storing num1 in ebx
	
	cmp 	ebx,200				; jump back to L2 if input is above 200
	ja L2					; the actual jump
	
	cmp	ebx,1				; jump back to L2 if input is below 1
	jb L2					; the actual jump
	
	output szNewline

 	; when the code reaches this point
 	; both inputs are valid
 	
	ret
	
validNum	ENDP




;**********************************************************
 firstPro	PROC
;
; This function performs a division program through 
; mutliple suctractions. eax is the number being divided
; ebx is the quotient
; ecx originally is num2, being counted down with each jmp
; 
;**********************************************************	


looper:
	sub eax,num2		; after the loop eax will have the remainer 
	
	cmp eax,0		; if num1 >= num2 : jmp if num1 < num2
	jl exit			
	
	inc ebx			; inc the quotient
	jmp normal		; jump back into the outer loop

exit:
	add eax,num2		; add the divisor to the remainer
	jmp normal		; jump back into the outer loop
		
normal:				; the gate to the outer loop
	
	loop looper		; End outer loop

 	
	ret
	
firstPro	ENDP






;**********************************************************
 roundOff	PROC
;
; This function arounds off the remainder. The function
; takes the value at ecx(2) and multiplies the remainder.
; Then the remainder is subtracted by num2 and compared 
; against zero. If the reaminder is greater then 0 the 
; quotient is incremented one more time.
; Rounds .5 & over
;
;**********************************************************	
	
	mov ecx,2		; storing 2 for later calc
	mul ecx			; 2 * eax
	sub eax,num2		; eax - divisor
	cmp eax,0		
	jl incQuot
	
	inc ebx
incQuot:			

	dtoa 	quout,ebx	; turning quotient into a string
	output szQuotient	; 
	output  quout		; outputing quotient
	output szNewline

	ret
	
roundOff	ENDP




;**********************************************************
 secondPro	PROC
;
; This function performs an assembly division instruction
;
;**********************************************************

	mov 	edx, 0		; clearing out edx
	div 	num2		; dividing eax by num2
	dtoa 	quout,eax	; converting to a string
	output 	szQuotient
	output 	quout
	output szNewline
	


	ret	
secondPro	ENDP






PUBLIC _start 
END