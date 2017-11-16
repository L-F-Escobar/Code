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


.CODE 
_start: 

call	GetNums


;(Num1 + 28)----------------------------------------
;Using ebx - function value will be stored in ebx
mov 	eax,0
mov	eax,Num1
add	eax,28		;EAX holds the value of (Num1 + 28)


;(-Num2 * 60)----------------------------------------
;using ebx & ecx
;
mov 	ebx,0		;Accumulator
mov	ecx,0		;Processor

mov 	ebx,Num2
shl	ebx,2	
add	ecx,ebx

mov	ebx,Num2
shl	ebx,3
add	ecx,ebx

mov	ebx,Num2
shl	ebx,4
add	ecx,ebx

mov	ebx,Num2
shl	ebx,5
add	ecx,ebx		;
neg	ecx		;ECX holds the value of (-Num2 * 60)



;(Num1 + 28)/(-Num2 * 60)----------------------------------------
mov	edx,0
idiv	ecx		;EAX already holds the proper value
			;Divide (Num1 + 28)/(-Num2 * 60)
			;EAX Holds the value (Num1 + 28)/(-Num2 * 60)
mov	ebx,eax		;EBX Holds the value (Num1 + 28)/(-Num2 * 60)


;(-Num3 % 7)----------------------------------------
;
mov	eax,0		;
mov	edx,0		;
mov	ecx,7		;mod value

mov	eax,Num3	;mov Num3 into eax
neg	eax		;(-Num3)


cmp	eax,0		;If Num3 is negative
jl	NegArith	;Jump to NegArith


#If Num3 is positive go in here to find the mod
PosLoop:
	sub	eax,7		;Sub Num3	
	cmp	eax,7		;Check to see if its less then 7
	jb	CodeBlock	;If it is less then 7 jump
	loop 	PosLoop		;Else loop
	
	jmp	CodeBlock	;Jump to end

jmp	CodeBlock


#If Num3 is negative go in here to find the mod
NegArith:

NegLoop:
	add	eax,7		;Add 7 to Num3
	cmp	eax,0		;If Num3 is greater then 0
	jge	CodeBlock	;If larger then 0 jump to CodeBlock
	jmp	NegLoop		;Else continue till its larger than 0


;EAX = (-Num3 % 7) at this point in the code

CodeBlock:
;(Num1 + 28)/(-Num2 * 60) + (-Num3)
add	ebx,eax

dtoa 	Result,ebx
output 	Result
output	szNewline



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

output 	szPrompt2 			; repeat for second number 
input 	szString,128
atod 	szString 
mov 	Num2, eax 

output 	szPrompt3 			; repeat for third number 
input 	szString,128 
atod 	szString 
mov 	Num3, eax 

	
ret
	
GetNums	ENDP





PUBLIC _start 
END