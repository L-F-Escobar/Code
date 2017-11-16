; Program Description: Assign6 – Recursive Procedure
; Author: Luis Fernando Escobar-Driver
; Creation Date: 04-27-2016

.386 
.MODEL FLAT 

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 


cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

szPrompt1 	BYTE 	"Input a positive integer: ",0 
szNewline 	BYTE 	cr,lf,0
inputNum	DWORD	?
szTest		DWORD	?
Test1		BYTE	"return from first call", 0
Test2		BYTE	"Test2", 0

szSearch 	BYTE 	16 DUP (?) 		; input string for numbers

.CODE 
_start: 


mov	eax,0		;Good habit
call 	GetInput	;Grabs 1 unsigned(positive) input from the user

mov	ebx,0
mov	ecx,0
mov	eax,0
mov	edx,0

cmp	inputNum,0
je	EndOfCode

push	inputNum	;Pass by value onto the stack ([ebp + 8])	
call	Fibonacci	;Calling procedure Fibonacci ([ebp + 4])
dtoa	szSearch,ecx
output	szSearch
EndOfCode:

INVOKE ExitProcess, 0 

;---------------------------------------------------------------------
GetInput PROC
;
; Inputs  :  Allows the user to input 1 positive integer value from 
;	     the console & store it in a memory location labeled 
;	     inputNum
;
; Receives: <nothing>
; Returns : inputNum - the value of the integer selection
;---------------------------------------------------------------------

output	szPrompt1
input	inputNum,32	
atod	inputNum
mov	inputNum,eax		;Saving the value into inputNum

	ret
GetInput 	ENDP



;---------------------------------------------------------------------
Fibonacci  PROC
;
; Inputs  :  
;
; Receives: 
; Returns : 
;---------------------------------------------------------------------
			;Creating a stack frame with the next 2 lines.
push 	ebp 		;Saves previous frame pointer.
mov  	ebp,esp 	;Set current frame pointer.

mov	eax,[ebp + 8]	;Getting argument N 
cmp  	eax,1       	;N <= 1 ?

ja   	Recurse      	;No, compute it recursively
mov	ecx,1
jmp  	exit		;Yes, Unconditional jump to exit

Recurse:  
	dec	eax          	; = N - 1
	mov	edx,eax
	push	edx
	push 	eax
	
	call	Fibonacci
	pop 	eax
	dec	eax
	push	ecx
	push 	eax
	
	call	Fibonacci
	pop	eax
	add	ecx,eax		; = Fib(N-1)+FIB(N-2)

	dtoa	szSearch,ecx
	output	szSearch
  
exit:

	mov  esp,ebp      ; reset stack to value at function entry 
	pop  ebp          ; restore caller's frame pointer

  ret           	  ;And return
Fibonacci  ENDP




PUBLIC _start 
END