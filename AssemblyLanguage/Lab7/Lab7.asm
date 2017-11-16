; Program Description: Lab#7 – Reversing a String, .......
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

szPrompt1 	BYTE 	"Enter a string: ",0 
szPrompt2	BYTE	"Your result is: ",0
inputStr	BYTE 	50 DUP (?) 		; input string for any name as large as 50 bits
nameSize 	= ($ - inputStr) - 1		; gets the size of the string for indexing purposes 
szNewline 	BYTE 	cr, lf, 0 

szTest		BYTE	"TESTING THSI SHIT",0


.CODE 
_start: 

	output  szPrompt1 			; prompt for first number
	input 	inputStr,50			; input first number as ASCII

	mov	esi, OFFSET inputStr		; moving first byte address into esi

	call relevantAscII			; getting the count of all the ASCII characters
						; number of ascii chars in ecx
	mov	ebx, ecx			;moves number into ebx aka safe location
	
	mov	edx, OFFSET inputStr		; get the first address of the string
		
	call reverseStr				; calling the function/procedure
	
	output szPrompt2
	output inputStr
	output szNewline
	
INVOKE ExitProcess, 0 



;**********************************************
 reverseStr	PROC
;
; This procedure reverses the inputStr. 
;
;
;
;
;
;**********************************************	
	mov ecx, ebx 			; moves the total number of 
					; ascii chars into the counter
	mov esi, edx			; moves the address of inputStr 
					; into the point reg

L1:
	movzx eax, BYTE PTR[esi]	; this gets the first bit, bit 0
	push  eax			; 
	inc   esi			; to get the next bit
	Loop L1

	mov ecx,ebx			; repeating the process at the
					; beginning of the procedure
	mov esi,edx			

L2:
	pop eax				; popping the stack, last first
	mov BYTE PTR[esi],al		; moving one byte at a time into al reg
	inc esi				; on to the next address
	Loop L2
	
	ret
	
reverseStr	ENDP


;**********************************************
 relevantAscII	PROC
;
; This procedure essentially allows the code
; to get the length of the actualy characters
; in inputStr. 
;
;**********************************************
	mov ecx,0	; setting the index to 0

L3:
	mov  al, [esi]	; Moving character into al
	test al, al	; tests if the character is 0
	je	L4	; jump if = 0
	inc  ecx	; increment ecx, the final number
			; will be the total ascii chars
	inc  esi	; increment esi, the final 
			; address will be saved			
	jmp  L3		; jump to top of loop

L4:

	ret
	
relevantAscII	ENDP

PUBLIC _start 
END