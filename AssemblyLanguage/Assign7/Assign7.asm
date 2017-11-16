; Program Description: Assign7 – Assembly - Searching & Sorting
; Author: Luis Fernando Escobar-Driver
; Creation Date: 05-04-2016

.386 
.MODEL FLAT 


BubbleSort 	PROTO NEAR32 stdcall,
	pArray:		PTR BYTE,	;pointer to array
	Count:		DWORD		;array size
	
BinarySearch 	PROTO NEAR32 stdcall, 
	pArray:		PTR BYTE, 	; pointer to array
	Count:		DWORD, 		; array size
	searchVal:	DWORD		; search value
	
SequentialSearch PROTO NEAR32 stdcall,
	pArray:		PTR BYTE, 	; pointer to array	
	arraySize:	DWORD, 		; array size
	searchVal:	DWORD 		; search value
	
;CheckBinarySearch PROTO NEAR32 stdcall,
;	searchVal:	DWORD 		; search value	


ExitProcess PROTO NEAR32 stdcall, dwExitCode:dword 

include io.h 

cr EQU 0dh 	; cr = carriage return 
lf EQU 0ah 	; lf = line feed 

.STACK 4096 

.DATA 

szPrompt1 	BYTE 	"Enter an integer to search for: ",0 
szNotFound	BYTE	" was not Found!",0
szFound		BYTE	" was found in index #",0
szIndex 	BYTE 	"Index #: ",0 
szInteger	BYTE	"The integer ",0
szBubbleSort	BYTE	"Performing Bubble Sort!",0
szNewline 	BYTE 	cr, lf, 0 

array		BYTE	4,1,7,12,8,13,9,21
searchNum	DWORD	?

szSearch 	BYTE 	16 DUP (?) 		; input string for numbers 


.CODE 
_start: 

call	outputArray
output	szNewline		

mov	ecx,4
FourTimes:

call	GetSearchNum		;Grabbing a search number
INVOKE 	SequentialSearch, OFFSET array, SIZEOF array, searchNum
output	szNewline		;Newline

loop 	FourTimes		;Looping this segement of code 4 times


output	szNewline
output	szBubbleSort		;Output sorting string
output	szNewline
output	szNewline


INVOKE	BubbleSort, OFFSET array, SIZEOF array
call	outputArray		;Outputting the array
	
mov	ecx,4	
FourMoreTimess:

output	szNewline
call	GetSearchNum		;Grabbing a search number
INVOKE 	BinarySearch, OFFSET array, SIZEOF array, searchNum
call	CheckBinarySearch

loop 	FourMoreTimess		;Looping this segement of code 4 times











INVOKE ExitProcess, 0 

;---------------------------------------------------------------------
CheckBinarySearch PROC 
;
; Inputs  :  Allows the code to check whether the binary search 
;	     found its search value
;
; Receives: eax - index position & searchNum - the number to look for
; Returns : outputs whether the value was found or not
;---------------------------------------------------------------------
mov	edx,eax

cmp	eax,666
je	NoMatch			;Jump if not found else it was found

output	szInteger

mov	eax,searchNum		;Move the search value into eax
dtoa	szSearch,eax		;Decimal to ASCII search value
output	szSearch		;Output the value

output	szFound			;Output Found string

dtoa	szSearch,edx		;Decimal to ASCII on index #
output	szSearch		;Output the index value


output	szNewline		;Output a new line
output	szNewline		;Output a new line

jmp	quit

NoMatch:

mov	ebx,searchNum		;Move the search value into eax
dtoa	szSearch,ebx		;Decimal to ASCII search value
output	szSearch		;Output the value
output	szNotFound
output	szNewline

quit:
mov	eax,edx

	ret
CheckBinarySearch 	ENDP




;---------------------------------------------------------------------
GetSearchNum PROC
;
; Inputs  :  Allows the user to enter a number to search for
;
; Receives: <nothing>
; Returns : searchNum
;---------------------------------------------------------------------
output	szPrompt1
input	searchNum,256	
atod	searchNum
mov	searchNum,eax

	ret
GetSearchNum 	ENDP


;---------------------------------------------------------------------
SequentialSearch PROC NEAR32 stdcall uses ecx edx,
	pArray:		PTR BYTE, 	; pointer to array
	arraySize:	DWORD, 		; array size
	searchVal:	DWORD 		; search value
;
; Inputs  :  linear search of an array, byte by bye. 
;
; Receives: the first address of the array, the size of the array &
;	    the value to search for
; Returns : whether the value was found or not
;---------------------------------------------------------------------	
	mov	eax, 0			;Index (LCV)
	mov	esi, pArray		;Array pointer 
	
L1:	
	cmp	eax, arraySize		;while (index < Count)
	jge	notFound
	mov	edx, 0
	mov	dl, [esi + eax]		;dl = array[eax]
	cmp	edx, searchVal
	je	quit			;if edx == searchVal =>found
	inc	eax			;else inc eax then loop back
	jmp	L1
	
notFound:
	mov	eax,searchVal		;Move the value into eax
	dtoa	szSearch,eax		;Decimal to ASCII
	output	szSearch		;Output the value
	output	szNotFound		;Output the not found string
	output	szNewline		;New line
	mov	eax,666			;Set trigger for not found
	
quit:
	cmp 	eax,666			;Checking trigger
	je	FinishIt		;If it doesnt jump the number was found
	mov	edx,eax			;Saving the index # into ebx
	output	szInteger		;Outputting first phase of found string
	mov	eax,searchVal		;Move the search value into eax
	dtoa	szSearch,eax		;Decimal to ASCII search value
	output	szSearch		;Output the value
	output	szFound			;Output Found string
	dtoa	szSearch,edx		;Decimal to ASCII on index #
	output	szSearch		;Output the index value
	output	szNewline		;Output a new line
	
FinishIt:			
	ret
SequentialSearch	ENDP



;---------------------------------------------------------------------
BinarySearch	PROC NEAR32 stdcall uses ebx edx esi edi, 
	pArray:		PTR BYTE,	; pointer to array 
	Count:		DWORD,		; array size 
	searchVal:	DWORD		; search value 
;
; Inputs  :  A simple searching algorithm that works well for large
;	     arrays of values that have been placed in either 
;	     accending or decending order
;
; Receives: An unsorted int array
; Returns : A sorted int array
;---------------------------------------------------------------------	

LOCAL 	first:	DWORD, 		; first position
	last:	DWORD, 		; last position
	mid:	DWORD 		; midpoint

	mov 	first,0 	; first = 0
	mov 	eax,Count 	; last = (count - 1)
	dec 	eax
	mov 	last,eax
	mov 	edi,searchVal 	; EDI = searchVal
	mov 	ebx,pArray 	; EBX points to the array
L1: 				; while first <= last
	mov 	eax,first
	cmp 	eax,last
	jg 	L5 		; exit search 
	
	; mid = (last + first) / 2
	mov 	eax,last
	add 	eax,first
	shr 	eax,1
	mov 	mid,eax
	
	; EDX = values[mid]
	mov 	esi,mid
	mov	edx, 0
	mov 	dl,[ebx+esi] 	; DX = values[mid]
	
	; if ( EDX < searchval(EDI) )
	; first = mid + 1;
	cmp 	edx,edi
	jge 	L2
	mov 	eax,mid 	; first = mid + 1
	inc 	eax
	mov 	first,eax
	jmp 	L4 		; continue the loop 

L2: 
	cmp 	edx,edi 	; (could be removed)
	jle 	L3
	mov 	eax,mid 	; last = mid - 1
	dec 	eax
	mov 	last,eax
	jmp 	L4 		; continue the loop
	
	; else return mid
L3: 
	mov 	eax,mid 	; VALUE FOUND
	mov	ebx,eax		; Save the value in ebx
	jmp 	L9 		; return (mid)
L4: 
	jmp 	L1 		; continue the loop
L5: 
	mov 	eax,666 	; SEARCH FAILED	
				; ELSE eax holds index number
L9:	
	ret	
BinarySearch	ENDP



;---------------------------------------------------------------------
BubbleSort PROC NEAR32 stdcall USES eax ecx esi, 
	pArray:	PTR BYTE,
	Count:	DWORD 
;
; Inputs  :  Allows a simple sorting algorithm that works well for 
;	     for small arrays.
;
; Receives: An unsorted int array
; Returns : A sorted int array
;---------------------------------------------------------------------
	mov 	ecx,Count 
	dec  	ecx		; decrement count by 1 
L1:
	push 	ecx		; save outer loop count 
	mov  	esi,pArray	; point to first value 
L2:
	mov  	al,[esi]	; get array value 
	cmp  	[esi + 1],al	; compare a pair of values 
	jge  	L3		; if [esi] <= [edi], skip 
	xchg 	al,[esi + 1]	; else exchange the pair 
	mov  	[esi],al 
L3:
	inc 	esi		; move both pointers forward 
	loop 	L2		; inner loop 
	pop  	ecx		; retrieve outer loop count 
	loop 	L1		; else repeat outer loop 
L4:
ret 
BubbleSort ENDP 



;---------------------------------------------------------------------
 outputArray	PROC
;
; Inputs  :  Allows the code to print an entire array of any size
;
; Receives: <none>
; Returns : a printed array
;---------------------------------------------------------------------
mov	ebx,0
mov	eax,0
mov	edi,OFFSET array
mov 	ecx,SIZEOF array

L1:
	mov al,[edi + ebx]
	
	output szIndex
	
	dtoa szSearch,ebx
	output szSearch
	
	dtoa szSearch,eax
	output szSearch
	
	output szNewline
	
	inc ebx
	
	loop L1
	
	ret	
outputArray	ENDP




PUBLIC _start 
END