/*
 *************************************************************************
 ********* CHAPTER 04 - Data Transfers, Addressing & Arithmetic *******
 *************************************************************************

 *
 *
 *
 * Direct memory operands
 	.data
	var1 BYTE 10h
	.code
	mov al,var1   ; AL = 10h
	mov al,[var1] ; AL = 10h  //Alternate form


 *
 *
 *
 * MOV Instruction
    mov 'destination', 'source'

    CS, EIP & IP cannot be the destination

    .data
		count BYTE 100
		wVal  WORD 2
	.code
		mov bl,count
		mov ax,wVal
		mov count,al
		mov al,wVal 	; error, size mismatch all
		mov ax,count 	; error
		mov eax,count 	; error


 *
 *
 *
 * Zero Extension
    MOVZX - when you copy a smaller value into a larger destination
    		the MOVZX instruction fills the upper half of the
    		destination with zeros

    		ex.	mov   bl,10001111b		ah		al
				movzx ax,bl 	  ;[00000000][100011111]
								  ;[		ax		   ]
								  ; zero-extension

	MOVSX - instruction fills the upper half of the destination
			with a copy of the sources operand's sign bit


									;BH   BL
			mov bl, 100011111b		;[ ][10001111] - BX
			movsx ax, bl			;    AH		   AL
  	  	  	  	  	  	  	  	  	;[11111111][10001111] - AX

 	 	 //essentially copies the first bit

 *
 *
 *
 * XCHC Instruction
    xchg changes the values of two operands. AT LEAST ONE operand
    must be a register. No immediate operands are permitted

    .data
		var1 WORD 1000h
		var2 WORD 2000h
	.code
		xchg ax,bx 		; exchange 16-bit regs
		xchg ah,al 		; exchange 8-bit regs
		xchg var1,bx 	; exchange mem, reg
		xchg eax,ebx 	; exchange 32-bit regs
		xchg var1,var2 	; error: two memory operands


 *
 *
 *
 * Direct offset operands
    A constant offset is added to a data label to produce an
    effective address(EA). The address is dereferenced to get the
    value inside its memory location.


    .data			[0],[1],[2],[3] - because its BYTES
		arrayB BYTE 10h,20h,30h,40h
	.code
		mov al,arrayB+1 	; AL = 20h
		mov al,[arrayB+1] 	; alternative notation

	.data			[0]  , [2] , [4] - because its in 16 bits
		arrayW WORD 1000h,2000h,3000h
				    [0],[4],[8],[12] - because its in 32 bits
		arrayD DWORD 1,  2,  3,  4
	.code
		mov ax,[arrayW+2] 	; AX = 2000h
		mov ax,[arrayW+4] 	; AX = 3000h
		mov eax,[arrayD+4] 	; EAX = 00000002h


 *
 *
 *
 * Addition  &  Subtraction

   Flags affected by arithmetic
    - Zero     : set when destination equal zero
    - Sign 	   : set when destination is negative
    - Carry	   : set when unsigned value is out of range
    - Overflow : set when signed value is out of range

    	mov instruction never affects the flags
    	• A flag is set when it equals 1.
		• A flag is clear when it equals 0.

* INC and DEC Examples
	.data
		myWord WORD 1000h
		myDword DWORD 10000000h
	.code
		inc myWord 	; 1001h
		dec myWord 	; 1000h
		inc myDword ; 10000001h
		mov ax,00FFh
		inc ax 		; AX = 0100h //Incs the 16 bit reg
		mov ax,00FFh
		inc al 		; AX = 0000h //Incs the 8 bit reg, therefore
								 //no carry
								  *
 * Show the value of the destination operand after each of the
   following instructions executes:
	.data		[1]     , [2]
		myByte BYTE 0FFh, 0
	.code
		mov al,myByte 		; AL = FFh
		mov ah,[myByte+1] 	; AH = 00h
		dec ah 				; AH = FFh
		inc al 				; AL = 00H
		dec ax 				; AX = FEFFh


 * ADD & SUB examples
 	 .data
		var1 DWORD 10000h
		var2 DWORD 20000h
	.code 				; ---EAX---
		mov eax,var1 	; 00010000h
		add eax,var2 	; 00030000h
		add ax,0FFFFh 	; 0003FFFFh
		add eax,1 		; 00040000h
		sub ax,1 		; 0004FFFFh


 * NEG(negate) Instruction
    Reverse the sign of an operand(by doing its 2 complement).
    Operand can be a register or memory operand.

    .data
		valB BYTE -1
		valW WORD +32767
	.code
		mov al,valB ; AL = -1
		neg al 		; AL = +1
		neg valW 	; valW = -32767
 	 //HAVE to be careful when you use negate because you might
 	  * negate a number that doesnt exist, absolute negatives
 	  * go out of range for the positibes. Look at 8, 16, 32
 	  * bit unsigned & signed ranges


 *	Rval = -Xval + (Yval - Zval) - Implementing Arith. Expressions

 	 	Rval DWORD ?
		Xval DWORD 26
		Yval DWORD 30
		Zval DWORD 40
	.code
		mov eax,Xval
		neg eax 		; EAX = -26
		mov ebx,Yval
		sub ebx,Zval 	; EBX = -10
		add eax,ebx
		mov Rval,eax 	; -36

 * Rval = Xval - (-Yval + Zval) - Implementing Arith. Expressions

 	 	mov ebx,Yval
		neg ebx
		add ebx,Zval
		mov eax,Xval
		sub eax,ebx
		mov Rval,eax


 * Zero Flag (ZF)
 	 The Zero flag is set when the result of an operation produces
	 zero in the destination operand.

	mov cx,1
	sub cx,1 		; CX = 0, ZF = 1
	mov ax,0FFFFh
	inc ax 			; AX = 0, ZF = 1
	inc ax 			; AX = 1, ZF = 0


 * Sign Flag (SF)
 	 The Sign flag is set when the destination operand is negative.
	 The flag is clear when the destination is positive.

  	  	mov cx,0
		sub cx,1 	; CX = -1, SF = 1
		add cx,2 	; CX = 1,  SF = 0
	The sign flag is a copy of the destination's highest bit:

		mov al,0
		sub	al,1 ; AL = 11111111b, SF = 1
		add al,2 ; AL = 00000001b, SF = 0

 * Carry Flag (CF)
    The Carry flag is set when the result of an operation generates an
	unsigned value that is out of range (too big or too small for the
	destination operand).

	mov al,0FFh
	add al,1 	; CF = 1, AL = 00
				; Try to go below zero:
	mov al,0
	sub al,1 	; CF = 1, AL = FF


 * For each of the following marked entries, show the values of
	the destination operand and the Sign, Zero, and Carry flags:

	Sign Flag (SF), Carry Flag (CF), Zero Flag (ZF)

	mov ax,00FFh
	add ax,1 		; AX= 00FFh SF= 0 ZF= 0 CF= 0
	sub ax,1 		; AX= 00FFh SF= 0 ZF= 0 CF= 0
	add al,1 		; AL=   00h SF= 0 ZF= 1 CF= 1
	mov bh,6Ch
	add bh,95h 		; BH= 01  h SF= 0 ZF= 0 CF= 1
	mov al,2
	sub al,3 		; AL=   FFh SF= 1 ZF= 0 CF= 1 //Now negative

 * Overflow Flag (OF)
    The Overflow flag is set when the signed result of an operation is
	invalid or out of range

		; Example 1
			mov al,+127
			add al,1 	; OF = 1, AL = ??
		; Example 2
			mov al,7Fh
			add al,1 	; OF = 1, AL = 80h

		mov al,-128
		neg al 		; CF = 1 OF = 1
		mov ax,8000h
		add ax,2 	; CF = 0 OF = 0
		mov ax,0
		sub ax,2 	; CF = 1 OF = 0
		mov al,-5
		sub al,+125 ; 	     OF = 1


 *
 *
 *
 * Data-Related Operators & Directives
	OFFSET Operator
		- Protected Mode: 32 bits
		  Real Mode		: 16 bits

		  Let's assume that the data segment begins at 00404000h:

		  .data
			bVal  BYTE ?
			wVal  WORD ?
			dVal  DWORD ?
			dVal2 DWORD ?
		 .code
			mov esi,OFFSET bVal  ; ESI = 00404000
			mov esi,OFFSET wVal  ; ESI = 00404001
			mov esi,OFFSET dVal  ; ESI = 00404003
			mov esi,OFFSET dVal2 ; ESI = 00404007

	PTR Operator
		- The value returned by OFFSET is a pointer. Compare the
		  following code written for both C++ and assembly language:

		  ; Assembly language:				//C++
			.data
				array BYTE 1000 DUP(?)		char array[1000];
			.code							char *p = &array;
				mov esi,OFFSET array

	TYPE Operator
	LENGTHOF Operator
	SIZEOF Operator
	LABEL Operator

	////// STOPPED ON CH04 SLIDE 54







 *
 *
 *
 */



