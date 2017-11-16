; Program Description: Assignment #8 - Assembly - Linked List
; Author: Lord Lucifer
; Creation Date: 5/(-_-)/16

.386 
.MODEL FLAT

ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 
cr EQU 0dh			; cr = carriage return
lf EQU 0ah 			; If = line feed

;FROM SLIDES - REVIEW MORE
ListNode STRUCT
	nodeData	DWORD	?
	nextPtr		DWORD	?
ListNode ENDS

;Initilizations - 
TotalNodeCount = 50
NULL 	       = 0
Counter        = 0

.STACK 4096 

.DATA

;FROM SLIDE - REVIEW MORE
LinkedList 	LABEL PTR ListNode 	;//will create a singly linked list
REPEAT		TotalNodeCount 		;//Generating nodes // repeats 50 times
		Counter = Counter + 1 	;//will fill from 1-50(int vlaues)
		ListNode <Counter, ($ + Counter * SIZEOF ListNode)>;//Same as the node ptr in c++(linker)
ENDM

;FROM SLIDES - REVIEW MORE
ListNode	<0,0>   ; tail node

Prompt		BYTE	"Enter an integer to search for: ",0
Output1		BYTE	" was found at address ",0
Output2		BYTE	" was not found!",0

inputNum	DWORD	?			; first input from the user
szString	BYTE 	16 DUP (?)		; input string for numbers
opResult	BYTE	12 DUP (0)		; The result	
szNewline	BYTE	cr, lf, 0

foundAddr	DWORD	?

.CODE
_start:

call		PrintList

output		Prompt		; prompt for a number
input		szString, 16	; input a number into ASCII
atod		szString	; convert to integer
mov 		inputNum, eax	; eax stored into input


output		szNewline
	
INVOKE ExitProcess, 0

;----------------------------
PrintList PROC
;----------------------------

mov		esi, OFFSET LinkedList

NextNode:
; Check for the tail node
mov		eax, (ListNode PTR [esi]).nextPtr
cmp		eax, NULL
je		over

; Display the node data.
mov		eax, (ListNode PTR [esi]).nodeData
dtoa		opResult, eax
output		opResult
output		szNewline

; Get pointer to next node
mov 		esi,(ListNode PTR [esi]).nextPtr
jmp 		NextNode

over: ret
PrintList ENDP

;----------------------------
SequentialSearch PROC
;----------------------------

mov		ecx, TotalNodeCount
mov		esi, LinkedList

.WHILE		ecx != 0
cmp		(ListNode PTR [esi]).nodeData, ebx
je		Found
mov		esi, (ListNode PTR [esi]).nextPtr
dec		ecx
.ENDW

mov		eax, -1
jmp		NotFound

Found: 
mov		foundAddr, esi
mov		edx, TotalNodeCount
sub		edx, ecx
mov		eax, edx

NotFound: ret

SequentialSearch ENDP

PUBLIC _start
END